import unittest
from datastructures.AVL_tree import AVLTree, Student


class TestAVLTree(unittest.TestCase):
    def test_innit(self):
        tree = AVLTree[Student]()

        self.assertIsInstance(tree, AVLTree)

    def test_is_empty_insert(self):
        tree1 = AVLTree[Student]()
        tree2 = AVLTree[Student]()

        student = Student()
        student.average_mark = 5.0
        tree1.insert(student)

        self.assertTrue(tree2.is_empty())
        self.assertFalse(tree1.is_empty())

    def test_inserts(self):
        tree = AVLTree[Student]()

        student1 = Student()
        student2 = Student()
        student3 = Student()

        student1.average_mark = 5.0
        student2.average_mark = 4.5
        student3.average_mark = 3.4

        tree.insert(student1)
        tree.insert(student2)
        tree.insert(student3)

        self.assertEqual(student2, tree.root.data)
        self.assertEqual(student3, tree.root.left.data)
        self.assertEqual(student1, tree.root.right.data)

    def test_find(self):
        tree = AVLTree[Student]()

        student1 = Student()
        student2 = Student()
        student3 = Student()

        student1.average_mark = 5.0
        student2.average_mark = 4.5
        student3.average_mark = 3.4

        tree.insert(student1)
        tree.insert(student2)

        self.assertEqual(student1, tree.find(student1))
        self.assertEqual(student2, tree.find(student2))
        self.assertEqual(None, tree.find(student3))

    def test_min_and_max(self):
        tree = AVLTree[Student]()

        student1 = Student()
        student2 = Student()
        student3 = Student()

        student1.average_mark = 5.0
        student2.average_mark = 4.5
        student3.average_mark = 3.4

        tree.insert(student1)
        tree.insert(student2)
        tree.insert(student3)

        self.assertEqual(student3, tree.min())
        self.assertEqual(student1, tree.max())

    def test_deleting(self):
        tree = AVLTree[Student]()

        student1 = Student()
        student2 = Student()
        student3 = Student()
        student4 = Student()
        student5 = Student()
        student6 = Student()

        student1.average_mark = 5.0
        student2.average_mark = 4.5
        student3.average_mark = 3.4
        student4.average_mark = 2.2
        student5.average_mark = 3.8
        student6.average_mark = 4.3

        tree.insert(student1)
        tree.insert(student2)
        tree.insert(student3)
        tree.insert(student4)
        tree.insert(student5)
        tree.insert(student6)

        tree.delete(student4)
        self.assertEqual(tree.get_size(), 5)

        tree.delete(student2)
        self.assertEqual(tree.get_size(), 4)

        tree.delete(student6)
        self.assertEqual(tree.get_size(), 3)

        tree.delete(student1)
        tree.delete(student3)
        tree.delete(student5)
        self.assertEqual(tree.get_size(), 0)

    def test_importing_from_file(self):
        tree = AVLTree[Student]()
        file = open('../benchmarks/students.txt', mode='r')
        tree.insert_from_file(file)
        file.close()

        self.assertFalse(tree.is_empty())
        self.assertEqual(tree.get_size(), 10)


if __name__ == '__main__':
    unittest.main()
