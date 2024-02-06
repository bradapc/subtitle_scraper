import googlesearch
import requests
import re
from bs4 import BeautifulSoup

def searchForMovie(search_request):
    subdl_request = search_request + ' subdl'
    search_results = googlesearch.search(subdl_request, start=0, stop=10)
    subdl_url = ''
    for result in search_results:
        if(re.search('.*subdl.*', result)):
            subdl_url = result + '/english'
            break
    else:
        print("Could not find result with that movie title.")
    if(subdl_url):
        return subdl_url
    else:
        return ''
    
def getSubOptions(subdl_url):
    subtitles = {}
    page = requests.get(subdl_url)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find('div')
    for div in data:
        a = div.findAll('a')
        for elem in a:
            if(".zip" in elem['href']):
                subtitles[elem.text] = elem['href']
    return subtitles

def downloadSubtitle(sub_link, search_request):
    r = requests.get(sub_link)
    file_name = f"{search_request} Subtitles"
    open(file_name, 'wb').write(r.content)