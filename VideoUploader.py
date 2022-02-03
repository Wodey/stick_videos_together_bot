import requests
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

URI = "https://www.googleapis.com/upload/youtube/v3/videos"

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

metadata = {
    "title": "",
    "description": "",
    "category": "",
    "keywords": "",
    "privacy": "",
}

FILE_PATH = "final_video.mp4"
CLIENT_SECRETS_FILE = "client_secrets.json"

YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class VideoUploader:
    def __init__(self, args):
        flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                       scope=YOUTUBE_UPLOAD_SCOPE)

        storage = Storage("%s-oauth2.json")
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            credentials = run_flow(flow, storage, args)



    def upload(self):
        r = requests.post(URI, {})

if __name__ == "__main__":
    v_u = VideoUploader()
    