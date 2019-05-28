"""Calibre library Python tooling."""

#   Python tooling for 
#
#        Keaton Institute Calibre Library
#
#   Monday May 27th 23:40
#   d@v1d.dk CPH, DK

import pandas, json
from collections import namedtuple, OrderedDict
from types import MethodType

class DictWithSearch(dict):

    def search(self, search_term, field):
        """Search Keaton Library books, returns dictionary of results."""

        result = DictWithSearch()
        for book in self:
            # ignore un-tagged books
            if isinstance(getattr(self[book], field), float):
                continue
            elif search_term.lower() in getattr(self[book], field).lower():
                #print(book)
                result[book] = self[book]
                
        return(result)


def build_dict(filename):
    """Load JSON file into dictionary."""

    keaton_df = pandas.read_csv(filename)
    values = keaton_df.get_values()

    mybooks = DictWithSearch()
    for book in values:
        Book = namedtuple('Book', 'author description path_to_cover_jpg time_stamp book_format isbn identifiers language library_name pubdate publisher rating series series_index size tags title title_sort id_no uuid amazon_url')
        if isinstance(book[7], float):
            book[7] = ""
        identi_str_list = (book[7]).split(',')           
        
        # parse identifiers into dict
        identi_dict = {}
        for item in identi_str_list:
            if ':' in item:
                try:
                    name, hash_val = item.split(':')
                except:
                    continue
                identi_dict[name] = hash_val

        def amazon_url(amazon_hash):
            url = 'https://www.amazon.com/dp/' + amazon_hash
            return url
        
        try:
            amazon_url = amazon_url(identi_dict['amazon'])
        except:
            amazon_url = ""


        BookofTheLoop = Book(author = book[1],
            description = book[2],
            path_to_cover_jpg = book[3],
            time_stamp = book[4],
            book_format = book[5],
            isbn = book[6],
            identifiers = identi_dict,
            language = book[8],
            library_name = book[9],
            pubdate = book[10],
            publisher = book[11],
            rating = book[12],
            series = book[13], 
            series_index = book[14],
            size = book[15],
            tags = book[16],
            title = book[17],
            title_sort = book[18],
            id_no = book[19],
            uuid = book[20],
            amazon_url = amazon_url)

        mybooks[book[17]] = BookofTheLoop

    def search(self, search_term, field):
        """Search Calibre books, returns dictionary of results."""



        result = DictWithSearch()
        for book in mybooks:
            # ignore un-tagged books
            if isinstance(getattr(mybooks[book], field), float):
                continue
            elif search_term.lower() in getattr(mybooks[book], field).lower():
                #print(book)
                result[book] = mybooks[book]

        return(result)

    mybooks.search = MethodType(search, mybooks)

    return mybooks

def write_json(mybooks, filename):
    """Write dictionary to file."""
    
    json = json.dumps(mybooks)
    with open(filename,'w') as f:
        f.write(json)
    
def load_json(filename):
    """Load dictionary from JSON file."""

    with open(filename, 'r') as f:
        mybooks = json.load(f)
    return(mybooks)

def search(search_term, field):
    """Search Keaton Library books, returns dictionary of results."""

    result = DictWithSearch()
    for book in mybooks:
        # ignore un-tagged books
        if isinstance(getattr(mybooks[book], field), float):
            continue
        elif search_term.lower() in getattr(mybooks[book], field).lower():
            #print(book)
            result[book] = mybooks[book]
            
    return(result)

def ten_titles_iter(result):
    """Iterates over library search dict result returning titles."""

    titles = [title for j, title in enumerate(result.keys())]  
    i = 0
    while i < len(titles): 
        yield(titles[i:i+10]) 
        i += 10

def show_covers_iter(result):
    """Iterates over library search dict result returning cover JPG file paths."""
    
    books = list(result.keys())
    i = 0
    while i < len(books): 
        yield(result[books[i]]['path_to_cover_jpg'])
        i += 1


mybooks = build_dict('keaton.csv')
books = mybooks
