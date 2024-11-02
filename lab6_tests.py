import data
import lab6
import unittest


# Define test cases for each part
class TestCases(unittest.TestCase):
    # Part 0: Tests for the index_smallest_from function

    def test_index_smallest_from_1(self):
        # Test case where smallest element is at index 3
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)

    def test_index_smallest_from_2(self):
        # Test case where smallest element is at index 4, starting from index 4
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)

    def test_index_smallest_from_3(self):
        # Test case where start index is out of bounds, expecting None
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)

    def test_index_smallest_from_4(self):
        # Test case with an empty list, expecting None
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)

    # Part 0: Tests for the selection_sort function

    def test_selection_sort_1(self):
        # Already sorted list should remain the same
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)

    def test_selection_sort_2(self):
        # Empty list should remain empty
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)

    def test_selection_sort_3(self):
        # Reverse sorted list should be sorted in ascending order
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)

    def test_selection_sort_4(self):
        # Unsorted list should be sorted in ascending order
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)

    # Part 1: Tests for the sorting_books function

    def test_sorting_books(self):
        # Sort books by title in alphabetical order
        books = [
            data.Book(["Author A"], "Zebra"),
            data.Book(["Author B"], "Apple"),
            data.Book(["Author C"], "Mango"),
        ]
        lab6.selection_sort_books(books)
        self.assertEqual(books[0].title, "Apple")
        self.assertEqual(books[1].title, "Mango")
        self.assertEqual(books[2].title, "Zebra")

    def test_empty_list(self):
        # Empty list of books should remain empty
        books = []
        lab6.selection_sort_books(books)
        self.assertEqual(books, [])

    # Part 2: Tests for the swap_case function

    def test_swap_case(self):
        # Test swapping uppercase and lowercase characters
        self.assertEqual(lab6.swap_case("Hello World"), "hELLO wORLD")
        self.assertEqual(lab6.swap_case("PyThOn123"), "pYtHoN123")
        self.assertEqual(lab6.swap_case(""), "")  # Test with an empty string

    # Part 3: Tests for the str_translate function

    def test_basic_replacement(self):
        # Test replacing 'a' with 'x'
        self.assertEqual(lab6.str_translate('abcdcba', 'a', 'x'), 'xbcdcbx')

    def test_replacing_with_same_char(self):
        # Test replacing 'a' with 'a', should remain the same
        self.assertEqual(lab6.str_translate('banana', 'a', 'a'), 'banana')

    # Part 4: Tests for the histogram function

    def test_histogram(self):
        # Test word frequency in a string
        self.assertEqual(lab6.histogram("hello world hello"), {"hello": 2, "world": 1})
        self.assertEqual(lab6.histogram("one two three two one one"), {"one": 3, "two": 2, "three": 1})
        self.assertEqual(lab6.histogram(""), {})  # Test with an empty string


# Run the test cases
if __name__ == '__main__':
    unittest.main()
