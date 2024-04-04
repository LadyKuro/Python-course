import datetime

def print_working_days(date1, date2):
    """Print the number of working days between date1 and date2."""
    d1 = datetime.date.fromisoformat(date1)
    d2 = datetime.date.fromisoformat(date2)
    working_days = 0
    days = (d2 - d1).days
    weeks = days // 7
    remaining_days = days % 7
    if remaining_days > 5:
        remaining_days -= 1
    working_days = weeks * 5 + remaining_days
    print(working_days)

print_working_days("2024-01-01", "2024-04-04")