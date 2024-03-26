import ctypes
from typing import TypeVar, Generic, Union, Callable

T = TypeVar("T")


class Student:
    name: str
    group: int
    course: int
    age: int
    average_mark: float

    def __str__(self):
        return f'Student(name:{self.name},' \
               f'group:№{self.group}, ' \
               f'course:{self.course}, ' \
               f'age:{self.age}, ' \
               f'average_mark:{self.average_mark})'

    def __init__(self, name, group, course, age, average_mark):
        self.name = name
        self.group = group
        self.course = course
        self.age = age
        self.average_mark = average_mark


class Book:
    author: str
    publisher: str
    pages: int
    price: int
    ISBN: str

    def __str__(self):
        return f'Book(author:{self.author},' \
               f'publisher:{self.publisher}, ' \
               f'pages:{self.pages}, ' \
               f'price:{self.price}$, ' \
               f'ISBN:{self.ISBN})'

    def __init__(self, author, publisher, pages, price, isbn):
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.ISBN = isbn


class IndexOutOfRangeException(Exception):
    pass


class Heap:
    def __init__(self, values: Union[list[T], 'Array[Students]'], comp: Callable[[T, T], bool]):
        self.__length: int = 0
        self.__comp: Callable[[T, T], bool] = comp
        self.__arr: list[T] = []
        for i in range(len(values)):
            self.insert(values[i])

    def trickle_up(self, index: int) -> None:
        parent: int = (index - 1) // 2
        bottom: T = self.__arr[index]

        while index > 0 and self.__comp(self.__arr[parent], bottom):
            self.__arr[index] = self.__arr[parent]
            index = parent
            parent = (parent - 1) // 2

        self.__arr[index] = bottom

    def trickle_down(self, index: int) -> None:
        large_child: int
        top: T = self.__arr[index]
        while index < self.__length // 2:
            left_child: int = 2 * index + 1
            right_child: int = left_child + 1
            if (right_child < self.__length and
                    self.__comp(self.__arr[left_child], self.__arr[right_child])):
                large_child = right_child
            else:
                large_child = left_child

            if not self.__comp(top, self.__arr[large_child]):
                break

            # Потомок сдвигается вверх
            self.__arr[index] = self.__arr[large_child]
            index = large_child

        self.__arr[index] = top  # index <- корень

    def insert(self, value: T) -> None:
        self.__arr.append(value)
        self.trickle_up(self.__length)
        self.__length += 1

    def pop(self) -> T:
        if len(self.__arr) == 0:
            raise ValueError("array is empty")

        root: T = self.__arr[0]
        self.__length -= 1
        self.__arr[0] = self.__arr[self.__length]
        self.trickle_down(0)
        return root


class Array(Generic[T]):
    def __init__(self):
        self.__length: int = 0
        self.__size: int = 20
        self.__arr: ctypes.Array[T] = (self.__size * ctypes.py_object)()

    def __str__(self):
        answer = "["
        for i in range(self.__length):
            answer += str(self.__arr[i])
            if i != self.__length - 1:
                answer += ","
        answer += "]"
        return answer

    def __len__(self) -> int:
        return self.__length

    def __getitem__(self, index: int) -> T:
        if self.__check_range(index):
            return self.__arr[index]
        else:
            raise IndexOutOfRangeException('Index out of range')

    def __setitem__(self, index: int, value: T) -> None:
        if not self.__check_range(index):
            raise IndexOutOfRangeException('Index out of range')
        else:
            if self.__length == self.__size:
                self.__resize()
            self.__arr[index] = value

    def __check_range(self, index) -> bool:
        if index >= self.__length or index < 0:
            return False
        else:
            return True

    def __resize(self) -> None:
        new_size = self.__size * 2
        new_arr: ctypes.Array[T] = (new_size * ctypes.py_object)()

        for i in range(self.__length):
            new_arr[i] = self.__arr[i]

        self.__size = new_size
        self.__arr = new_arr

    def append(self, value: T) -> None:
        if self.__length == self.__size:
            self.__resize()

        self.__arr[self.__length] = value
        self.__length += 1

    def insert(self, index: int, value: T):
        if not self.__check_range(index):
            raise IndexOutOfRangeException('Index out of range')
        if self.__length == self.__size:
            self.__resize()

        last = self.__arr[self.__length - 1]
        for i in range(self.__length, index, -1):
            self.__arr[i] = self.__arr[i - 1]

        self.__arr[index] = value
        self.append(last)

    def sort_fio(self: 'Array[Student]'):   #Сортировка перемешиванием для Students

        if len(self) == 0:
            raise ValueError('List is empty')

        def swap(i: int, j: int):
            self[i], self[j] = self[j], self[i]

        left = 0
        right = len(self) - 1

        while left <= right:
            for i in range(right, left, -1):
                if self[i - 1].name > self[i].name:
                    swap(i - 1, i)
            left += 1
            for i in range(left, right):
                if self[i].name > self[i + 1].name:
                    swap(i, i + 1)
            right -= 1

    def sort_price(self: 'Array[Book]'):    #Сортировка вставками для Book
        if len(self) == 0:
            raise ValueError('List is empty')
        for i in range(1, len(self)):
            temp = self[i]
            it = i
            while it > 0 and self[it - 1].price > temp.price:
                self[it] = self[it - 1]
                it -= 1
            self[it] = temp

    def __merge_sorting(self, buffer: list[Union[Book, int]], left: int, right: int) -> None:
        if left < right:
            mid = (left + right) // 2
            self.__merge_sorting(buffer, left, mid)
            self.__merge_sorting(buffer, mid + 1, right)

            k, j = left, mid + 1
            i = left
            while i <= mid or j <= right:
                # print(self.__arr[i], self.__arr[j], j)
                # if self.__arr[j] == 0:
                #     print(self)
                if j > right or (i <= mid and self[i].author > self[j].author):
                    buffer[k] = self[i]
                    i += 1
                else:
                    buffer[k] = self[j]
                    j += 1
                k += 1

            for i in range(left, right + 1):
                self.__arr[i] = buffer[i]

    def sort_author(self: 'Array[Book]') -> None:    #Сортировка слиянием для Book
        if len(self) == 0:
            raise ValueError('List is empty')

        buffer = [0 for _ in range(len(self))]
        self.__merge_sorting(buffer, 0, len(self) - 1)

    def sort_course(self: 'Array[Student]') -> None:  #Сортировка кучей для Students
        if len(self) == 0:
            raise ValueError("List is empty")

        heap = Heap(self, lambda i, j: i.course > j.course)
        for i in range(len(self) - 1, -1, -1):
            self[i] = heap.pop()


if __name__ == '__main__':
    stud = Array[T]()
    boox = Array[T]()

    Books = [Book("Bredberry", "RosPrint", 50, 115, "ISBN-13"),
             Book("Pushkin", "RosPrint", 50, 150, "ISBN-13"),
             Book("Sapkovsky", "RosPrint", 50, 170, "ISBN-13"),
             Book("Lermontov", "RosPrint", 50, 130, "ISBN-13"),
             Book("London", "RosPrint", 50, 100, "ISBN-13"),]

    Students = [Student("Petrov", 4218, 3, 18, 5),
                Student("Ivanov", 4218, 4, 18, 5),
                Student("Sidorov", 4218, 2, 18, 5),
                Student("Vasyachkin", 4218, 1, 18, 5),
                Student("Kolotushkin", 4218, 2, 18, 5)]

    for el in Students:
        stud.append(el)

    for el in Books:
        boox.append(el)


