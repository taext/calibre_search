
def main(search_term):

    url = "https://thehiddenbay.com/search/veep%20s01e01/1/99/0"

    new_search_term = search_term.replace(' ','%20')

    new_url = url.replace('veep%20s01e01', new_search_term)

    return new_url

