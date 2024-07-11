import unittest
import pandas as pd
from booklover import BookLover
class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        """
        Add a book and test if it is in `book_list`.
        """
        reader = BookLover('John Doe', 'john.doe@example.com', 'mystery')
        reader.add_book('Mystery Novel 1', 4)
        message = "Book is not in the list"
        self.assertTrue('Mystery Novel 1' in reader.book_list['book_name'].values, message)

    def test_2_add_book(self):
        """
        Add the same book twice. Test if it's in `book_list` only once.
        """
        reader = BookLover('John Doe', 'john.doe@example.com', 'mystery')
        reader.add_book('Mystery Novel 1', 4)
        reader.add_book('Mystery Novel 1', 4)
        expected = 1
        message = "Book is in the list more than once"
        self.assertEqual(len(reader.book_list[reader.book_list['book_name'] == 'Mystery Novel 1']), expected, message)

    def test_3_has_read(self): 
        """
        Pass a book in the list and test if the answer is `True`.
        """
        reader = BookLover('John Doe', 'john.doe@example.com', 'mystery')
        reader.add_book('Mystery Novel 1', 4)
        test_value = reader.has_read('Mystery Novel 1')
        message = "Book is not marked as read"
        self.assertTrue(test_value, message)

    def test_4_has_read(self): 
        """
        Pass a book NOT in the list and test if the answer is `False`.
        """
        reader = BookLover('John Doe', 'john.doe@example.com', 'mystery')
        reader.add_book('Mystery Novel 1', 4)
        test_value = reader.has_read('Science Fiction Novel 1')
        message = "Book is incorrectly marked as read"
        self.assertFalse(test_value, message)

    def test_5_num_books_read(self): 
        """
        Add some books to the list, and test num_books matches expected.
        """
        reader = BookLover('John Doe', 'john.doe@example.com', 'mystery')
        reader.add_book('Mystery Novel 1', 4)
        reader.add_book('Science Fiction Novel 1', 2)
        reader.add_book('Fantasy Novel 1', 4)
        reader.add_book('Non-Fiction Book 1', 5)
        
        num_books = reader.num_books_read()
        expected = 4
        message = "Number of books read does not match expected"
        self.assertEqual(num_books, expected, message)

    def test_6_fav_books(self):
        """
        Add some books with ratings to the list, making sure some of them have rating > 3. 
        Your test should check that the returned books have rating > 3.
        """
        reader = BookLover('John Doe', 'john.doe@example.com', 'mystery')
        reader.add_book('Mystery Novel 1', 4)
        reader.add_book('Romance Novel 1', 2)
        reader.add_book('Science Fiction Novel 1', 1)
        reader.add_book('Fantasy Novel 1', 3)
        reader.add_book('Historical Fiction Novel 1', 5)
        fav_book_list = reader.fav_books()
        message = "Not all favorite books have a rating greater than 3"
        self.assertTrue(all(fav_book_list['book_rating'] > 3), message)

if __name__ == '__main__':
    unittest.main(verbosity=3)