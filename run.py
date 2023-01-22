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
    print("Please select a function to run from the following list:\n")
    print("1 - Select Day\n2 - Calculate average speed")
    print("3 - Calculate total speeding")


function_select()
