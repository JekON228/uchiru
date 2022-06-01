#!/bin/bash
fileid="1E4yRCDzdT9nax6F_TuA4Tl1otcBSuyV0"
filename="$HOME/Downloads/image2.png"
googlefolder="$HOME/Downloads/google.dmg"
html=`curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}"`
curl -Lb ./cookie "https://drive.google.com/uc?export=download&`echo ${html}|grep -Po '(confirm=[a-zA-Z0-9\-_]+)'`&id=${fileid}" -o ${filename}
osascript -e 'tell application "System Events" to set picture of every desktop to "'"$filename"'"'
curl https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg -o ${googlefolder}
hdiutil attach ${googlefolder}
cp -R /Volumes/Google\ Chrome /Applications/
hdiutil detach $(hdiutil info | grep Google | awk '{print$1}')

