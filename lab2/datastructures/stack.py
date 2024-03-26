from typing import TypeVar, Generic, Any, Optional
T = TypeVar("T")


class EmptyStackError(Exception):
    pass


class StackNode(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next_ptr: Optional['StackNode'] = None


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.__length = 0
        self.__head: Optional[StackNode[T]] = None

    def __len__(self) -> int:
        return self.__length

    def __lt__(self, other: 'Stack') -> bool:
        return len(self) < len(other)

    def __gt__(self, other: 'Stack') -> bool:
        return len(self) > len(other)

    def __le__(self, other: 'Stack') -> bool:
        return len(self) <= len(other)

    def __ge__(self, other: 'Stack') -> bool:
        return len(self) >= len(other)

    def __add__(self, other: 'Stack') -> 'Stack':
        if self.__head is None:
            return other
        if other.__head is None:
            return self
        if self.__head is not None and other.__head is not None:
            node = self.__head
            while node.next_ptr is not None:
                node = node.next_ptr
            node.next_ptr = other.__head
            return self

    def __str__(self) -> str:
        def to_string(data: Any) -> str:
            return f"'{data}'" if isinstance(data, str) else f'{data}'
        if self.__head is None:
            return "None"
        items = []
        node = self.__head
        items.append(to_string(node.data))
        while node.next_ptr is not None:
            node = node.next_ptr
            items.append(to_string(node.data))
        return "[" + ",".join(items) + "]"

    def is_empty(self) -> bool:
        return self.__length == 0

    def push(self, data: T) -> None:
        node = StackNode[T](data)

        if self.__length == 0:
            self.__head = node
            self.__length += 1
        else:
            node.next_ptr = self.__head
            self.__head = node
            self.__length += 1

    def pop(self) -> T:
        if self.__head is not None:
            node = self.__head
            self.__head = self.__head.next_ptr
            self.__length -= 1
            return node.data
        else:
            raise EmptyStackError('Stack is empty')

    def first(self) -> T:
        if self.__head is not None:
            return self.__head.data
        else:
            raise EmptyStackError('Stack is empty')

    def last(self) -> T:
        if self.__head is not None:
            node = self.__head
            while node.next_ptr is not None:
                node = node.next_ptr
            return node.data
        else:
            raise EmptyStackError('Stack is empty')
