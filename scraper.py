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

def downloadSubtitle(sub_link, search_query):
    r = requests.get(sub_link)
    file_name = f"{search_query} Subtitles"
    open(file_name, 'wb').write(r.content)
    print(f"Successfully downloaded {search_query} subtitles.")

def userSearchSubtitles():
    search_query = ''
    while not search_query:
        print("Enter a movie to find subtitles.")
        search_query = input()
        movie_results = searchForMovie(search_query)
        if(not movie_results):
            print("Movie could not be found. Please try again.")
            search_query = ''
    userChooseSubtitle(movie_results, search_query)

def userChooseSubtitle(movie_results, search_query):
    print(f"Getting results for {search_query}")
    subtitles = getSubOptions(movie_results)
    subtitles_indexed = []
    response = ''
    for key in subtitles:
        subtitles_indexed.append({key: subtitles[key]})
    for item in range(len(subtitles_indexed)):
        print(f"{item + 1}: {"".join([key for key in subtitles_indexed[item]])}")
    print(f"Found {len(subtitles)} subtitles in search.")
    print("Select a number to download the file.")
    while not response:
        response = input()
        try:
            response = int(response)
            if(response not in range(1, len(subtitles_indexed) + 1)):
                print("The number you have selected is invalid.")
                response = ''
                continue
            else:
                break
        except:
            print("You must select a number to download subtitle.")
            response = ''
            continue
    selected_subtitle = subtitles_indexed[response - 1]
    selected_subtitle = list(selected_subtitle.values())[0]
    downloadSubtitle(selected_subtitle, search_query)
    


if __name__ == "__main__":
    userSearchSubtitles()