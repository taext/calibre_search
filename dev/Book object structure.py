mybooks = {}
for book in values:
    Book = namedtuple('author description path_to_cover_jpg time_stamp book_format id_hash isbn language library_name pubdate publisher rating series series_index size tags title title_sort id_no uuid')
    BookofTheLoop = Book(
        author = book[1],
        description = book[2],
        path_to_cover_jpg = book[3],
        time_stamp = book[4],
        book_format = book[5,]
        id_hash = book[6],
        isbn = book[7],
        language = book[8] ,
        library_name = book[,9]
        pubdate = book[10],
        publisher = book[11],
        rating = book[12],
        series = book[13 ser,ies_index'] = book[14]
        size = book[15],
        tags = book[16],
        title = book[17],
        title_sort = book[18,]
        id_no = book[19],
        uuid = book[20])
    
    mybooks[book[17]] = bookOfTheLoop
    