from typing import TypeVar, Generic, List, Any, Optional

K = TypeVar("K", int, float, bool, str, tuple)
V = TypeVar("V")


class HashNode(Generic[K, V]):
    def __init__(self, key: K, value: V) -> None:
        self.key: K = key
        self.value: V = value


class HashTable(Generic[K, V]):
    def __init__(self) -> None:
        self.__size = 0
        self.__factor = 0.75
        self.__sizes = [
            5, 11, 23, 47, 97, 193, 389, 769, 1543, 3072, 3079, 12289,
            24593, 49157, 98317, 196613, 393241, 786433, 1572869, 3145739,
            6291469, 12582917, 25165843, 50331653, 100663319, 201326611,
            402653189, 805306457, 1610612736, 2147483629
        ]
        self.__sizes_index = 0
        self.__arr: List[Optional[HashNode]] = [None] * self.__sizes[self.__sizes_index]

    @staticmethod
    def __hash_func(key: K) -> int:
        return hash(key)

    def __hash_index(self, key: K) -> int:
        hash_index = self.__hash_func(key) % self.__sizes[self.__sizes_index]
        node = self.__arr[hash_index]

        while node is not None and node.key != key:
            hash_index += 1
            hash_index %= self.__sizes[self.__sizes_index]
            node = self.__arr[hash_index]
        return hash_index

    def __getitem__(self, key: K) -> V:
        if not isinstance(key, (int, float, bool, str, tuple)):
            raise TypeError('key should be immutable')

        node = self.__arr[self.__hash_index(key)]

        if node is not None:
            return node.value
        else:
            raise KeyError(f'there is no item with key {key}')

    def __setitem__(self, key: K, value: V) -> None:
        if not isinstance(key, (int, float, bool, str, tuple)):
            raise TypeError('key should be immutable')

        if self.__sizes[self.__sizes_index] * self.__factor < self.__size:
            self.__increase_array_size()

        self.__insert(key, value)

    def __delitem__(self, key: K) -> None:
        if not isinstance(key, (int, float, bool, str, tuple)):
            raise TypeError('key should be immutable')

        hash_index = self.__hash_index(key)

        if self.__arr[hash_index] is None:
            raise KeyError(f'there is no item with key {key}')

        self.__arr[hash_index] = None

    def __str__(self) -> str:
        def to_string(data: Any) -> str:
            return f"'{data}'" if isinstance(data, str) else f'{data}'

        parts = []
        for node in self.__arr:
            if node is None:
                continue
            parts.append(f'{to_string(node.key)} : {to_string(node.value)}')

        return "{" + ",".join(parts) + "}"

    def __contains__(self, key: K) -> bool:
        if not isinstance(key, (int, float, bool, str, tuple)):
            raise TypeError('key should be immutable')

        return self.__arr[self.__hash_index(key)] is not None

    def __len__(self) -> int:
        return self.__size

    def __increase_array_size(self) -> None:
        self.__sizes_index += 1
        old_arr = self.__arr

        self.__size = 0
        self.__arr = [None] * self.__sizes[self.__sizes_index]

        for i in old_arr:
            if i is None:
                continue
            self.__insert(i.key, i.value)
            del i

        del old_arr

    def __insert(self, key: K, value: V):
        node = HashNode[K, V](key, value)
        hash_index = self.__hash_index(key)

        if self.__arr[hash_index] is None:
            self.__size += 1

        self.__arr[hash_index] = node

    def get(self, key: K) -> Optional[V]:
        if not isinstance(key, (int, float, bool, str, tuple)):
            raise TypeError('key should be immutable')

        node = self.__arr[self.__hash_index(key)]

        return node.value if node is not None else None

    def values(self) -> List[V]:
        arr_values = []
        for node in self.__arr:
            if node is None:
                continue
            arr_values.append(node.value)

        return arr_values

    def keys(self) -> List[K]:
        arr_keys = []
        for node in self.__arr:
            if node is None:
                continue
            arr_keys.append(node.key)

        return arr_keys
