import pandas as pd
import matplotlib.pyplot as plt

def show_math_trend(filename):
    
    data = pd.read_csv(filename)

    math_scores = data['Math']

    plt.plot(data.index, math_scores)

    plt.xlabel("Student Index")
    plt.ylabel("Math Score")
    plt.title("Math Score Trends")

    plt.show()

    return len(data)

result = show_math_trend("labs/lab09/data/students.csv")