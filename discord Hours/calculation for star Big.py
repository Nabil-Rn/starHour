import re
import pandas as pd

# The Big text 
input_text = """
Feb 21th: Bryce: 2 hours

2L — 22/02/2024 14:20
Feb 22nd: Alam: 31 minutes 35 seconds

2L — 22/02/2024 18:15
Feb 22nd: Alam: 2 hours 24 minutes 39 seconds
23 February 2024

Burrito — 23/02/2024 17:02
Feb 23rd: Kevin: 3 hours
24 February 2024

Dolphin Duck — 24/02/2024 00:54
Feb 23rd: Nabil: 12:30 to 2pm : 1 hour 30 minutes
26 February 2024

Dolphin Duck — 26/02/2024 16:05
Feb 26rd: Nabil: 4 hours
27 February 2024

2L — 27/02/2024 11:44
Feb 27th: Alam: 1 hour 44 minutes 09 seconds

SweatyBeanz (co-prez) — 27/02/2024 13:56
Feb 27: Anmol: 58 mins 07 seconds

2L — 27/02/2024 13:58
Feb 27th: Alam: 21 minutes 38 seconds

Dolphin Duck — 27/02/2024 15:59
Feb 27rd: Nabil: 3 hours

magicage — 27/02/2024 16:29
Feb 27th:Bryce;3 hours

SweatyBeanz (co-prez) — 27/02/2024 16:31
Feb 27th: 1 hour 48 mins

Burrito — 27/02/2024 20:59
Feb 27th: 2 hours 30 minutes
29 February 2024

Dolphin Duck — 29/02/2024 11:32
Feb 29rd: Nabil: 1 hour and 30 minutes

SweatyBeanz (co-prez) — 29/02/2024 13:58
Feb 29th: Anmol: 1 hour

2L — 29/02/2024 14:14
Feb 29th: Alam: 1 hour 1 minutes 46 seconds

2L — 29/02/2024 18:03
Feb 29th: Alam: 2 hours 20 minutes 16 seconds
18 March 2024

Dolphin Duck — 18/03/2024 13:57
March 18: Nabil:  1 hour: hosting the club: 12:15 -> 1:15 (edited)

Dolphin Duck — 18/03/2024 14:15
March 18: Nabil:  1 hour: club meeting: 1:15 -> 2:15

SweatyBeanz (co-prez) — 18/03/2024 14:25
March 18: Anmol: 1 hour
19 March 2024

Dolphin Duck — 19/03/2024 03:47
March 19: Nabil:  2 hour: poster: 1:45 -> 3:45
20 March 2024

SweatyBeanz (co-prez) — 20/03/2024 11:23
March 19: Anmol: 6 hours for geek con

2L — 20/03/2024 11:24
March 19: Alam: 5 hours 30 minutes (geek-con)

Dolphin Duck — 20/03/2024 15:00
March 19: Nabil: 3 hours: geek-con (edited)

@Dolphin Duck
March 19: Nabil: 3 hours: geek-con (edited)

SweatyBeanz (co-prez) — 20/03/2024 15:41
Why are you writing for alam lmao

Dolphin Duck — 20/03/2024 15:42
I’m lazy I copied and edited the hours forgot to edit the name (edited)

Burrito — 20/03/2024 17:27
March 19: Kevin: 2 hours 45 mins
21 March 2024

2L — 21/03/2024 16:52
March 21: Alam: 6 hours

SweatyBeanz (co-prez) — 21/03/2024 17:03
March 21: Anmol: 2 hours

Burrito — 21/03/2024 17:17
March 21: Kevin: 30 minutes

Dolphin Duck — 21/03/2024 19:30
March 21: Nabil: 1 hours
22 March 2024

magicage — 22/03/2024 22:39
March 19: 12:45-4:00

SweatyBeanz (co-prez) — 22/03/2024 22:45
March 22: Anmol: 1 hour
25 March 2024

magicage — 25/03/2024 17:16
March 25: bryce: 4:15-5:15
27 March 2024

2L — 27/03/2024 16:16
March 26: Alam: 2 hours

SweatyBeanz (co-prez) — 27/03/2024 16:40
March 27: Anmol: 1 hour

2L — 27/03/2024 16:42
March 27: Alam: 30 minutes

Burrito — 27/03/2024 19:18
March 27: Kevin: 1 hour
28 March 2024

magicage — 28/03/2024 17:30
March 28: bryce:4:30-5:30
29 March 2024

2L — 29/03/2024 16:08
March 28: Alam: 1h30
5 April 2024

Dolphin Duck — 05/04/2024 12:22
April 4: Nabil: 30 minutes
10 April 2024

magicage — 10/04/2024 13:25
April 10: bryce: 2 hours

SweatyBeanz (co-prez) — 10/04/2024 13:30
April 10: Anmol: 1 hour 30 minutes

Burrito — 10/04/2024 13:39
April 10: Kevin: 2 hours
11 April 2024

Dolphin Duck — 11/04/2024 00:03
April 10: Nabil: 1 hour

2L — 11/04/2024 17:42
April 11: Alam: 1 hour 10 minutes
12 April 2024

magicage — 12/04/2024 12:09
April 12: bryce:1 bour and 20 minutes
15 April 2024

magicage — 15/04/2024 16:30
April 15: bryce:50 minutes
17 April 2024

Dolphin Duck — 17/04/2024 12:49
April 17: Nabil :30 minutes
18 April 2024

2L — 18/04/2024 17:53
April 18: Alam: 2 hours 30 minutes

Dolphin Duck — 18/04/2024 17:59
April 18: Nabil : 1 hour
19 April 2024

Dolphin Duck — 19/04/2024 14:02
April 19: Nabil : 1 hour
23 April 2024

Dolphin Duck — 23/04/2024 14:11
April 23: Nabil : 1 hour
29 April 2024

Dolphin Duck — 29/04/2024 12:46
April 29: Nabil : 1 hour
2 May 2024

Dolphin Duck — 02/05/2024 10:14
April 30: Nabil : 1 hour 30 minutes
3 May 2024

Dolphin Duck — 03/05/2024 15:00
May 3: Nabil : 2 hour 30 minutes

Burrito — 03/05/2024 17:29
May 3: Kevin: 2 hours

2L — 03/05/2024 18:29
May 3: Alam: 15 minutes
8 May 2024

Burrito — 08/05/2024 16:32
May 8:  Kevin: 6 hours 30 minutes

Dolphin Duck — 08/05/2024 18:34
May 8:  Nabil: 1 hour 30 minutes

2L — 08/05/2024 22:59
May 8: Alam: 1 hour 30 minutes
10 May 2024

Dolphin Duck — 10/05/2024 12:19
May 9: Nabil: 1 hour 15 minutes

Dolphin Duck — 10/05/2024 13:23
May 10: Nabil: 1 hour (edited)

Burrito — 10/05/2024 21:31
May 10: Kevin: 4 hours
11 May 2024

Dolphin Duck — 11/05/2024 13:14
May 10: Nabil: 4 hours

2L — 11/05/2024 14:50
May 10: Alam: 4 hours
22 May 2024

Dolphin Duck — Today at 20:21
May 14: Nabil: 1 hours
[20:23]
May 17: Nabil: 1 hours
[20:23]
May 17: Nabil: 2 hours
"""

