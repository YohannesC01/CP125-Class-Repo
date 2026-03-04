# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    # TODO: Implement this function
    file1 = open(file1,'r')
    file1_set = set(file1.readlines())

    file2 = open(file2,'r')
    file2_set = set(file2.readlines())

    merged = file1_set | file2_set
    merged_list = list(merged)
    merged_list = sorted(merged_list)

    merge = open(output_file, "w")
    merge.writelines(merged_list)
    
    result = len(merged)
    

    file1.close()
    file2.close()
    merge.close()
    
    return result
# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
