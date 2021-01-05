from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.SetContentString('Hello')
file1.Upload()

file1['title'] = 'HelloWorld.txt'
file1.Upload()

# file = GoogleDrive.CreateFile({'title': 'TestFile.txt', 'mimeType': 'text/plan'})
# file.SetContentString("Hello World")gauth.LocalWebserverAuth()

# file.Upload(param={'convert': True})
