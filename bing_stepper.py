#!/home/dd/anaconda3/bin/python
"""next page module for bing.com search results"""
# bing_stepper v0.1 (November 27th 2017)
import re


def next_page(url):

    """Takes Bing search result URL, returns next search result page URL."""

    m = re.search('first', url)
    if m:
        m2 = re.search('first=(\d+)&', url)
        page_count = int(m2.group(1))
        new_page_count = page_count + 10
        to_be_replaced = 'first=' + str(page_count)
        replacement = 'first=' + str(new_page_count)
        new_url = url.replace(to_be_replaced, replacement)
    else:
        new_url = url + '&amp;first=11&amp;FORM=PORE&first=11&FORM=PORE'
        
    return(new_url)