import re
import pandas as pd

# Sample data
messages = [
    "April 23: Nabil : 1 hour",
    "April 18: Alam: 2 hours 30 minutes",
    "April 15: bryce:50 minutes",
    "April 10: Anmol: 1 hour 30 minutes",
]

# Regular expression to extract time components
time_pattern = re.compile(r'(\d+)\s*(hours?|h)|(\d+)\s*(minutes?|m)|(\d+)\s*(seconds?|s)', re.IGNORECASE)

# Function to convert extracted components to total minutes
def time_to_minutes(time_str):
    matches = time_pattern.findall(time_str)
    total_minutes = 0

    for match in matches:
        if match[0]:
            total_minutes += int(match[0]) * 60  # Convert hours to minutes
        if match[2]:
            total_minutes += int(match[2])  # Add minutes
        if match[4]:
            total_minutes += int(match[4]) / 60  # Convert seconds to minutes

    return total_minutes

# Dictionary to store user time in minutes
user_time = {}

for msg in messages:
    # Split the message to get the user and time part
    parts = msg.split(":")
    user = parts[1].strip()  # Get the username
    time_str = parts[2].strip()  # Get the time part

    # Convert time to minutes
    total_minutes = time_to_minutes(time_str)

    # Accumulate time for each user
    if user not in user_time:
        user_time[user] = 0
    user_time[user] += total_minutes

# Output results
results = {user: user_time[user] / 60 for user in user_time}  # Convert back to hours

# Convert to pandas DataFrame for a cleaner output
df = pd.DataFrame(list(results.items()), columns=["User", "Total Hours"])
print(df)
