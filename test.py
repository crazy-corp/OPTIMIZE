from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from apiclient.http import MediaFileUpload
scopes = ['https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('token.json', scopes)

http_auth = credentials.authorize(Http())
drive_service = build('drive', 'v3', http=http_auth)

url="https://drive.google.com/uc?export=view&id="
file_id='1794quNMNXCx2-qCLwBf0J5Pyno1EPiuX'
permission = {'type': 'anyone',
              'value': 'anyone',
              'role': 'reader'}
permission=drive_service.permissions().create(fileId=file_id,body=permission).execute()
print(permission)





# folder_id = '1aDc1Md6zn-gNMqRX4ii4tnt8BFCcNhxo'
# file_metadata = {
    # 'name': 'photo.jpg',
    # 'parents': [folder_id]
# }
# media = MediaFileUpload('image.jpg',
                        # mimetype='image/jpeg',
                        # resumable=True)
# file = drive_service.files().create(body=file_metadata,
                                    # media_body=media,
                                    # fields='id').execute()
# print('File ID: %s' % file.get('id'))



# file_metadata = {
    # 'name': 'Images',
    # 'mimeType': 'application/vnd.google-apps.folder'
# }
# file = drive.files().create(body=file_metadata,
                                    # fields='id').execute()
# print('Folder ID: %s' % file.get('id'))

#1aDc1Md6zn-gNMqRX4ii4tnt8BFCcNhxo   FolderID

# file_metadata = {'name': 'image.jpg'}
# media = MediaFileUpload('image.jpg',
                        # mimetype='image/jpeg')
# file = drive.files().create(body=file_metadata,
                                    # media_body=media,
                                    # fields='id').execute()
# print('File ID: %s' % file.get('id'))
# request = drive.files().list().execute()
# files = request.get('items', [])
# for f in files:
    # print(f)