import datetime

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.datetime.now()
    # Print the current date and time in "YYYY-MM-DD HH:MM:SS" format
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    # Ask the user for the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date
    current_date = datetime.datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + datetime.timedelta(days=days_to_add)
    
    # Print the future date in "YYYY-MM-DD" format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Run the functions
display_current_datetime()
calculate_future_date()
