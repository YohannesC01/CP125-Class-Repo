import pandas as pd


def compare_averages(filename):
    data = pd.read_csv(filename)
    math_avg = float(round(data['Math'].mean(), 1))
    science_avg = float(round(data['Science'].mean(), 1))
    english_avg = float(round(data['English'].mean(), 1))


    averages = {
        "Math": math_avg,
        "Science": science_avg,
        "English": english_avg
    }

    
    best_subject = float(max(averages.values()))
    worst_subject = float(min(averages.values()))

    averages["best_subject"] = best_subject
    averages["worst_subject"] = worst_subject

    print(averages)
    return averages

result = compare_averages("labs/lab09/data/students.csv")