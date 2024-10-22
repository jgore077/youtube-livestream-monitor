from url import getLiveUrl
from time import sleep
import subprocess
import argparse

class LiveDownloader():
    def __init__(self,channel:str,delay:int=30) -> None:
        self.delay=delay
        self.channel=channel
    
    
    def downloadStream(self):
        url=getLiveUrl(self.channel)
        if url:
            subprocess.run(['./ytarchive','--merge','-o','streams/%(channel)s/%(title)s-%(id)s-%(url)s-%(start_date)s',url,'best'])
            return
        print(f'No stream to download, waiting {self.delay} seconds before checking again')    
        
    def monitorStream(self):
        while True:
            try:
                self.downloadStream()
            except Exception as e:
                print(e)
            sleep(self.delay)


if __name__=="__main__":
    
    parser = argparse.ArgumentParser(
                    prog='Monitoring Livestream Archiver',
                    description='Given a channel name this program will watch that users Youtube account and download their livestreams whenever they go live',)
    parser.add_argument('-c', '--channel',required=True)
    args = parser.parse_args()
      
    downloader=LiveDownloader(args.channel)
    downloader.monitorStream()