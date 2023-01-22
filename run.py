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

survey_data = SHEET.worksheet('survey_data')

data = survey_data.get_all_values()
operational_data = data


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
            print(f"You have selected program {selection}")
            break

    if selection == "1":
        data_selection()
    elif selection == "2":
        pass
    elif selection == "3":
        pass
    else:
        pass


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
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def data_selection():
    global data
    global operational_data
    data_choice = input("Select the day to analyse 1-7 (0 for all)\n")
    if data_choice == "1":
        new_data = operational_data[0:2]
        print(new_data)
    elif data_choice == "2":
        new_data = operational_data[2:4]
        print(new_data)
    elif data_choice == "3":
        new_data = operational_data[4:6]
        print(new_data)
    elif data_choice == "4":
        new_data = operational_data[6:8]
        print(new_data)
    elif data_choice == "5":
        new_data = operational_data[8:10]
        print(new_data)
    elif data_choice == "6":
        new_data = operational_data[10:12]
        print(new_data)
    elif data_choice == "7":
        new_data = operational_data[12:14]
        print(new_data)
    else:
        new_data = data
        print(new_data)


def main():
    """
    Runs all program functions
    """
    function_select()


print("Welcome to Speed Survey Data Analysis\n")
main()