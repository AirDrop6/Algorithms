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


class Car(Key):
    mark: str
    VIN: str
    engine_capasity: int
    price: int
    average_speed: int

    def key(self) -> int:
        return self.price

    def __str__(self):
        return f'Car(mark:{self.mark},' \
               f' VIN:{self.VIN}, ' \
               f'engine_capasity:{self.engine_capasity}, ' \
               f'{self.price}$, ' \
               f'average_speed:{self.average_speed} km/h)'


class Node(Generic[T], Key):
    data: T
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def key(self) -> int:
        return self.data.key()


class BinarySearchTree(Generic[T]):

    def __init__(self):
        self.length: int = 0
        self.root: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.length == 0

    def get_size(self) -> int:
        return self.length

    def insert(self, value: T) -> None:
        new_node: Node[T] = Node()
        new_node.data = value

        if self.root is None:
            self.root = new_node
            self.length += 1
        else:
            current_node = self.root
            while True:
                if current_node.key() == new_node.key():
                    return

                elif current_node.key() > new_node.key():
                    if current_node.left is None:
                        current_node.left = new_node
                        self.length += 1
                        return
                    else:
                        current_node = current_node.left

                elif current_node.key() < new_node.key():
                    if current_node.right is None:
                        current_node.right = new_node
                        self.length += 1
                        return
                    else:
                        current_node = current_node.right

    def find(self, value: T) -> Optional[T]:
        if self.is_empty():
            raise EmptyTreeException('Your tree is empty')

        current_node = self.root

        while current_node.key() != value.key():
            if current_node.key() > value.key():
                current_node = current_node.left

            elif current_node.key() < value.key():
                current_node = current_node.right

            if current_node is None:
                return None

        return current_node.data

    def min(self) -> T:
        if self.is_empty():
            raise EmptyTreeException("Your tree is empty")

        current_node = self.root

        while current_node.left is not None:
            current_node = current_node.left

        return current_node.data

    def max(self) -> T:
        if self.is_empty():
            raise EmptyTreeException("Your tree is empty")

        current_node = self.root

        while current_node.right is not None:
            current_node = current_node.right

        return current_node.data

    @staticmethod
    def __first_type_del(current, parent):
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None

    @staticmethod
    def __second_type_del(current, parent):
        if parent.left == current:
            if current.left is None:
                parent.left = current.right
            elif current.right is None:
                parent.left = current.left
        elif parent.right == current:
            if current.left is None:
                parent.right = current.right
            elif current.right is None:
                parent.right = current.left

    def __third_type_del(self, current):
        new_node = current.right
        parent_new_node = current
        while new_node.left is not None:
            parent_new_node = new_node
            new_node = new_node.left
        current.data = new_node.data
        self.__second_type_del(new_node, parent_new_node)

    def delete(self, value: T) -> None:
        if self.is_empty():
            raise EmptyTreeException('Your tree is empty')

        current_node = self.root
        parent_node = self.root

        while current_node.key() != value.key():
            parent_node = current_node

            if current_node.key() > value.key():
                current_node = current_node.left

            if current_node.key() < value.key():
                current_node = current_node.right

            if current_node is None:
                raise KeyNotFoundException('Key is not found')

        if current_node.left is None and current_node.right is None:
            self.__first_type_del(current_node, parent_node)
            self.length -= 1

        elif current_node.left is None or current_node.right is None:
            self.__second_type_del(current_node, parent_node)
            self.length -= 1

        else:
            self.__third_type_del(current_node)
            self.length -= 1

    def __show_tree(self, node: Optional[Node]):
        if node is None:
            return

        self.__show_tree(node.left)
        print(node.data.key())
        self.__show_tree(node.right)

    def print(self) -> None:
        if self.is_empty():
            raise EmptyTreeException('Your tree is empty')

        self.__show_tree(self.root)

    def print_tree(self) -> None:
        result: list[str] = ["BinarySearchTree\n"]
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
        car1: Car = Car()
        car2: Car = Car()
        car3: Car = Car()
        car4: Car = Car()
        car5: Car = Car()
        car6: Car = Car()
        car7: Car = Car()
        car8: Car = Car()
        car9: Car = Car()
        car10: Car = Car()
        cars: list[Car] = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]

        for el in datafile:
            info.append(el)

        for el in cars:
            el.mark = str(info[i])
            el.VIN = str(info[i + 1])
            el.engine_capasity = int(info[i + 2], 10)
            el.price = int(info[i + 3], 10)
            el.average_speed = int(info[i + 4])
            i += 5
            self.insert(el)

    def __save(self, node: Optional[Node], datafile: Any) -> None:
        if node is None:
            return

        self.__save(node.left, datafile)
        datafile.write(str(node.data))
        datafile.write('\n')
        self.__save(node.right, datafile)

    def save_info_in_file(self) -> None:
        if self.is_empty():
            raise EmptyTreeException('EmptyTreeException')

        datafile: Any = open('your_cars.txt', mode='w', encoding='utf-8')
        self.__save(self.root, datafile)

if __name__ == "__main__":
    car = Car()
    car.price = 10
    print(car.key())