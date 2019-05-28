
def main(search_term):

    url = "https://www.youtube.com/results?search_query=nytt+paa+nytt"

    new_search_term = search_term.replace(' ','+')

    new_url = url.replace('nytt+paa+nytt', new_search_term)

    return new_url

