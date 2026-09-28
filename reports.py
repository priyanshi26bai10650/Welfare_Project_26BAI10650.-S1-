def Show_Report(Data):
    print("\n Welfare Report ")
    print("Total Citizens:", len(Data))

    Senior = 0
    Disabled = 0
    Students = 0
    Low_income = 0

    for Citizen in Data:
        if Citizen["Age"] >= 60:
            Senior += 1
        if Citizen["Disability"] == "yes":
            Disabled += 1
        if Citizen["Student"] == "yes":
            Students += 1
        if Citizen["Income"] <= 300000:
            Low_income += 1

    print("Senior Citizens:", Senior)
    print("Disabled Citizens:", Disabled)
    print("Students:", Students)
    print("Low income citizens:", Low_income)