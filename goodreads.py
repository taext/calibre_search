
def main(search_term):

    url = "https://www.goodreads.com/search?q=kierkegaard+soren"

    new_search_term = search_term.replace(' ','+')

    new_url = url.replace('kierkegaard+soren', new_search_term)

    return new_url