# Split the text into individual lines because of lazy copy of discord chat
lines = input_text.strip().split("\n")

# idk Regular expression so i copied it outside to extract volunteer time information
time_pattern = re.compile(r'(\d+)\s*(hours?|h)|(\d+)\s*(minutes?|m)|(\d+)\s*(seconds?|s)', re.IGNORECASE)

def time_to_minutes(time_str):
    matches = time_pattern.findall(time_str)
    total_minutes = 0

    for match in matches:
        if match[0]:
            total_minutes += int(match[0]) * 60  
        if match[2]:
            total_minutes += int(match[2]) 
        if match[4]:
            total_minutes += int(match[4]) / 60  

    return total_minutes

user_volunteer_hours = {}

# Loop through the lines and extract user : time
for line in lines:
    if ":" not in line:
        continue  # Ignore lines without colon (not containing volunteer info)

    # Split the line to get the date, user, and time part
    parts = line.split(":", maxsplit=3)  # Split into at least 3 parts
    if len(parts) < 3:
        continue  # Ignore lines with incomplete info

    # Extract the user and time information
    user = parts[1].strip()  # Get the username
    time_str = parts[2].strip()  # Get the time part!!!

    # Convert time to total minutes
    total_minutes = time_to_minutes(time_str)

    # Accumulate volunteer hours for each user
    if user not in user_volunteer_hours:
        user_volunteer_hours[user] = 0
    user_volunteer_hours[user] += total_minutes

# Convert the total volunteer time for each user to hours
results = {user: user_volunteer_hours[user] / 60 for user in user_volunteer_hours}

# Convert to pandas DataFrame for a cleaner output
df = pd.DataFrame(list(results.items()), columns=["User", "Total Hours"])
print(df)
