from apiclient import *
from oauth2client import *
from oauth2client import *
from oauth2client.file import *
import datetime
import argparse
import httplib2
import os

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Smart Mirror'

def get_credentials(): #Kalender
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
                Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
                os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                                                   'calendar-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
                flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
                flow.user_agent = APPLICATION_NAME
                if flags:
                        credentials = tools.run_flow(flow, store, flags)
                else: # Needed only for compatibility with Python 2.6
                        credentials = tools.run(flow, store)
                print('Storing credentials to ' + credential_path)
        return credentials

credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('calendar', 'v3', http=http)

now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
eventsResult = service.events().list(
    calendarId='primary', timeMin=now, maxResults=4, singleEvents=True,
    orderBy='startTime').execute()
events = eventsResult.get('items', [])
text=""
for event in events:
    if(str(event['start'].get('dateTime')) == "None"):
        text = str(text) + " " + event['summary'] + "\n"
    else:
        datum = event['start'].get('dateTime').split("-")[2].split("T")[0] + "." + event['start'].get('dateTime').split("-")[1] + "." + event['start'].get('dateTime').split("-")[0] + " " + event['start'].get('dateTime').split("T")[1].split(":00+")[0]
        text = str(text) + " " +  datum + " " + event['summary'] + "\n"

with open("RAM/Kalender.txt", "w") as out:
    out.write(text)
    os.system("touch RAM/refresh")
    out.close()
