

```python
import calibre_search as cali
```

<br>

## Accessing specific books and fields

`calibre_search` loads the .csv Calibre library export file in its main folder on import.

This library is represented by the `books` object:


```python
cali.books['Dive Into Python']
```




    Dive Into Python   (pdf)   (Python, Programming, Computers)




```python
res = cali.books['Dive Into Python']

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
