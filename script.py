# import pandas as pd
# import os,sys
# try:
#     file_name = sys.argv[1]
#     if file_name !="":
#         df = pd.read_excel(f'./Inital_files/{file_name}.xlsx')
#         df = pd.DataFrame(df)
#     else:
#         raise Exception(f"File with name {file_name} not found")
# except:
# #   print('File not found')
#   exit()
# else:
#   try:
#         print(file_name)
#         payment_amount = []

#         for index,row in df.iterrows():
#             if pd.notnull(row['credit']) and pd.notnull(row['debit']):
#                 diff = row['credit']-row['debit']
#                 if diff>0:
#                     payment_amount.append(f'+{diff:.2f}')
#                 else:
#                     payment_amount.append(f'{diff:.2f}')
#             else:
#                 if pd.notnull(row['credit']):
#                     payment_amount.append(row['credit'])
#                 elif pd.notnull(row['debit']):
#                     payment_amount.append(f"-{row['debit']}")
#                 else:
#                     payment_amount.append('0')

#         df['payment_amount'] = payment_amount
#         df['Total Amount Paid to ME A/c'] = payment_amount
#         if os.path.exists(f'./Final_files/final_{file_name}.xlsx'):
#             os.remove('./Final_files/final_{file_name}.xlsx')
#             df.to_excel('./Final_files/final_{file_name}')
#             print('File with same name overwritten successfully')
#         else:
#             df.to_excel('./Final_files/final_{file_name}')
#             print('File created successfully')
  
#   except:
#       print('Something went wrong while processing the file')

# downlaod pandas,openpyxl


import pandas as pd
import os
import sys

def calculate_payment_amount(row):
    if pd.notnull(row['credit']) and pd.notnull(row['debit']):
        diff = row['credit'] - row['debit']
        if diff > 0:
            return f'+{diff:.2f}'
        else:
            return f'{diff:.2f}'
    elif pd.notnull(row['credit']):
        return f'+{row["credit"]:.2f}'
    elif pd.notnull(row['debit']) and row['debit'] != 0:
        return f'-{row["debit"]:.2f}'
    else:
        return '0'

def process_file(file_name):
    try:
        output_file_path = f'./final_{file_name}.xlsx'
        if os.path.exists(output_file_path):
            print(f"Error: File with name final_{file_name}.xlsx already exists.")
            sys.exit()
        df = pd.read_excel(f'./{file_name}.xlsx')
        df['payment_amount'] = df.apply(lambda row: calculate_payment_amount(row), axis=1)
        df['Total Amount Paid to ME A/c'] = df['payment_amount']

        df.to_excel(output_file_path, index=False)
        print('File created successfully')

    except FileNotFoundError:
        print(f"File with name {file_name} not found")
        sys.exit()
    except Exception as e:
        print(f'Something went wrong while processing the file: {e}')

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print("Syntax: python3 script_name.py <file_name>")
        sys.exit()

    file_name = sys.argv[1]
    if file_name:
        process_file(file_name)
    else:
        print("Please provide a valid file name")
