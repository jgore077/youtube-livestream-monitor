import streamlink
import subprocess
import argparse
from streamlink.stream import *
from time import sleep

class LiveDownloader():
    def __init__(self,user:str,delay:int=30) -> None:
        self.delay=delay
        self.user=user
        self.link=f'https://www.youtube.com/@{user}'
    
    def getStreams(self):
        return streamlink.streams(self.link)
    
    def downloadStream(self):
        streams=self.getStreams()
        stream=streams["best"]
        if (type(stream)==HLSStream):
            print('Start recording')
            urlarray=stream.url.split('/')
            streamurl=urlarray[urlarray.index('id')+1].split('.')[0]
            subprocess.run(['./ytarchive','--merge','-o' ,'streams/',f'https://www.youtube.com/watch?v={streamurl}','best'])
            return
        print(f'{self.user} is offline')    
        
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
                    description='Given a username this program will watch that users Youtube account and download their livestreams',)
    parser.add_argument('-u', '--user',required=True)
    args = parser.parse_args()
      
    downloader=LiveDownloader(args.user)
    downloader.monitorStream()