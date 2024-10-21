from bs4 import BeautifulSoup
import requests



WATCH_URL="https://www.youtube.com/watch?v="
USER_AGENT="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3"
def getLiveUrl(channelId:str)->str:
    
    live_url=f"https://www.youtube.com/channel/{channelId}/live"

    response=requests.get(live_url,headers={
        "User-Agent":USER_AGENT
    })
    
    if response.status_code!=200:
        print(f"Something went wrong with the request,{response.status_code}")
    
    soup=BeautifulSoup(response.content,'html.parser')
    for element in soup.select('link[rel*=canonical]'):
        if WATCH_URL in element['href']:
            return element['href']
    
    return None