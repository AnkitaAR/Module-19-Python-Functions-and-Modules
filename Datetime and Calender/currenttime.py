from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the time into a readable string (HH:MM:SS)
current_time = now.strftime("%H:%M:%S")

print("Current Time =", current_time)