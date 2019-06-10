import calibre_tooling as calibre
import unittest

class TestCalibreTooling(unittest.TestCase):

    def test_dict_building(self):
        
        books = calibre.build_dict('tests/welcome_shelf.csv')                                                                                                
        self.assertEqual(len(books), 34)

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
        string_repr = german_search.__repr__()[:276]
        result_to_check_for = """Basic German: A Grammar and Workbook (Grammar Workbooks)   (pdf)   (German, Language, Teaching Methods & Materials)\nReaktionen der organischen Chemie   (pdf)   (Chemistry, Organic, Science, German, Language)\nRFID   (pdf)   (Electronics, Wireless, German, Computers, Language)\n"""
        self.assertEqual(string_repr, result_to_check_for)