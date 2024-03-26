from Array_with_search import Array, Student, Book
import time
ITERATIONS = 100000


class ArrayBenchmark:
    @staticmethod
    def run():
        ArrayBenchmark.student_search()
        ArrayBenchmark.book_search()

    @staticmethod
    def student_search():
        print("Students:")
        s = Array[Student]()
        students = [Student("Petrov", 4218, 3, 18, 5.0),
                    Student("Ivanov", 4218, 4, 18, 4.1),
                    Student("Sidorov", 4218, 2, 18, 3.3),
                    Student("Vasyachkin", 4218, 1, 18, 2.1),
                    Student("Kolotushkin", 4218, 2, 18, 2.7),
                    Student("Abvgdeev", 4218, 6, 18, 4.3),
                    Student("Vasilev", 4218, 1, 18, 3.8),
                    Student("Spiransky", 4218, 4, 18, 3.9),
                    Student("Zhukov", 4218, 6, 18, 4.0),
                    Student("Lozeykin", 4218, 29, 18, 4.4),
                    Student("Kitov", 4218, 3, 18, 4.9),
                    Student("Bonov", 4218, 3, 18, 3.2),
                    Student("Sopkin", 4218, 6, 18, 1.7),
                    Student("Rulkin", 4218, 1, 18, 1.5),
                    Student("Udaev", 4218, 2, 18, 4.8),
                    Student("Finnesov", 4218, 4, 18, 4.6),
                    Student("Kait", 4218, 7, 18, 1.1),
                    Student("Jops", 4218, 9, 18, 1.3),
                    Student("Danilov", 4218, 5, 18, 2.2),
                    Student("Kozlovsky", 4218, 8, 18, 3.1)]
        for el in students:
            s.append(el)

        start = time.time()

        for i in range(int(ITERATIONS/2)):
            s.ternary_search_average(4)
            s.ternary_search_average(3.2)

        end = time.time()

        print(f'Time spent on {ITERATIONS} iterations: {end - start} sec \n')

    @staticmethod
    def book_search():
        print("Books:")
        b = Array[Book]()
        books = [Book("Bredberry", "RosPrint", 97, 115, "ISBN-13"),
                 Book("Pushkin", "RosPrint", 220, 150, "ISBN-13"),
                 Book("Sapkovsky", "RosPrint", 113, 170, "ISBN-13"),
                 Book("Lermontov", "RosPrint", 674, 130, "ISBN-13"),
                 Book("London", "RosPrint", 841, 100, "ISBN-13"),
                 Book("Tolstoy", "RosPrint", 21, 65, "ISBN-13"),
                 Book("Tolkien", "RosPrint", 84, 120, "ISBN-13"),
                 Book("Rouling", "RosPrint", 99, 50, "ISBN-13"),
                 Book("Chehov", "RosPrint", 155, 30, "ISBN-13"),
                 Book("Dostoevsky", "RosPrint", 111, 90, "ISBN-13"),
                 Book("Bunin", "RosPrint", 219, 115, "ISBN-13"),
                 Book("Fet", "RosPrint", 724, 150, "ISBN-13"),
                 Book("Tutchev", "RosPrint", 452, 170, "ISBN-13"),
                 Book("Gogol", "RosPrint", 123, 130, "ISBN-13"),
                 Book("Nekrasov", "RosPrint", 88, 100, "ISBN-13"),
                 Book("Titov", "RosPrint", 449, 65, "ISBN-13"),
                 Book("Gusev", "RosPrint", 23, 120, "ISBN-13"),
                 Book("Krasnov", "RosPrint", 414, 50, "ISBN-13"),
                 Book("Lisichkin", "RosPrint", 666, 30, "ISBN-13"),
                 Book("Kepko", "RosPrint", 73, 90, "ISBN-13")]
        for el in books:
            b.append(el)

        start = time.time()

        for i in range(int(ITERATIONS/2)):
            b.ternary_search_average(666)
            b.ternary_search_average(220)

        end = time.time()

        print(f'Time spent on {ITERATIONS} iterations: {end - start} sec \n')


if __name__ == '__main__':
    ArrayBenchmark.run()