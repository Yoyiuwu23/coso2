import requests

def google_dork_search(query):
    url = f'https://www.google.com/search?q={query}'
    response = requests.get(url)
    return response.text 