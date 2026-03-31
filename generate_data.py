import pandas as pd
import random

data = []
hours = [2,3,4,5,6]
backlog = ['low','medium','high']
difficulty = ['easy','medium','hard']
mood = ['tired','normal','energetic']
for _ in range(150):  
    h = random.choice(hours)
    b = random.choice(backlog)
    d = random.choice(difficulty)
    m = random.choice(mood)   
    if b == 'high' and d == 'hard':
        subject = 'Physics'
    elif b == 'medium' and d in ['medium','hard']:
        subject = 'Chemistry'
    elif b == 'low' and d == 'easy':
        subject = 'Math'
    elif m == 'tired':
        subject = 'Math'
    elif m == 'energetic' and d == 'hard':
        subject = 'Physics'
    else:
        subject = 'Chemistry'

    data.append([h, b, d, m, subject])
df = pd.DataFrame(data, columns=["hours_available","backlog_level","subject_difficulty","mood","priority_subject"])
df.to_csv("data.csv", index=False)
print("Dataset created successfully!")