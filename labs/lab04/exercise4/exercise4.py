
def analyze_performance(lap_times):
  firstlap=[]
  secondlap=[]
  for i in range (0,(len(lap_times)-1)):
    if len(lap_times)%2 == 0:
        if i+1 <= len(lap_times) // 2 == 0:
            firstlap.append(lap_times[i])
        else:
            i+1 <= len(lap_times) // 2 == 0 
            secondlap.append(lap_times[i])
    else:
        if i+1 <= (len(lap_times) // 2)+1:
            firstlap.append(lap_times[i])
        else:
            i+1 <= (len(lap_times) // 2) 
            secondlap.append(lap_times[i])
        

average_firstlap = sum(firstlap)/len(firstlap)



# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
