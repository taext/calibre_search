#!/home/dd/anaconda3/bin/python
import sys, re
import bn as bing

def main(book_title):
    """Takes book title, uses Bing to get Amazon URL."""

    amazon_search_str = 'amazon ' + book_title
    results = bing.return_results(amazon_search_str, 8)
    for item in results:
        if '/dp/' in item and '.com/' in item:
            m = re.search('\/dp\/([0-9]+)', item)
            if m:
                hash_found = m.group(1)
                return [item, hash_found]
    
    
if __name__ == '__main__':
    
    result = main(sys.argv[1])
    if len(result) > 0:
        print(result[0])
