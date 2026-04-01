import pandas as pd
import matplotlib.pyplot as plt


def show_science_distribution(filename):
    data = pd.read_csv(filename)

    science_scores = data['Science']

    plt.hist(science_scores, bins=10)

    plt.xlabel("Science Score")
    plt.ylabel("Frequency")
    plt.title("Science Score Distribution")

    plt.show()

    return len(data)

result = show_science_distribution("labs/lab09/data/students.csv")
