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
        print("Please select a function to run from the following list:\n")
        print("1 - Select Day\n2 - Calculate average speed")
        print("3 - Calculate total speeding\n0 - Exit program\n")

        selection = input("Enter your selection here:\n")
        if verify_selection(selection):
            print(f"You have selected program {selection}\n")

        if selection == "1":
            data_selection()
        elif selection == "2":
            average_speed()
        elif selection == "3":
            total_speeding()
        else:
            print("Exiting program")


def verify_selection(selection):
    """
    Verifies the function_select input to ensure the user selects an available
    program
    """
    try:
        choice = int(selection)
        if (choice > 3 or choice < 0):
            raise ValueError(
                f"Select a valid program 0-3. You entered {choice}"
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
    global DATA
    global operational_data
    data_choice = input("Select the day to analyse 1-7 (0 for all)\n")
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
    else:
        new_data = DATA
        operational_data = new_data
    print(operational_data)


def average_speed():
    """
    Calculates the average speed on the selected date
    """
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
    list_of_speeds = operational_data[1]
    list_of_speeds_without_title = list_of_speeds[1:]
    total_speeders = 0
    list_of_speeds_ints = [int(speed) for speed in list_of_speeds_without_title]
    for speed in list_of_speeds_ints:
        if speed > 80:
            total_speeders += 1
    print(f"The total number of cars over 80km/h were {total_speeders}\n")


def main():
    """
    Runs all program functions
    """
    function_select()


print("Welcome to Speed Survey Data Analysis\n")
main()
