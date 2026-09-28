from validator import Check_Name, Check_Age, Check_Income, Check_yes_no
from welfare_engine import Check_Eligibility

def Test_Name():
    assert Check_Name("Rahul") == True
    assert Check_Name("") == False

def Test_Age():
    assert Check_Age(20) == True
    assert Check_Age(-5) == False

def Test_Income():
    assert Check_Income(200000) == True
    assert Check_Income(-100) == False

def Test_yes_no():
    assert Check_yes_no("yes") == True
    assert Check_yes_no("no") == True

def Test_Welfare():
    Citizen = {"Name": "Test", "Age": 65, "Income": 200000, "Disability": "yes", "Student": "no"}

    result = Check_Eligibility(Citizen)
    assert "Senior Citizen Support" in result
    assert "Low Income Support" in result

Test_Name()
Test_Age()
Test_Income()
Test_yes_no()
Test_Welfare()
print("All tests passed.")