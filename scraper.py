import googlesearch
from urllib.request import Request, urlopen
import re

def searchForMovie(search_request):
    subdl_request = search_request + ' subdl'
    search_results = googlesearch.search(subdl_request, start=0, stop=10)
    subdl_url = ''
    for result in search_results:
        if(re.search('.*subdl.*', result)):
            subdl_url = result
            break
    else:
        print("Could not find result with that movie title.")
    if(subdl_url):
        return subdl_url
    else:
        return ''