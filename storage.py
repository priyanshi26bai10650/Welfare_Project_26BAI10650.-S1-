import json
import os
FILE_NAME = "data/citizens.json"
def Load_Data():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def Save_Data(Data):
    with open(FILE_NAME, "w") as file:
        json.dump(Data, file, indent=4)

def Add_Citizen(Citizen):
    Data = Load_Data()
    Data.append(Citizen)
    Save_Data(Data)

def Get_Citizens():
    return Load_Data()