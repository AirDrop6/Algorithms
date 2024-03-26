import time
from datastructures.binary_search_tree import BinarySearchTree, Car


class BinarySearchTreeBenchmark:

    @staticmethod
    def run():
        BinarySearchTreeBenchmark.inserting_from_file()

    @staticmethod
    def inserting_from_file():
        tree: BinarySearchTree[Car] = BinarySearchTree()
        file = open('cars.txt', mode='r')

        start_ins = time.time()
        tree.insert_from_file(file)
        end_ins = time.time() + 0.001

        print(f'Time spent on inserting 10 elements from file: {round((end_ins - start_ins) * 1000)} milliseconds. Tree:')
        tree.print_tree()

        start_save = time.time()
        tree.save_info_in_file()
        end_save = time.time() + 0.001

        print(f'Time spent on saving tree in file(your_cars.txt): {round((end_save - start_save) * 1000)} milliseconds')


if __name__ == '__main__':
    BinarySearchTreeBenchmark.run()
