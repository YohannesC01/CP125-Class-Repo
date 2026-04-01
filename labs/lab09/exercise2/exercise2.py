import pandas as pd


def compare_averages(filename):
    data = pd.read_csv(filename)
    math_avg = round(data['Math'].mean(), 1)
    science_avg = round(data['Science'].mean(), 1)
    english_avg = round(data['English'].mean(), 1)

    averages = {
        "Math": math_avg,
        "Science": science_avg,
        "English": english_avg
    }

    
    best_subject = max(averages)
    worst_subject = min(averages)

    averages["best_subject"] = best_subject
    averages["worst_subject"] = worst_subject

    print(averages)
    return averages

result = compare_averages("labs/lab09/data/students.csv")