import calibre_tooling as calibre
import unittest

class TestBook(unittest.TestCase):

    def test_book_title(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.title, 'Learning Python Testing')

    def test_book_tags(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.tags, 'Python, Testing, Computers')

    def test_book_author(self): 
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.author, 'Daniel Arbuckle')

    def test_book_identifiers(self): 
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.identifiers, {'isbn': '9781783553228', 'amazon': 'B00Q6T04GO', 'google': '_e-ZBQAAQBAJ'})

    def test_book_amazon_link(self): 
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.amazon_url_method(), 'https://www.amazon.com/dp/B00Q6T04GO')



    def test_book_description(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.description[:69], '**A straightforward and easy approach to testing your Python projects')

    def test_book_path_to_cover(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.path_to_cover_jpg, '/media/truecrypt1/Keaton Institute Intelligence Library/Daniel Arbuckle/Learning Python Testing (5560)/cover.jpg')

    def test_book_time_stamp(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.time_stamp, '2018-12-29T11:00:40+01:00')

    def test_book_book_format(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.book_format, 'pdf')

    def test_book_isbn(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.isbn, '9781783553228')

    def test_book_language(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.language, 'eng')

    def test_book_pubdate(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.pubdate, '2014-11-25T00:00:00+01:00')

    def test_book_publisher(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.publisher, 'Packt Publishing')

    def test_book_size(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.size, 1616077.0)

    def test_book_id_no(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.id_no, 5560)

    def test_book_uuid(self):
        python_book = calibre.books['Learning Python Testing']
        self.assertEqual(python_book.uuid, 'b8a94794-65e2-44f1-afb6-a13a4adb456b')
