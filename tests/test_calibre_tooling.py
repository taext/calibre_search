import calibre_tooling as calibre
import unittest

class TestCalibreTooling(unittest.TestCase):

    def test_dict_building(self):
        
        books = calibre.build_dict('tests/tag_german.csv')                                                                                                
        self.assertEqual(len(books), 31)

    def test_dict_length(self):
        
        self.assertEqual(len(calibre.books), 4262)

    def test_searching(self):

        spanish_search = calibre.books.search('spanish','tags')                                                                                    
        self.assertEqual(len(spanish_search), 13)

    def test_secondary_search(self):

        spanish_search = calibre.books.search('spanish','tags')                                                                                    
        second_search = spanish_search.search('science','tags')
        self.assertEqual(len(second_search), 2)

    def test_repr(self):

        german_search = calibre.books.search('german','tags')
        string_repr = german_search.__repr__()
        result_to_check_for = """Basic German: A Grammar and Workbook (Grammar Workbooks)   (German, Language, Teaching Methods & Materials)
Reaktionen der organischen Chemie   (Chemistry, Organic, Science, German, Language)
RFID   (Electronics, Wireless, German, Computers, Language)"""
        self.assertEqual(string_repr[:251], result_to_check_for)