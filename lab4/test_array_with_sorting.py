import unittest
from Array_with_sorting import Array, Student, Book


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

    def test_sort_fio(self):
        arr = Array()
        student1 = Student("Belov", 4218, 3, 18, 5)
        student2 = Student("Klozin", 4218, 4, 18, 5)
        student3 = Student("Antonov", 4218, 2, 18, 5)
        arr.append(student1)
        arr.append(student2)
        arr.append(student3)
        arr.sort_fio()
        self.assertEqual(arr[0], student3)
        self.assertEqual(arr[1], student1)
        self.assertEqual(arr[2], student2)

    def test_sort_course(self):
        arr = Array()
        student1 = Student("Belov", 4218, 3, 18, 5)
        student2 = Student("Klozin", 4218, 4, 18, 5)
        student3 = Student("Antonov", 4218, 2, 18, 5)
        arr.append(student1)
        arr.append(student2)
        arr.append(student3)
        arr.sort_course()
        self.assertEqual(arr[0], student2)
        self.assertEqual(arr[1], student1)
        self.assertEqual(arr[2], student3)

    def test_sort_price(self):
        arr = Array()
        book1 = Book("Bredberry", "RosPrint", 50, 115, "ISBN-13")
        book2 = Book("Sapkovsky", "RosPrint", 50, 170, "ISBN-13")
        book3 = Book("Chehov", "RosPrint", 50, 30, "ISBN-13")
        arr.append(book1)
        arr.append(book2)
        arr.append(book3)
        arr.sort_price()
        self.assertEqual(arr[0], book3)
        self.assertEqual(arr[1], book1)
        self.assertEqual(arr[2], book2)

    def test_sort_author(self):
        arr = Array()
        book1 = Book("Bredberry", "RosPrint", 50, 115, "ISBN-13")
        book2 = Book("Astafiev", "RosPrint", 50, 170, "ISBN-13")
        book3 = Book("Chehov", "RosPrint", 50, 30, "ISBN-13")
        arr.append(book1)
        arr.append(book2)
        arr.append(book3)
        arr.sort_author()
        self.assertEqual(arr[0], book3)
        self.assertEqual(arr[1], book1)
        self.assertEqual(arr[2], book2)


if __name__ == '__main__':
    unittest.main()
