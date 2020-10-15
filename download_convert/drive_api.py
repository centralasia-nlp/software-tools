from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import io
from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

# Note: folder_id can be parsed from the shared link
def listFiles(service, folder_id):
    listOfFiles = []

    #query = f"'{folder_id}' in parents and mimeType='image/jpeg'"
    query = f"'{folder_id}' in parents and mimeType='application/pdf'"
    # Get list of pdf files in shared folder
    page_token = None
    while True:
        response = service.files().list(
            q=query,
            fields="nextPageToken, files(id, name)",
            pageToken=page_token,
            includeItemsFromAllDrives=True, 
            supportsAllDrives=True
        ).execute()

        for file in response.get('files', []):
            listOfFiles.append(file)

        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

    return listOfFiles

def downloadFiles(service, listOfFiles):
    # Download all pdfs
    for fileID in listOfFiles:
        request = service.files().get_media(fileId=fileID['id'])
        fh = io.FileIO('ziyonet/' + fileID['name'], 'wb')
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Downloading..." + str(fileID['name']))

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    """
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    """
    #folder_id = '1DrKy3xsQq5Why6wWk7rFa5ntnVl5uEmJ' #ziyonet
    folder_id = '1YFNFTm91C1Lb-XxFbXHpaqUEzm6Roo7e' #test folder
    list = listFiles(service, folder_id)
    downloadFiles(service, list)


if __name__ == '__main__':
    main()