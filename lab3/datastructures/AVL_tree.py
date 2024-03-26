from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, Any


class EmptyTreeException(Exception):
    pass


class KeyNotFoundException(Exception):
    pass


class Key(ABC):

    @abstractmethod
    def key(self) -> int:
        ...


T = TypeVar("T", bound=Key)


class Student(Key):
    name: str
    group: int
    course: int
    age: int
    average_mark: float

    def key(self) -> float:
        return self.average_mark

    def __str__(self):
        return f'Student(name:{self.name},' \
               f' group:№{self.group}, ' \
               f'course:{self.course}, ' \
               f'age:{self.age}, ' \
               f'average_mark:{self.average_mark})'


class Node(Generic[T], Key):
    data: T
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    height: int = 0

    def key(self) -> int:
        return self.data.key()

    def __str__(self):
        return f'Student(name:{self.data.name},' \
               f' group:№{self.data.group}, ' \
               f'course:{self.data.course}, ' \
               f'age:{self.data.age}, ' \
               f'average_mark:{self.data.average_mark})'


class AVLTree(Generic[T]):

    def __init__(self):
        self.length: int = 0
        self.root: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.length == 0

    def get_size(self) -> int:
        return self.length

    @staticmethod
    def __height(node: Optional[Node]) -> int:
        if node is None:
            return -1
        return node.height

    def __balance_factor(self, node: Optional[Node]) -> int:
        return self.__height(node.right) - self.__height(node.left)

    def __update_height(self, node: Optional[Node]) -> None:
        hl = self.__height(node.left)
        hr = self.__height(node.right)

        if hl > hr:
            node.height = hl + 1
        else:
            node.height = hr + 1

    def __rotate_right(self, node: Node[T]) -> Node[T]:
        parent = node.left
        node.left = parent.right
        parent.right = node
        self.__update_height(node)
        self.__update_height(parent)
        return parent

    def __rotate_left(self, node: Node[T]) -> Node[T]:
        parent = node.right
        node.right = parent.left
        parent.left = node
        self.__update_height(node)
        self.__update_height(parent)
        return parent

    def __balance(self, node: Node[T]) -> Node[T]:
        self.__update_height(node)
        if self.__balance_factor(node) >= 2:
            if self.__balance_factor(node.right) < 0:
                node.right = self.__rotate_right(node.right)
            return self.__rotate_left(node)
        if self.__balance_factor(node) <= -2:
            if self.__balance_factor(node.left) > 0:
                node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)
        return node

    def __insert(self, node: Optional[Node], value: T) -> Node[T]:
        if node is None:
            new_node: Node = Node()
            new_node.data = value
            return new_node
        if value.key() < node.key():
            node.left = self.__insert(node.left, value)
        else:
            node.right = self.__insert(node.right, value)
        return self.__balance(node)

    def insert(self, value: T) -> None:
        self.root = self.__insert(self.root, value)
        self.length += 1

    @staticmethod
    def __find_minimum_root_node(node: Optional[Node]) -> Node:
        current_node = node.left
        if current_node is None:
            return node
        while current_node.left is not None:
            current_node = current_node.left

        return current_node

    def __remove_node_with_min_key(self, node: Optional[Node]) -> Node:
        if node.left is None:
            return node.right
        node.left = self.__remove_node_with_min_key(node.left)
        return self.__balance(node)

    def __delete(self, node: Optional[Node], value: T) -> Optional[Node]:
        if node is None:
            return None

        if value.key() < node.key():
            node.left = self.__delete(node.left, value)
        elif value.key() > node.key():
            node.right = self.__delete(node.right, value)
        else:
            left = node.left
            right = node.right
            if right is None:
                return left

            min_node = self.__find_minimum_root_node(right)
            min_node.right = self.__remove_node_with_min_key(right)
            min_node.left = left
            return self.__balance(min_node)
        return self.__balance(node)

    def delete(self, value: T) -> None:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")

        check = self.find(value)
        if check is None:
            raise KeyNotFoundException("KeyNotFoundException")
        self.root = self.__delete(self.root, value)
        self.length -= 1

    def find(self, value: T) -> Optional[T]:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")

        current_node = self.root
        while current_node.key() != value.key():
            if value.key() < current_node.key():
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node is None:
                return None
        return current_node.data

    def min(self) -> T:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")

        node = self.root
        while node.left is not None:
            node = node.left

        return node.data

    def max(self) -> T:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")

        node = self.root
        while node.right is not None:
            node = node.right

        return node.data

    def __show_tree(self, node) -> None:
        if node is None:
            return

        self.__show_tree(node.left)
        print(node.data.key())
        self.__show_tree(node.right)

    def print(self) -> None:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")
        self.__show_tree(self.root)

    def print_tree(self) -> None:
        result: list[str] = ["AVLTree\n"]
        if not self.is_empty():
            self.__create_str_tree(result, "", self.root, True)
        print("".join(result))

    def __create_str_tree(self, result: list[str], prefix: str,
                          node: Optional[Node[T]], is_tail: bool):
        if node.right is not None:
            new_prefix = prefix
            if is_tail:
                new_prefix += "│   "
            else:
                new_prefix += "    "
            self.__create_str_tree(result, new_prefix, node.right, False)

        result.append(prefix)
        if is_tail:
            result.append("└── ")
        else:
            result.append("┌── ")
        result.append(str(node.key()) + "\n")

        if node.left is not None:
            new_prefix = prefix
            if is_tail:
                new_prefix += "    "
            else:
                new_prefix += "│   "
            self.__create_str_tree(result, new_prefix, node.left, True)

    def insert_from_file(self, datafile: Any) -> None:
        info: list[Optional[str]] = []
        i: int = 0
        student1: Student = Student()
        student2: Student = Student()
        student3: Student = Student()
        student4: Student = Student()
        student5: Student = Student()
        student6: Student = Student()
        student7: Student = Student()
        student8: Student = Student()
        student9: Student = Student()
        student10: Student = Student()
        students: list[Student] = [student1, student2, student3, student4, student5,
                                   student6, student7, student8, student9, student10]

        for el in datafile:
            info.append(el)

        for el in students:
            el.name = str(info[i])
            el.group = int(info[i + 1])
            el.course = int(info[i + 2], 10)
            el.age = int(info[i + 3], 10)
            el.average_mark = float(info[i + 4])
            i += 5
            self.insert(el)

    def __save(self, node, datafile):
        if node is None:
            return

        self.__save(node.left, datafile)
        datafile.write(str(node.data))
        datafile.write('\n')
        self.__save(node.right, datafile)

    def save_info_in_file(self):
        if self.is_empty():
            raise EmptyTreeException('EmptyTreeException')
        datafile = open('your_students.txt', mode='w', encoding='utf-8')
        self.__save(self.root, datafile)
