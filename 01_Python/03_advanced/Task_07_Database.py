import pandas as pd
import os
import openpyxl

file_path = ".\employees.xlsx"

def initialize_excel(file_path):
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["ID", "Name", "Job", "Salary"])
        df.to_excel(file_path, index=False,)
        print(f"Excel File {file_path} has been created!")

def add_employee(id, name, job, salary):
    df = pd.read_excel(file_path)
    new_employee = pd.DataFrame({"ID": [id], "Name": [name], "Job": [job], "Salary": [salary]})
    df = pd.concat([df, new_employee], ignore_index=True)
    df.to_excel(file_path, index=False)
    print(f"Employee {name} with ID {id} has been added")

def print_employee(id):
    df = pd.read_excel(file_path)
    employee = df[df['ID'] == id]
    if not employee.empty:
        employee = employee.iloc[0]
        print(f"ID {employee["ID"]} belongs to the Employee {employee["Name"]}, who works as {employee["Job"]} with salary {employee["Salary"]}")
    else:
        print("Employee not found.")

def remove_employee(id):
    df = pd.read_excel(file_path)
    if id in df["ID"].values:
        employee = df[df['ID'] == id]
        df.df[df["ID"]!= id]
        df.to_excel(file_path, index=False)
        print(f"Employee {employee["Name"]} with ID {id} has been removed")
    else:
        print("Employee not found.")

def update_employee(id, name=None, job=None, salary=None):
    df = pd.read_excel(file_path)
    if id in df['ID'].values:
        if name:
            df.loc[df['ID'] == id, 'Name'] = name
        if job:
            df.loc[df['ID'] == id, 'Job'] = job
        if salary:
            df.loc[df['ID'] == id, 'Salary'] = salary
        employee = df[df['ID'] == id]
        df.to_excel(file_path, index=False)
        print(f"Employee {employee["Name"]} with ID {id} has been removed")
    else:
        print("Employee not found.")

def main():
    initialize_excel(file_path)
    while True:
        print("\nEmployee Management System")
        print("1. Add New Employee")
        print("2. Print Employee Data")
        print("3. Remove Employee")
        print("4. Update Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            job = input("Enter Job: ")
            salary = float(input("Enter Salary: "))
            add_employee(id, name, job, salary)
        elif choice == '2':
            id = int(input("Enter ID: "))
            print_employee(id)
        elif choice == '3':
            id = int(input("Enter ID: "))
            remove_employee(id)
        elif choice == '4':
            id = int(input("Enter ID: "))
            name = input("Enter Name (or leave blank to keep current): ")
            job = input("Enter Job (or leave blank to keep current): ")
            salary = input("Enter Salary (or leave blank to keep current): ")

            name = name if name else None
            job = job if job else None
            salary = float(salary) if salary else None

            update_employee(id, name, job, salary)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main function
if __name__ == "__main__":
    main()
 