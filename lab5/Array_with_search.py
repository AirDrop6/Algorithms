from abc import ABC, abstractmethod
import ctypes
from typing import TypeVar, Generic, Union

T = TypeVar("T")


class Value(ABC):

    @abstractmethod
    def value(self) -> int:
        ...


class Student(Value):
    name: str
    group: int
    course: int
    age: int
    average_mark: float

    def value(self) -> float:
        return self.average_mark

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


class Book(Value):
    author: str
    publisher: str
    pages: int
    price: int
    ISBN: str

    def value(self):
        return self.pages

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

    def __merge_sorting(self, buffer: list[Union[T, int]], left: int, right: int) -> None:
        if left < right:
            mid = (left + right) // 2
            self.__merge_sorting(buffer, left, mid)
            self.__merge_sorting(buffer, mid + 1, right)

            k, j = left, mid + 1
            i = left
            while i <= mid or j <= right:
                if j > right or (i <= mid and self[i].value() < self[j].value()):
                    buffer[k] = self[i]
                    i += 1
                else:
                    buffer[k] = self[j]
                    j += 1
                k += 1

            for i in range(left, right + 1):
                self.__arr[i] = buffer[i]

    # Сортировка слиянием
    def sort(self: 'Array[T]') -> None:
        if len(self) == 0:
            raise ValueError('List is empty')

        buffer = [0 for _ in range(len(self))]
        self.__merge_sorting(buffer, 0, len(self) - 1)

    def __ternary_search_impl(self: 'Array[Student]', target_mark: float, left: int, right: int) -> int:
        if right > left:
            if right - left == 1:
                if self[right].value() == target_mark:
                    return right
                if self[left].value() == target_mark:
                    return left
                raise ValueError("Not Found")

            step = round((right - left) / 3)
            m1 = left + step
            m2 = m1 + step

            if self[m1].value() == target_mark:
                return m1

            if self[m2].value() == target_mark:
                return m2

            if target_mark < self[m1].value():
                return self.__ternary_search_impl(target_mark, left, m1)
            elif self[m1].value() < target_mark < self[m2].value():
                return self.__ternary_search_impl(target_mark, m1, m2)
            else:
                return self.__ternary_search_impl(target_mark, m2, right)

        raise ValueError("Not Found")

    # Поиск индекса студента с искомой средней оценкой
    def ternary_search_average(self: 'Array[Student]', mark: float) -> int:
        try:
            self.sort()
        except ValueError as e:
            raise ValueError("Sorting has failed")

        if mark < self[0].value() or self[len(self) - 1].value() < mark:
            raise ValueError("Not Found")

        return self.__ternary_search_impl(mark, 0, len(self) - 1)

    # Поиск индекса книги с искомым кол-вом страниц
    def interpolationt_search_pages(self: 'Array[Book]', pages: int) -> int:
        try:
            self.sort()
        except ValueError as e:
            raise ValueError("Sorting has failed")

        if pages < self[0].value() or self[len(self) - 1].value() < pages:
            raise ValueError("Not Found")

        low = 0
        high = len(self) - 1
        while(self[low].value() != self[high].value() and
                self[low].value() <= pages <= self[high].value()):
            pos = low + int((high - low) /
                            (self[high].value() - self[low].value()) *
                            (pages - self[low].value()))

            if self[pos].value() == pages:
                return pos
            elif self[pos].value() < pages:
                low = pos + 1
            else:
                high = pos - 1

        raise ValueError("Not Found")
