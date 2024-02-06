import googlesearch
import re

search_request = ''

def searchMovieOnIMDB(search_request):
    search = googlesearch.search(search_request, start=0, stop=10)
    imdb_item = ''
    for item in search:
        if(re.search('.*imdb.com/title/tt.*', item)):
            imdb_item = item
            imdb_item = re.sub('.*tt', '', imdb_item)
            break
    else:
        print("Search yielded no imdb links.")
    if(imdb_item):
        return imdb_item
    else:
        return False