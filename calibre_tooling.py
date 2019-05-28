"""Calibre library Python tooling."""

#   Monday May 27th 23:40
#   d@v1d.dk CPH, DK

import pandas, json, re, os
from collections import namedtuple, OrderedDict


class DictWithSearch(dict):
    """dict object with search, intitle and intags functions."""

    def __repr__(self):
        """Build string representation with title and tags."""
        
        titles = [t for t in self]                                                                                                                                
        string_repr = ""
        for item in titles:
            string_repr += item
            if not isinstance(self[item].tags, float):
                string_repr += "   (" + self[item].tags + ")"
                string_repr += "\n"
            else:
                string_repr += "\n"
        return(string_repr)
    
    def search(self, search_term, field):
        """Takes search term and field name, returns dictionary of results."""

        result = DictWithSearch()
        for book in self:
            # ignore un-tagged books
            if isinstance(getattr(self[book], field), float):
                continue
            elif search_term.lower() in getattr(self[book], field).lower():
                result[book] = self[book]
                
        return(result)

    def intitle(self, search_term):
        """Partially match title field, return result list. 
        Syntactic sugar for dict.search(search_term, 'title')."""

        result = DictWithSearch()
        for title_item in self:
            m = re.search(search_term.lower(), title_item.lower())
            if m:
                result[title_item] = self[title_item]
        return(result)

    def intags(self, search_term):
        """Partially match tag field, return result list. 
        Syntactic sugar for dict.search(search_term, 'tags')."""

        result = DictWithSearch()
        for title_item in self:
            tags = str(self[title_item].tags).lower()
            m = re.search(search_term.lower(), tags)
            if m:
                result[title_item] = self[title_item]
        return(result)


def build_dict(filename):
    """Load JSON file into dictionary."""

    library_df = pandas.read_csv(filename)
    values = library_df.get_values()

    mybooks = DictWithSearch()
    for book in values:
        Book = namedtuple('Book', 'author description path_to_cover_jpg '\
                          'time_stamp book_format isbn identifiers language '\
                          'library_name pubdate publisher rating series series_index '\
                          'size tags title title_sort id_no uuid amazon_url')
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

    return mybooks


def write_json(mybooks, filename):
    """Write dictionary to file."""
    
    json_dict = json.dumps(mybooks)
    with open(filename,'w') as f:
        f.write(json_dict)


def load_json(filename):
    """Load dictionary from JSON file."""

    with open(filename, 'r') as f:
        mybooks = json.load(f)
    return(mybooks)


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


def _get_csv_filename():
    files = os.listdir()
    result = []
    for file in files:
        m = re.search('.csv', file)
        if m:
            result.append(file)

    if len(result) != 1:
        return "Error: Didn't find exactly one .csv file in folder"
    else:
        return result[0]

mybooks = build_dict(_get_csv_filename())
books = mybooks
