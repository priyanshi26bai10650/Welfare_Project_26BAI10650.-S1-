from validator import Check_Name, Check_Age, Check_Income, Check_yes_no
from storage import Add_Citizen, Get_Citizens
from welfare_engine import Check_Eligibility
from reports import Show_Report

def Add_New_Citizen():
    print("\n Add Citizen ")

    Name = input("Enter Name: ").strip()

    if not Check_Name(Name):
        print("Incorrect Name.")
        return
    try:
        Age = int(input("Enter Age: "))
        Income = float(input("Enter Yearly Income: "))
    except ValueError:
        print("Please enter numbers for age and income.")
        return
    if not Check_Age(Age):
        print("Incorrect Age.")
        return
    if not Check_Income(Income):
        print("Incorrect Income.")
        return

    Disability = input("Has Disability? (yes/no): ").lower()
    if not Check_yes_no(Disability):
        print("Enter yes or no.")
        return

    Student = input("Is the person a Student? (yes/no): ").lower()
    if not Check_yes_no(Student):
        print("Enter yes or no.")
        return

    Citizen = {"Name": Name, "Age": Age, "Income": Income, "Disability": Disability, "Student": Student}

    Add_Citizen(Citizen)
    print("Citizen added successfully.")


def Check_Citizen_Schemes():
    Data = Get_Citizens()
    if len(Data) == 0:
        print("\n No citizen records found.")
        return
    print("\n Citizen List ")

    for i, Citizen in enumerate(Data):
        print(i + 1, "-", Citizen["Name"])
    try:
        Choice = int(input("Select citizen number: "))
    except ValueError:
        print("Incorrect Choice.")
        return

    if Choice < 1 or Choice > len(Data):
        print("Incorrect Citizen Number.")
        return

    Citizen = Data[Choice - 1]
    Scheme = Check_Eligibility(Citizen)
    print("\n Citizen:", Citizen["Name"])

    if len(Scheme) == 0:
        print("Matching schemes NOT found.")
    else:
        print("Possible eligible schemes:")

        for Scheme in Scheme:
            print("-", Scheme)


def Show_All_Citizens():
    Data = Get_Citizens()

    if len(Data) == 0:
        print("\n No citizen records found.")
        return
    print("\n All Citizens ")

    for Citizen in Data:
        print("Name:", Citizen["Name"])
        print("Age:", Citizen["Age"])
        print("Income:", Citizen["Income"])
        print("Disability:", Citizen["Disability"])
        print("Student:", Citizen["Student"])


def main():
    while True:
        print(" Welfare Scheme Management ")
        print("1. Add citizen")
        print("2. Check welfare schemes")
        print("3. Show all citizens")
        print("4. Show report")
        print("5. Exit")

        Choice = input("Enter Choice: ")

        if Choice == "1":
            Add_New_Citizen()

        elif Choice == "2":
            Check_Citizen_Schemes()

        elif Choice == "3":
            Show_All_Citizens()

        elif Choice == "4":
            Data = Get_Citizens()
            Show_Report(Data)
    
        else:
            print("Incorrect Choice.")
            
if __name__ == "__main__":
    main()