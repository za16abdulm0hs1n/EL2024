import re       
import openpyxl
import os
import string


"""The re module allows you to work with regular expressions in Python,
which are powerful tools for pattern matching and string manipulation.
Here are some common tasks you can accomplish with re: https://docs.python.org/3/library/re.html#"""


def get_header_file_path():
    head_file_path = input("Please Enter Valid Path for C/C++ Header File: ")
    while not os.path.exists(head_file_path):
        print(f"The Path {head_file_path} is Invalid!")
        head_file_path = input("Please Enter Valid Path for C/C++ Header File: ")
    return head_file_path

#---------------------------------------------------

def get_output_file_name():
    output_file_name = input("Please Enter Output File Name: ")

    while not(any(c.isalpha() for c in output_file_name)):
        print("File name must contain at least one letter. Please enter a valid file name!")
        output_file_name = input("Please Enter Output File Name: ")

    return output_file_name

#-----------------------------------------------------   

def prase_header_file(head_file_path):
    function_pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*\s+\**[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\)\s*;') # This experssion is designed to match C/C++ function prototypes.
    with open(head_file_path,'r') as file:
        file_content = file.readlines()

    functions = []
    for line in file_content:
        match = function_pattern.match(line.strip())
        if match:
            functions.append(match.group(0))

    return functions

#-------------------------------------------

def write_to_excel(output_file_name, functions):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Function Prototypes"

    ws.append(["Function Prototype", "ID"])
    for idx, function in enumerate(functions):
        ws.append([function,f"IDX{idx}"])

    wb.save(output_file_name + '.xlsx')


user_choice = input("Welcome to Header Parser for C/C++ Header Files\nEnter '1' to continue or '0' to exit: ")

while user_choice not in ['1', '0']:
    print("Invalid input. Please enter '1' to continue or '0' to exit!")
    user_choice = input("Welcome to Header Parser for C/C++ Header Files\nEnter '1' to continue or '0' to exit: ")
   
if user_choice == '1':
    print("Continuing with the Header Parser...")
    head_file_path = get_header_file_path() #/usr/include/math.h
    output_file_name = get_output_file_name()
    functions = prase_header_file(head_file_path)
    write_to_excel(output_file_name,functions)
    print(f"Excel File Gereration is complete. Thank you for your patience. Goodbye!")
   
else:
    print("Exiting. Goodbye!")
