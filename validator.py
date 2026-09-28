def Check_Name(Name):
    if Name.strip() == "":
        return False
    return True

def Check_Age(Age):
    if Age < 0 or Age > 120:
        return False
    return True

def Check_Income(Income):
    if Income < 0:
        return False
    return True

def Check_yes_no(Value):
    Value = Value.lower()

    if Value == "yes" or Value == "no":
        return True
    return False
