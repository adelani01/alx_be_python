#dateime module
from datetime import date, datetime, timedelta




# defining current date and time
def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", current_date)
    return current_date

# calculating future date
def calculate_future_date():
    date_today = date.today() 
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = date_today + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date: ",formatted_future_date)
    return formatted_future_date

# Run the function
display_current_datetime()
calculate_future_date()