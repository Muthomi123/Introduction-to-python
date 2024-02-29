from datetime import datetime

def main():
    # Get the current time
    current_time = datetime.now().strftime("%H:%M")

    # Convert the current time to hours
    current_time_in_hours = convert(current_time)

    # Check if it's breakfast, lunch, or dinner time
    if 7.0 <= current_time_in_hours <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= current_time_in_hours <= 13.0:
        print("It's lunch time!")
    elif 19.0 <= current_time_in_hours <= 22.0:
        print("It's dinner time!")

def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time.split(':'))

    # Convert hours and minutes to a floating-point representation
    return hours + minutes / 60.0

if __name__ == "__main__":
    main()