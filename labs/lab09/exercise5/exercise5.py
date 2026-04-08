import pandas as pd

def high_performers(filename):
    data = pd.read_csv(filename)

    high_performers_student = data.loc[
        (data['Math'] > 85) &
        (data['Science'] > 85) &
        (data['English'] > 85) &
        (data['Physics'] > 85) &
        (data['Chemistry'] > 85),
        'Name'
    ]

    names_set = set(high_performers_student) 

    result = {
        "count": len(names_set),
        "names": names_set
    }
    
    return result