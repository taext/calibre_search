#!/home/dd/anaconda3/bin/python


def main(search_term):
    #arg_list = sys.argv[1:]

    url = 'http://gen.lib.rus.ec/search.php?req=mysearchquery&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def'
    url = url.replace('mysearchquery', search_term)

    return(url)
