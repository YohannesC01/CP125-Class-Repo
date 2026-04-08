import pandas as pd


def explore_data(filename):

    df = pd.read_csv(filename)

    total_students = df.shape
    subjects = ["Math", "Science", "English"]
    math_average = float(round(df["Math"].mean(), 1))
    highest_score = -1
    highest_math_student = ""

    for i in range(len(df)):
        if df.loc[i, "Math"] > highest_score:
            highest_score = df.loc[i, "Math"]
            highest_math_student = df.loc[i, "Name"]
    
    result = {}

    result["total_students"] = total_students[0]
    result["subjects"] = subjects
    result["math_average"] = math_average
    result["highest_math_student"] = highest_math_student

    return result

print(explore_data("labs/lab09/data/students.csv"))