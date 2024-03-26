import time

from datastructures.stack import Stack

ITERATIONS = 200_000


class StackBenchmark:
    @staticmethod
    def run():
        StackBenchmark.test_push()
        StackBenchmark.test_pop()

    @staticmethod
    def test_push():
        st = Stack[str]()

        start = time.time()

        for i in range(ITERATIONS):
            st.push(f'{i}')

        end = time.time()

        print(f'Time spent on {ITERATIONS} pushing: {end - start} seconds')

    @staticmethod
    def test_pop():
        st = Stack[str]()

        for i in range(ITERATIONS):
            st.push(f'{i}')

        start = time.time()

        for i in range(ITERATIONS):
            st.pop()

        end = time.time()

        print(f'Time spent on {ITERATIONS} pops: {end - start} seconds')


if __name__ == "__main__":
    StackBenchmark.run()
