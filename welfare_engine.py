def Check_Eligibility(Citizen):
    Scheme = []

    Age = Citizen["Age"]
    Income = Citizen["Income"]
    Disability = Citizen["Disability"]
    Student = Citizen["Student"]

    if Age >= 60:
        Scheme.append("Senior Citizen Support")

    if Disability == "yes":
        Scheme.append("Disability Support")

    if Income <= 300000:
        Scheme.append("Low Income Support")

    if Student == "yes":
        Scheme.append("Education Support")

    return Scheme