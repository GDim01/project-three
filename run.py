import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('speed_survey')
SURVEY_DATA = SHEET.worksheet('survey_data')
DATA = SURVEY_DATA.get_all_values()

operational_data = DATA


def function_select():
    """
    Allows the user to choose which function of the program they wish to use.
    """
    while True:
        print("\nPlease select a function to run from the following list:\n")
        print("1 - Select Day\n2 - Calculate average speed")
        print("3 - Calculate total speeding\n4 - Show no. cars each hour")
        print("0 - Exit program\n")

        selection = input("Enter your selection here:\n")
        if verify_selection(selection):
            print(f"You have selected program {selection}\n")

        if selection == "1":
            data_selection()
        elif selection == "2":
            average_speed()
        elif selection == "3":
            total_speeding()
        elif selection == "4":
            hourly_count()
        elif selection == "0":
            print("Exiting program")
            break
        else:
            print("Please select a program from the above list")


def verify_selection(selection):
    """
    Verifies the function_select input to ensure the user selects an available
    program
    """
    try:
        choice = int(selection)
        if (choice > 8 or choice < 0):
            raise ValueError(
                f"Select a valid program. You entered {choice}"
            )
    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False

    return True


def data_selection():
    """
    Selects the relevant data chosen by the user and updates the
    operational_data variable for use in other functions
    """
    global operational_data
    data_choice = input("Select the day to analyse 1-7\n")
    if verify_selection(data_choice):
        print(f"You have selected day {data_choice}\n")
    if data_choice == "1":
        new_data = operational_data[0:2]
        operational_data = new_data
    elif data_choice == "2":
        new_data = operational_data[2:4]
        operational_data = new_data
    elif data_choice == "3":
        new_data = operational_data[4:6]
        operational_data = new_data
    elif data_choice == "4":
        new_data = operational_data[6:8]
        operational_data = new_data
    elif data_choice == "5":
        new_data = operational_data[8:10]
        operational_data = new_data
    elif data_choice == "6":
        new_data = operational_data[10:12]
        operational_data = new_data
    elif data_choice == "7":
        new_data = operational_data[12:14]
        operational_data = new_data
    print(operational_data)


def average_speed():
    """
    Calculates the average speed on the selected date
    """
    global operational_data
    list_of_speeds = operational_data[1]
    list_of_speeds_without_title = list_of_speeds[1:]
    total_speed = 0
    list_of_speeds_ints = [int(speed) for speed in list_of_speeds_without_title]
    for speed in list_of_speeds_ints:
        total_speed += speed
    result = total_speed / len(list_of_speeds_ints)
    print(f"The average speed during the selected date was {result}\n")


def total_speeding():
    """
    Calculates the number of cars driving over 80km/h on the selected date
    """
    global operational_data
    list_of_speeds = operational_data[1]
    list_of_speeds_without_title = list_of_speeds[1:]
    total_speeders = 0
    list_of_speeds_ints = [int(speed) for speed in list_of_speeds_without_title]
    for speed in list_of_speeds_ints:
        if speed > 80:
            total_speeders += 1
    print(f"The total number of cars over 80km/h were {total_speeders}\n")


def hourly_count():
    """
    Counts the number of cars at each hour of the selected date
    """
    global operational_data
    list_of_times = operational_data[0]
    list_of_times_without_title = list_of_times[1:]
    hours_list = []
    hourly_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for hour in list_of_times_without_title:
        hours_list.append(hour[0:2])
    for hour in hours_list:
        if hour == "00":
            hourly_counts[0] += 1
        elif hour == "01":
            hourly_counts[1] += 1
        elif hour == "02":
            hourly_counts[2] += 1
        elif hour == "03":
            hourly_counts[3] += 1
        elif hour == "04":
            hourly_counts[4] += 1
        elif hour == "05":
            hourly_counts[5] += 1
        elif hour == "06":
            hourly_counts[6] += 1
        elif hour == "07":
            hourly_counts[7] += 1
        elif hour == "08":
            hourly_counts[8] += 1
        elif hour == "09":
            hourly_counts[9] += 1
        elif hour == "10":
            hourly_counts[10] += 1
        elif hour == "11":
            hourly_counts[11] += 1
        elif hour == "12":
            hourly_counts[12] += 1
        elif hour == "13":
            hourly_counts[13] += 1
        elif hour == "14":
            hourly_counts[14] += 1
        elif hour == "15":
            hourly_counts[15] += 1
        elif hour == "16":
            hourly_counts[16] += 1
        elif hour == "17":
            hourly_counts[17] += 1
        elif hour == "18":
            hourly_counts[18] += 1
        elif hour == "19":
            hourly_counts[19] += 1
        elif hour == "20":
            hourly_counts[20] += 1
        elif hour == "21":
            hourly_counts[21] += 1
        elif hour == "22":
            hourly_counts[22] += 1
        elif hour == "23":
            hourly_counts[23] += 1
    print(f"The number of cars for each hour, starting at '00' is {hourly_counts}")


def main():
    """
    Runs all program functions
    """
    data_selection()
    function_select()


print("Welcome to Speed Survey Data Analysis\n")
main()
