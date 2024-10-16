from datetime import datetime, timedelta

def display_current_datetime():
    time = datetime.now()
    print(f"Current date and time: {time}")


display_current_datetime()

def calculate_future_date(days):
    time = datetime.now()
    
    future_date = time + timedelta(days=days)
    
    return future_date.strftime("%Y-%m-%d %H:%M:%S")

days_input = int(input("Enter the number of days to add to the current date: "))

future_date = calculate_future_date(days_input)
print(f"The future date after {days_input} days will be: {future_date}")
