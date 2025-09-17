""" Build service test
Building service process of GoogleDriveManager.access.py tests.
TODO 1; Check GoogleDriveManager.access.Credentials class.
"""


from GoogleDriveManager.access import Credentials

from googleapiclient.http import MediaFileUpload


if __name__ == '__main__':
    # test Credentials class
    creds = Credentials("/home/swimmy/ドキュメント/02_メンター/KASHIWAGI/token.pkl", "/home/swimmy/ドキュメント/02_メンター/KASHIWAGI/credentials.json")
    service = creds.build_service()

    # file upload test
    file_metadata = {'name': 'sample.txt', "parents": ["1FOdJBovjuaXJr1IDmRAJdR5ULQlOQUNs"]}
    media = MediaFileUpload('sample.txt', mimetype='text/plain')
    uploaded = service.files().create(body=file_metadata, media_body=media, fields='id, parents').execute()
    print("Uploaded File ID:", uploaded.get('id'))
    ...
