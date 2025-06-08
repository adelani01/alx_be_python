#dateime module
from datetime import date, datetime, timedelta


# defining current date
def display_current_datetime():
    current_date = datetime.now()
    formatted_date= current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted_date)
    return formatted_date

# calculating future date
def calculate_future_date():
    today = date.today()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = today + timedelta(days=number_of_days)
    print("Future date: ",future_date)
    return future_date


display_current_datetime()
calculate_future_date()