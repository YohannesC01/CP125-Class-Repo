def manage_roster(enrolled, drop_requests, waitlist):
    """
    Processes student drop requests and adds from waitlist if needed.
    
    Args:
        enrolled: Set of currently enrolled student names
        drop_requests: List of student names requesting to drop
        waitlist: Set of students on the waitlist
    
    Returns:
        int: Count of final enrolled students
    """
    enrolled_set = set(enrolled)
    drop_requests_set = set(drop_requests)
    updated_enrolled = enrolled_set ^ drop_requests_set
    
    if len(updated_enrolled) < 5:
        for item in range(7-len(updated_enrolled)):
            if len(waitlist)==0:
                return len(updated_enrolled)
            else:
                random = waitlist.pop()
                updated_enrolled.add(random)
  
    return len(updated_enrolled)
    
    
