import keaton_tooling as kt                                                                                                        
import unittest

class TestCalibreTooling(unittest.TestCase):

    def test_dict_building(self):
        
        books = kt.build_dict('Tag German.csv')                                                                                                
        self.assertEqual(len(books), 31)

    def test_dict_length(self):
        
        self.assertEqual(len(kt.books), 4245)

    def test_searching(self):

        spanish_search = kt.books.search('spanish','tags')                                                                                    
        self.assertEqual(len(spanish_search), 13)

    def test_secondary_search(self):

        spanish_search = kt.books.search('spanish','tags')                                                                                    
        second_search = spanish_search.search('science','tags')
        self.assertEqual(len(second_search), 2)

    def test_repr(self):

        german_search = kt.books.search('german','tags')
        string_repr = german_search.__repr__()
        result_to_check_for = """Basic German: A Grammar And Workbook (Grammar Workbooks)
Reaktionen Der Organischen Chemie
Rfid
S-Ketamin - Aktuelle Interdisziplinäre Aspekte"""
        self.assertEqual(string_repr[:142], result_to_check_for)