import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from src.schemes.product import ProductSchema


class AGoogleTable:
    service = None

    def __init__(self, spreadsheet_id: str, scopes: list[str], secret: str = "secret.json"):
        self.spreadsheet_id: str = spreadsheet_id
        self.scopes: list[str] = scopes
        self.secret: str = secret

        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'secret.json', self.scopes)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def __call__(self):
        return self


class IGoogleTable:
    def send(self, data: list[ProductSchema]):
        raise NotImplementedError()
