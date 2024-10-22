# youtube-livestream-monitor
Capture livestreams from a public youtube channel using only a channel id. Allows you to download all streams automatically.
# Installation
To install all depedencies run
```
./install.sh
```
This will install the packages in `requirements.txt` and grab the executable `ytarchive` from https://github.com/Kethsar/ytarchive.
# Usage
To run you will need to navigate the channel you want to download from, `https://www.youtube.com/@LofiGirl`. Then take only the username at the end of the url which is `LofiGirl`. Then use the program like this
```
python LiveDownloader.py -i 
```
or
```
python LiveDownloader.py --id
```
