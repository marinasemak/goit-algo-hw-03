from datetime import datetime


# Convert input string date to datetime object
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")

# Calculates diff between current date and date from input
def get_days_from_today(date):
    try:
        date = string_to_date(date_string)
        today = datetime.today()
        days_diff = today.toordinal() - date.toordinal()
    except ValueError:
        print(f"{date_string} date has wrong format")
        return None
    return days_diff

# Asks user to enter date and prints difference
date_string = input("Enter date in the format: 'YYYY-MM-DD': ")
result = get_days_from_today(date_string)
if result:
    print(f"There are {result} dates from {date_string} till today")



