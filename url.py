from bs4 import BeautifulSoup
import requests
import json



WATCH_URL="https://www.youtube.com/watch?v="
USER_AGENT="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3"
CACHE_FILE="cache.json"

def getCachedIds()->dict:
    try:
        with open(CACHE_FILE,'r') as cachefile:
            return json.loads(cachefile.read())
    except:
        return {}
    
def writeCachedId(channelName:str,channelId:str,cache:dict)->dict:
    cache[channelName]=channelId
    with open(CACHE_FILE,'w') as cachefile:
        cachefile.write(json.dumps(cache,indent=4))


def getChannelId(channelName:str)->str:
    cache=getCachedIds()
    channel_url=f"https://www.youtube.com/@{channelName}"
    
    if channelName in cache:
        return cache[channelName]
    
    response=requests.get(channel_url,headers={
        "User-Agent":USER_AGENT
    })
    if response.status_code!=200:
        print(f"Something went wrong with the fetching the channel id,{response.status_code}")
    
    soup=BeautifulSoup(response.content,'html.parser')
    try:
        channelId=soup.select('meta[itemprop*=identifier]')[0]['content']
        writeCachedId(channelName,channelId,cache)
        return channelId
    except Exception as e:
        print(e)
        return None
        
def getLiveUrl(channelName:str)->str:
    channelId=getChannelId(channelName)
    if not channelId:
        raise ValueError("channelId is not useable")
    live_url=f"https://www.youtube.com/channel/{channelId}/live"

    response=requests.get(live_url,headers={
        "User-Agent":USER_AGENT
    })
    
    if response.status_code!=200:
        print(f"Something went wrong with the getting the live url,{response.status_code}")
    
    soup=BeautifulSoup(response.content,'html.parser')
    for element in soup.select('link[rel*=canonical]'):
        if WATCH_URL in element['href']:
            return element['href']
    
    return None