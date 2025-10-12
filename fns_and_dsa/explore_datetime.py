from datetime import datetime,timedelta


def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    enter_future_date = int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days=enter_future_date)

    print("Future date:",future_date + datetime.now().date())

display_current_datetime()
calculate_future_date()
