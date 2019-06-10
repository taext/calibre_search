"""Calibre library Python tooling."""

#   Monday Jun 10th 13:35
#   by d@v1d.dk CPH, DK

import pandas, json, re, os, copy, sh, time
from collections import namedtuple, OrderedDict
from lib import libgen, goodreads, thehiddenbay, youtube, bing_image_search, amazon_link
from dataclasses import dataclass


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
                result[title_item] = copy.deepcopy(self[title_item])
        return(result)


    def amazon_open(self):
        result = [] 
        for item in self:
            #print(calibre.books[item].amazon_url) 
            result.append(self[item].amazon_url)
        if len(result) < 201:
            sh.google_chrome(result)
        else:
            return "error: more than 200 results, assuming a mistake has been made ( in amazon_open)"

    def cover_html(self, width, link_to):
        """link_to options: amazon libgen goodread thehiddenbay youtube bing_image_search."""

        covers = []
        html_str = '<a href="linkylinky" alt="none title="Amazon"><img src="smiley.gif" alt="Smiley face" width="300"></img></a>'
        temp_html_str = html_str.replace('300', str(width))
        #print(f'temp_html_str: {temp_html_str}')
        for item in self:

            abreviated_title = self[item].title.split(':')[0]

            if isinstance(self[item].path_to_cover_jpg, float):
                continue # NB: consequenses unknown :D .D
            new_html_str = temp_html_str.replace('smiley.gif', self[item].path_to_cover_jpg)
            if link_to.lower() == 'amazon':
                new_html_str = new_html_str.replace('linkylinky',self[item].amazon_url)
                #new_html_str = new_html_str.replace('Amazon',self[item].amazon_url)
            if link_to.lower() == 'libgen':
                new_html_str = new_html_str.replace('linkylinky', libgen.main(abreviated_title))
            if link_to.lower() == 'goodreads':
                new_html_str = new_html_str.replace('linkylinky', goodreads.main(abreviated_title))
            if link_to.lower() == 'thehiddenbay':
                new_html_str = new_html_str.replace('linkylinky', thehiddenbay.main(abreviated_title))
            if link_to.lower() == 'youtube':
                new_html_str = new_html_str.replace('linkylinky', youtube.main(abreviated_title))
            if link_to.lower() == 'bing-image-search':
                new_html_str = new_html_str.replace('linkylinky', bing_image_search.main(abreviated_title))
                #new_html_str = new_html_str.replace('Amazon',self[item].amazon_url)
            #print(self[item].amazon_url)
            covers.append(new_html_str)
        covers_str = " ".join([cover for cover in covers])
        return(covers_str)

    def cover_browser(self, width=300, link_to='amazon'):
        """link_to="help" for options."""

        if link_to == 'help':
            return("options: amazon libgen goodreads thehiddenbay youtube bing-image-search")
        html_str = self.cover_html(width=width, link_to=link_to)
        with open('temp.htm','w') as f:
            f.write(html_str)
        sh.firefox('temp.htm')
        time.sleep(1)
        os.remove('temp.htm')

    def untagged(self):
        result = DictWithSearch()

        for item in self:
            if isinstance(self[item].tags, float):
                result[item] = self[item]
        return(result)

    def no_amazon_id(self):
        """Takes DictWithSearch, returns title of Books without Amazon identifier hash."""
        result = []
        for item in self:
            try:
                self[item].identifiers['amazon']
            except:
                result.append(item)
                
        return result



@dataclass
class BookDataClass:

    def amazon_url(self):
        url = 'https://www.amazon.com/dp/' + self.identifiers['amazon'] 
        return url

   
    author: str
    description: str
    path_to_cover_jpg: str
    time_stamp: str
    book_format: str
    isbn: str
    identifiers: dict
    language : str
    library_name: str
    pubdate : str
    publisher: str
    rating: str
    series: str
    series_index: str
    size: str
    tags: list
    title: str
    title_sort: str
    id_no: str
    uuid: str


class AmazonLinkBook(BookDataClass):

    def __repr__(self):
        repr_str = self.title  + '   (' + self.book_format + ')' + "   (" + self.tags + ')'
        return(repr_str)

    def amazon_url_method(self):
        if 'amazon' in self.identifiers:
            #print(f'self.identifiers: {self.identifiers}')
            url = 'https://www.amazon.com/dp/' + self.identifiers['amazon']
            return url
    


    def lookup_amazon_link(self):
        """Uses the amazon_link module to lookup Amazon link and add to identifiers."""

        def amazon_url(amazon_hash):
            url = 'https://www.amazon.com/dp/' + amazon_hash
            return url
        
        # try:
        #     amazon_url = amazon_url(self.identifiers['amazon'])
        # except:
        #     amazon_url = ""

        # return amazon_url


        print(f'Looking up {self.title} Amazon URL...')
        ama_link = amazon_link.main(self.title)
        if ama_link == None:
            # Amazon link lookup was unsuccesfull
            print('failed to get Amazon link')
            return
        #print('ama_link: ', ama_link)
        self.identifiers['amazon'] = ama_link[1]
        #print('OVER HERE: ', amazon_url(self.identifiers['amazon']))
        self.amazon_url = amazon_url(self.identifiers['amazon'])
        #return DictWithSearchObj


def build_dict(filename):
    """Load JSON file into dictionary."""

    def split_identifiers(id_str):
        my_dict = {}
        if not isinstance(id_str, float):
            id_lines = id_str.split(",")
            for id_line in id_lines:
                
                if len(id_line.split(":")) == 2:
                    key, value = id_line.split(":")
                    my_dict[key] = value
            
        return my_dict

    library_df = pandas.read_csv(filename)
    values = library_df.get_values()

    mybooks = DictWithSearch()
    for book in values:
        
       

        BookofTheLoop = AmazonLinkBook(author = book[1],
            description = book[2],
            path_to_cover_jpg = book[3],
            time_stamp = book[4],
            book_format = book[5],
            isbn = book[6],
            identifiers = split_identifiers(book[7]),
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
            )
        
        title = book[17]

        mybooks[title] = BookofTheLoop

        try:
            mybooks[title].amazon_url = amazon_url(mybooks[title].identifiers['amazon'])
        except:
            mybooks[title].amazon_url = ""
        

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
