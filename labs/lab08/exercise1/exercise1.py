# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id score per line)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    # TODO: Implement this function
    passing_list = []
    score = open(input_file,'r')
    score_data = score.readlines()
    
    for row in score_data:
        if row >= str(80):
            passing_list.append(row)
        
    passing = open(output_file, "w")
    passing.write(passing_list)


# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")
