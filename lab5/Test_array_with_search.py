import unittest
from Array_with_search import Array, Student, Book


class TestArray(unittest.TestCase):
    def test_init(self):
        arr = Array()
        self.assertIsInstance(arr, Array)

    def test_append(self):
        arr = Array()
        student1 = Student("Petrov", 4218, 3, 18, 5)
        student2 = Student("Ivanov", 4218, 4, 18, 5)
        arr.append(student1)
        arr.append(student2)
        self.assertEqual(arr[0], student1)
        self.assertEqual(arr[1], student2)

    def test_ternary_search_average(self):
        arr = Array()
        student1 = Student("Petrov", 4218, 3, 18, 1.2)
        student2 = Student("Ivanov", 4218, 4, 18, 2.3)
        student3 = Student("Sidorov", 4218, 2, 18, 3.3)
        student4 = Student("Vasyachkin", 4218, 1, 18, 4.7)
        arr.append(student1)
        arr.append(student2)
        arr.append(student3)
        arr.append(student4)

        self.assertEqual(arr.ternary_search_average(1.2), 0)
        self.assertEqual(arr.ternary_search_average(2.3), 1)
        self.assertEqual(arr.ternary_search_average(3.3), 2)
        self.assertEqual(arr.ternary_search_average(4.7), 3)
        self.assertEqual(arr.ternary_search_average(4.7), 3)
        self.assertRaises(ValueError, arr.ternary_search_average, 5.0)

    def test_interpolationt_search_pages(self):
        arr = Array()
        book1 = Book("Bredberry", "RosPrint", 97, 115, "ISBN-13")
        book2 = Book("Astafiev", "RosPrint", 113, 170, "ISBN-13")
        book3 = Book("Chehov", "RosPrint", 155, 30, "ISBN-13")
        book4 = Book("Lisichkin", "RosPrint", 666, 30, "ISBN-13")
        arr.append(book1)
        arr.append(book2)
        arr.append(book3)
        arr.append(book4)

        self.assertEqual(arr.interpolationt_search_pages(97), 0)
        self.assertEqual(arr.interpolationt_search_pages(113), 1)
        self.assertEqual(arr.interpolationt_search_pages(155), 2)
        self.assertEqual(arr.interpolationt_search_pages(666), 3)
        self.assertRaises(ValueError, arr.ternary_search_average, 999)

