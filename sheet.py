from __future__ import print_function
import time
import pickle
import os.path
from fetch_data import *
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1YgC2R2BWrdFY2I5SvboHOffFJTJiBRuHnf1lWslmnh4'
#test

def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    while True:
        try:
            data = create_tuples()[:6]
            del data[3]

            values = [[d[1], yesterday_price(d[0]+'USDT')] for d in data]
            body = {
                'values': values
            }
            result = service.spreadsheets().values().update(
                spreadsheetId=SPREADSHEET_ID, range='B2:C7',
                valueInputOption='USER_ENTERED', body=body).execute()
            time.sleep(1)
            print ('k')
        except Exception as e: 
            print(e)



    # result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
    #                             range=RANGE_NAME).execute()
    # values = result.get('values', [])

    # if not values:
    #     print('No data found.')
    # else:
    #     for row in values:
    #         print (row)

if __name__ == '__main__':
    main()



