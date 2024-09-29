import datetime
def display_current_datetime():
    time = datetime.date.today()
    print(f"Current date and time {time}")


display_current_datetime()

def calculate_future_date(days):
    time = datetime.date.today()
    
    future_date = time + datetime.timedelta(days=days)
    
    return future_date.strftime("%Y-%m-%d")

days_input = int(input("Enter the number of days to add: "))

future_date = calculate_future_date(days_input)
print(f"The future date after {days_input} days will be: {future_date}")
