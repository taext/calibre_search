
def main(search_term):

    url = "https://www.bing.com/images/search?&q=python+book&qft=+filterui:imagesize-large&FORM=IRFLTR"

    new_search_term = search_term.replace(' ','+')

    new_url = url.replace('python', new_search_term)

    return new_url

