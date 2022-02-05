import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


URI = "https://www.googleapis.com/upload/youtube/v3/videos"

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

metadata = {
    "title": "",
    "description": "",
    "category": "10",
    "keywords": "",
    "privacy": "private",
}

FILE_PATH = "final_video.mp4"
CLIENT_SECRETS_FILE = "client_secret_1038976130845-vc9k99fan2ods2c6pbakmk4aiuuq85gk.apps.googleusercontent.com.json"

YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class VideoUploader:
    def __init__(self):
        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)

                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        try:
            self.service = build('docs', 'v1', credentials=creds)

        except HttpError as err:
            print(err)

    def upload(self):
        self.service.video().insert(

        )

if __name__ == "__main__":
    v_u = VideoUploader()
    