import pandas as pd


def explore_data(filename):
    data = pd.read_csv(filename)
    math_avg = data["Math"].mean()
    total_students = len(data)
    highest_math = data["Math"].max()
    subject = ["Math,Science,English"]

    result = pd.DataFrame({
    'Total Students': total_students,
    'Subjects' : subject,
    'Math Average ': math_avg,
    'Math Highest Mark': highest_math
})
    
    print(result)
    return result

result = explore_data("labs/lab09/data/students.csv")
