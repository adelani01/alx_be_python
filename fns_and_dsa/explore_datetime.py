from datetime import date , timedelta

def display_current_datetime():
    current_date = date.today()
    print(current_date)
    return current_date


def calculate_future_date():
    current_date = date.today()
    number_of_days = int(input("Enter the number of days to add to the current date:"))
    future_date = display_current_datetime() + timedelta(days=number_of_days)
    return future_date

calculate_future_date()