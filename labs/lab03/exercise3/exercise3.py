def has_adjacent_seats(seats):
    for i in range(0,len(seats)-1):
        if seats[i+1] == 0 and seats[i-1] == 0:
            return True
        else: 
            return False
