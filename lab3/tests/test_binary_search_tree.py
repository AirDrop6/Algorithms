import unittest
from datastructures.binary_search_tree import BinarySearchTree, Car


class TestBinarySearchTree(unittest.TestCase):
    def test_init(self):
        tree = BinarySearchTree[Car]()

        self.assertIsInstance(tree, BinarySearchTree)

    def test_is_empty_insert(self):
        tree1 = BinarySearchTree[Car]()
        tree2 = BinarySearchTree[Car]()

        car = Car()
        car.price = 5000
        tree1.insert(car)

        self.assertTrue(tree2.is_empty())
        self.assertFalse(tree1.is_empty())

    def test_inserts(self):
        tree = BinarySearchTree[Car]()

        car1 = Car()
        car2 = Car()
        car3 = Car()

        car1.price = 5000
        car2.price = 3000
        car3.price = 8000

        tree.insert(car1)
        tree.insert(car2)
        tree.insert(car3)

        self.assertEqual(car1, tree.root.data)
        self.assertEqual(car2, tree.root.left.data)
        self.assertEqual(car3, tree.root.right.data)

    def test_find(self):
        tree = BinarySearchTree[Car]()

        car1 = Car()
        car2 = Car()
        car3 = Car()

        car1.price = 5000
        car2.price = 3000
        car3.price = 8000

        tree.insert(car1)
        tree.insert(car2)

        self.assertEqual(car1, tree.find(car1))
        self.assertEqual(car2, tree.find(car2))
        self.assertEqual(None, tree.find(car3))

    def test_min_and_max(self):
        tree = BinarySearchTree[Car]()

        car1 = Car()
        car2 = Car()
        car3 = Car()

        car1.price = 5000
        car2.price = 3000
        car3.price = 8000

        tree.insert(car1)
        tree.insert(car2)
        tree.insert(car3)

        self.assertEqual(car2, tree.min())
        self.assertEqual(car3, tree.max())

    def test_deleting(self):
        tree = BinarySearchTree[Car]()

        car1 = Car()
        car2 = Car()
        car3 = Car()
        car4 = Car()
        car5 = Car()
        car6 = Car()

        car1.price = 5000
        car2.price = 3000
        car3.price = 8000
        car4.price = 2000
        car5.price = 1000
        car6.price = 4000

        tree.insert(car1)
        tree.insert(car2)
        tree.insert(car3)
        tree.insert(car4)
        tree.insert(car5)
        tree.insert(car6)

        tree.delete(car5)
        self.assertEqual(tree.get_size(), 5)

        tree.delete(car2)
        self.assertEqual(tree.get_size(), 4)

        tree.delete(car4)
        self.assertEqual(tree.get_size(), 3)

        tree.delete(car1)
        tree.delete(car3)
        tree.delete(car6)
        self.assertEqual(tree.get_size(), 0)

    def test_importing_from_file(self):
        tree = BinarySearchTree[Car]()
        file = open('../benchmarks/cars.txt', mode='r')
        tree.insert_from_file(file)
        file.close()

        self.assertFalse(tree.is_empty())
        self.assertEqual(tree.get_size(), 10)


if __name__ == '__main__':
    unittest.main()
