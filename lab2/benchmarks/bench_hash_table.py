import time

from datastructures.hash_table import HashTable

ITERATIONS = 200_000


class HashTableBenchmark:
    @staticmethod
    def run():
        HashTableBenchmark.test_add()
        HashTableBenchmark.test_search()

    @staticmethod
    def test_add():
        table: HashTable[str, int] = HashTable()

        start = time.time()

        for i in range(ITERATIONS):
            table[f'key-{i}'] = i

        end = time.time()

        print(f'Time spent on {ITERATIONS} elements additions: {end - start} seconds')

    @staticmethod
    def test_search():
        table: HashTable[str, int] = HashTable()

        for i in range(ITERATIONS):
            table[f'key-{i}'] = i

        start = time.time()

        for i in range(ITERATIONS):
            table[f'key-{i}']

        end = time.time()

        print(f'Time spent on searching {ITERATIONS} elements: {end - start} seconds')


if __name__ == "__main__":
    HashTableBenchmark.run()
