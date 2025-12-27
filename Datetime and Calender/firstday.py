from datetime import date
import datetime

# Get today's date
today = date.today() 
# today = date(2025, 12, 27) # Example specific date

# Get the first day of the current month
first_day_of_month = today.replace(day=1)

print(f"Today's date: {today}")
print(f"First day of the month: {first_day_of_month}")