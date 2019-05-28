#!/home/dd/anaconda3/bin/python
# bn - bing first result new (arbitrary no. results & piping) 
# v2.1 (November 27th 2017)

# Searches bing.com and returns search result URL(s).

# What's New: add 3-digit count args


import sys, requests, re
import bing_stepper
from more_itertools import unique_everseen

userAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'

def return_results(args, count=1):
    
    """Takes args string, returns Bing search result(s),
    1-2 digit integer values in args interpreted as count, 
    default count 1."""

    # NB: CHECKS FOR OVERRIDING INTEGER VALUE count IN args SEARCH TERMS

    m = re.search('[\s\'](\d{1,3})[\s\']', args)
    if m:
    
        count = int(m.group(1))
        args = args[:-(len(m.group(1))+2)]

    search_string = args.replace(" ","+")
    bing_string = 'http://www.bing.com/search?q=' + search_string

    result = [] 
    
    while count > len(result):

        r = requests.get(bing_string, headers={"User-Agent": userAgent})
        m = re.findall('href=\"(http.*?)\"', r.text)

        filtered_results = []
        [filtered_results.append(item) for item in m if 'bat.bing' not in item and 'translator' not in item \
        and 'choice.microsoft' not in item and 'go.microsoft' not in item and 'bing.microsoft' not in item \
        and 'privacy.microsoft' not in item]
        for item in filtered_results:
            if len(item) < 220:        # NB: arbitrary length limit (for ad links)
                result.append(item)

        result = list(unique_everseen(result))

        #count = count - len(filtered_results)
        bing_string = bing_stepper.next_page(bing_string)

    return(result[:count])


if __name__ == '__main__':

    if len(sys.argv) == 1:       # no arguments, piping mode
        args = sys.stdin.read()  # if no piped input,
        result = return_results(args)  # reads from keyboard
    
    else:
        args = []
        [args.append(item) for item in sys.argv[1:]]
        if args:
            result = return_results(str(args))

    for url in result:
        print(url)


