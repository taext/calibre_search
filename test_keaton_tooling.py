import keaton_tooling as kt                                                                                                        
import unittest

class TestCalibreTooling(unittest.TestCase):

    def test_dict_loading(self):
        books = kt.build_dict('keaton.csv')                                                                                                

        self.assertEqual(len(books), 4245)

    def test_searching(self):

        books = kt.build_dict('keaton.csv')                                                                                                
        spanish_search = books.search('spanish','tags')                                                                                    
        self.assertEqual(len(spanish_search), 13)

    def test_secondary_search(self):

        books = kt.build_dict('keaton.csv')                                                                                                
        spanish_search = books.search('spanish','tags')                                                                                    
        second_search = spanish_search.search('science','tags')
        self.assertEqual(len(second_search), 2)