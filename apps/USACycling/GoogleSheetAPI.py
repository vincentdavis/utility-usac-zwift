import os

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GSheetAPI():
    def __init__(self) -> None:
        self.creds = None

        self.scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file",
                  "https://www.googleapis.com/auth/spreadsheets"]
        if os.path.exists('get-permission-2d1be-4fbe8b484e2c.json'):
            self.creds = service_account.Credentials.from_service_account_file('get-permission-2d1be-4fbe8b484e2c.json',
                                                                          scopes=self.scopes)
        # Sheet ID
        self.SPREADSHEET_ID = '1EbC7zxPxZ8c46lOpMHc5omb5Biu4XAi7aXSN59xmJl0'
        super().__init__()

    def get_values(self, spreadsheet_id, range_name):
        """
        Creates the batch_update the user has access to.
        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
            """
        # pylint: disable=maybe-no-member
        try:
            service = build('sheets', 'v4', credentials=self.creds)

            result = service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id, range=range_name).execute()
            rows = result.get('values', [])
            print(f"{len(rows)} rows retrieved")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error


    def update_values(self, spreadsheet_id, range_name, value_input_option, _value):
        """
        Creates the batch_update the user has access to.
        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
            """
        # pylint: disable=maybe-no-member
        try:

            service = build('sheets', 'v4', credentials=self.creds)
            values =_value

            data = {
                'values': values
            }
            service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, body=data, range=range_name,
                                                   valueInputOption='USER_ENTERED').execute()

            return "rsult"
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

if __name__ == '__main__':
    gs = GSheetAPI()
    # gs.get_values(gs.SPREADSHEET_ID, "A1:C2")
    gs.update_values(gs.SPREADSHEET_ID, 'Profile!A1:D2', "USER_ENTERED",
                     [
                         ['a1', 'b1', 'c1', 123],
                     ]
                     )