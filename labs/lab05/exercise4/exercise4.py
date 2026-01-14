def filter_query_times(query_times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
    if not query_times:
        return[]
        
    mean =  sum(query_times) / len(query_times)

    for i in range (len(query_times)):
        sum = 0 
        varience = sum(i-mean)**2 / len(query_times)
        sum+=varience

    std_dev = (varience)**0.5

    upper_limit = mean + std_dev

    
    for i in query_times[:]:
        if i > upper_limit:
            query_times.remove(i)
            
    return query_times 

# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
