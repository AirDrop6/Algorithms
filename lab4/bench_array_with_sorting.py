import time
from Array_with_sorting import Array, Student, Book

ITERATIONS = 10000


class ArrayBenchmark:
    @staticmethod
    def run():
        ArrayBenchmark.students_sorts()
        ArrayBenchmark.books_sorts()

    @staticmethod
    def students_sorts():
        s = Array[Student]()
        students = [Student("Petrov", 4218, 3, 18, 5),
                    Student("Ivanov", 4218, 4, 18, 5),
                    Student("Sidorov", 4218, 2, 18, 5),
                    Student("Vasyachkin", 4218, 1, 18, 5),
                    Student("Kolotushkin", 4218, 2, 18, 5),
                    Student("Abvgdeev", 4218, 6, 18, 5),
                    Student("Vasilev", 4218, 1, 18, 5),
                    Student("Spiransky", 4218, 4, 18, 5),
                    Student("Zhukov", 4218, 6, 18, 5),
                    Student("Lozeykin", 4218, 29, 18, 5),
                    Student("Kitov", 4218, 3, 18, 5),
                    Student("Bonov", 4218, 3, 18, 5),
                    Student("Sopkin", 4218, 6, 18, 5),
                    Student("Rulkin", 4218, 1, 18, 5),
                    Student("Udaev", 4218, 2, 18, 5),
                    Student("Finnesov", 4218, 4, 18, 5),
                    Student("Kait", 4218, 7, 18, 5),
                    Student("Jops", 4218, 9, 18, 5),
                    Student("Danilov", 4218, 5, 18, 5),
                    Student("Kozlovsky", 4218, 8, 18, 5)]
        for el in students:
            s.append(el)

        start = time.time()
        for i in range(ITERATIONS):
            s.sort_fio()
            if i == ITERATIONS - 1:
                print("sort_fio:")
                print(s)
            s.sort_course()
            if i == ITERATIONS - 1:
                print("sort_course:")
                print(s)
        end = time.time()
        print(f'Time spent on 10000 sorting: {end - start} seconds. \n')

    @staticmethod
    def books_sorts():
        b = Array[Book]()
        books = [Book("Bredberry", "RosPrint", 50, 115, "ISBN-13"),
                 Book("Pushkin", "RosPrint", 50, 150, "ISBN-13"),
                 Book("Sapkovsky", "RosPrint", 50, 170, "ISBN-13"),
                 Book("Lermontov", "RosPrint", 50, 130, "ISBN-13"),
                 Book("London", "RosPrint", 50, 100, "ISBN-13"),
                 Book("Tolstoy", "RosPrint", 50, 65, "ISBN-13"),
                 Book("Tolkien", "RosPrint", 50, 120, "ISBN-13"),
                 Book("Rouling", "RosPrint", 50, 50, "ISBN-13"),
                 Book("Chehov", "RosPrint", 50, 30, "ISBN-13"),
                 Book("Dostoevsky", "RosPrint", 50, 90, "ISBN-13"),
                 Book("Bunin", "RosPrint", 50, 115, "ISBN-13"),
                 Book("Fet", "RosPrint", 50, 150, "ISBN-13"),
                 Book("Tutchev", "RosPrint", 50, 170, "ISBN-13"),
                 Book("Gogol", "RosPrint", 50, 130, "ISBN-13"),
                 Book("Nekrasov", "RosPrint", 50, 100, "ISBN-13"),
                 Book("Titov", "RosPrint", 50, 65, "ISBN-13"),
                 Book("Gusev", "RosPrint", 50, 120, "ISBN-13"),
                 Book("Krasnov", "RosPrint", 50, 50, "ISBN-13"),
                 Book("Lisichkin", "RosPrint", 50, 30, "ISBN-13"),
                 Book("Kepko", "RosPrint", 50, 90, "ISBN-13")
                 ]
        for el in books:
            b.append(el)

        start = time.time()
        for i in range(ITERATIONS):
            b.sort_price()
            if i == ITERATIONS - 1:
                print("sort_price:")
                print(b)
            b.sort_author()
            if i == ITERATIONS - 1:
                print("sort_author:")
                print(b)
        end = time.time()
        print(f'Time spent on 10000 sorting: {end - start} seconds. \n')


if __name__ == '__main__':
    ArrayBenchmark.run()
