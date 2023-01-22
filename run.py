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

    if selection == 1:
        data_selection()
    elif selection == 2:
        pass
    elif selection == 3:
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
    selected_data = []



def main():
    """
    Runs all program functions
    """
    function_select()


print("Welcome to Speed Survey Data Analysis")
main()
