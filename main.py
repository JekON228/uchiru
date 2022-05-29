#!/usr/bin/python
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
import io
import os
from pathlib import Path

os.system('source venv/bin/activate ')
SCOPES = ['https://www.googleapis.com/auth/drive']
API_KEY = 'AIzaSyAiBGaxoluBRbQWLXTKNqXXNkJqCF-SJLk'
service = build('drive', 'v3', developerKey=API_KEY)
file_id = '1E4yRCDzdT9nax6F_TuA4Tl1otcBSuyV0'
request = service.files().get_media(fileId=file_id)
filename = str(Path.home() / "Downloads/file2.png")
fh = io.FileIO(filename, 'wb')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))
cmd = """osascript -e 'tell application "System Events" to set picture of every desktop to "~/Downloads/file2.png"'"""
os.system(cmd)
os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
os.system('brew install --cask skype')
# :os.system('launchctl unload -w ~/Library/LaunchAgents/')
