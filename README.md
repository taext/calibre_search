

```python
import calibre_tooling as cali
```

<br>

## Accessing specific books and fields

calibre_tooling loads the `.csv` Calibre library export file found in its main folder on import.

This can then be accessed using the books object:


```python
cali.books['Dive Into Python']                            # the raw dataclass Book object
```




    AmazonLinkBook(author='Mark Pilgrim', description='  * Quick start to learning python―very example oriented approach \n  * Book has its own Web site established by the author: http://diveintopython.org/ \n\n\nAuthor is well known in the Open Source community and the book has a unique quick approach to learning an object oriented language.\n**\n', path_to_cover_jpg='/media/truecrypt1/Keaton Institute Intelligence Library/Mark Pilgrim/Dive Into Python (1079)/cover.jpg', time_stamp='2015-12-30T19:32:32+01:00', book_format='pdf', isbn='9781590593561', identifiers={'isbn': '9781590593561', 'amazon': '1590593561'}, language='eng', library_name='Keaton Institute Intelligence Library', pubdate='2004-07-19T00:00:00+02:00', publisher='Apress', rating=nan, series=nan, series_index=1.0, size=1278909.0, tags='Python, Programming, Computers', title='Dive Into Python', title_sort='Dive Into Python', id_no=1079, uuid='3df4a186-339f-4632-90d1-11d4d062d169')




```python
res = cali.books['Dive Into Python']
```


```python
[field for field in dir(res) if not "__" in field]           # the Book object fields
```




    ['amazon_url',
     'amazon_url_method',
     'author',
     'book_format',
     'description',
     'id_no',
     'identifiers',
     'isbn',
     'language',
     'library_name',
     'lookup_amazon_link',
     'path_to_cover_jpg',
     'pubdate',
     'publisher',
     'rating',
     'series',
     'series_index',
     'size',
     'tags',
     'time_stamp',
     'title',
     'title_sort',
     'uuid']



<br>

The `Book` object fields can be accessed by dot field name:


```python
cali.books['Dive Into Python'].tags
```




    'Python, Programming, Computers'






<br>

## Searching

#### General search

You can search any specific field using `.search(search_term, field_name)`:


```python
cali.books.search('spa', 'language')
```




    Ficciones   (Fiction, Classics)
    Conceptos de espacio   (Architecture, Spanish, Language, Classics)
    Ideas. Historia Intelectual de La Humanidad by ...   (Philosophy, History, Spanish, Language)
    Los enemigos del comercio   (Spanish, Language)
    Termodinámica   (Physics, Spanish, Language, Textbook, Science)
    Microeconomía intermedia   (Economics, Micro, Language, Spanish)
    Frame Analysis. Los Marcos De La Experiencia (Spanish Edition)   (Psychology, Social Psychology, Language, Spanish)
    A lomos de dragones   (Spanish, Language)
    Escupelo



<br>

#### Filtering on title

You can partially match title field using `.intitle`:


```python
cali.books.intitle('spanish')
```




    Schaum's Outline of Spanish Grammar   (Language, Spanish, Schaums, Science, Teaching Methods & Materials)
    A Political History of Spanish: The Making of a Language   (Language, Spanish, History, Politics, To Read)
    Frame Analysis. Los Marcos De La Experiencia (Spanish Edition)   (Psychology, Social Psychology, Language, Spanish)
    Practice Makes Perfect® Complete Spanish Grammar: Premium: Second Edition
    Oxford Spanish Dictionary   (Spanish, Language, Dictionary)



<br>

#### Filtering on tag

You can partially match tags using `books.intags`:


```python
cali.books.intags('spanish')
```




    Schaum's Outline of Spanish Grammar   (Language, Spanish, Schaums, Science, Teaching Methods & Materials)
    Wing-Chun   (Wing Chun, Martial Arts & Self-Defense, Spanish, Language, Grey)
    Persuasión   (Negotiation, Spanish, Language)
    Conceptos de espacio   (Architecture, Spanish, Language, Classics)
    Ideas. Historia Intelectual de La Humanidad by ...   (Philosophy, History, Spanish, Language)
    A Political History of Spanish: The Making of a Language   (Language, Spanish, History, Politics, To Read)
    Los enemigos del comercio   (Spanish, Language)
    Termodinámica   (Physics, Spanish, Language, Textbook, Science)
    Microeconomía intermedia   (Economics, Micro, Language, Spanish)
    Frame Analysis. Los Marcos De La Experiencia (Spanish Edition)   (Psychology, Social Psychology, Language, Spanish)
    A lomos de dragones   (Spanish, Language)
    The Reign of Greed   (Philippine fiction (Spanish) -- Translations into English, Nationalists -- Philippines -- Fiction, Philippines -- History -- Fiction)
    Oxford Spanish Dictionary   (Spanish, Language, Dictionary)



<br>

#### Chaining filters

The `.intitle` and `.intags` filters can be chained:


```python
cali.books.intitle('spanish').intags('psychology')
```




    Frame Analysis. Los Marcos De La Experiencia (Spanish Edition)   (Psychology, Social Psychology, Language, Spanish)



<br>
