from core import Array


class DynamicArrays:
    def __init__(self, initial_capacity: int = 1, typecode: str = "l") -> None:
        self._arrays = Array(initial_capacity, typecode)
        self._capacity = initial_capacity
        self._typecode = typecode
        self._size = 0

    def grows_capacity(self) -> None:
        old_array = self._arrays
        self._arrays = Array(self._capacity * 2, self._typecode)
        self._capacity *= 2

        for i in range(self._size):
            self._arrays[i] = old_array[i]

    def add(self, value: int) -> None:
        if self._size >= self._capacity:
            self.grows_capacity()

        self._arrays[self._size] = value
        self._size += 1

    def insert(self, index: int, value: int) -> None:

        if self._size >= self._capacity:
            self.grows_capacity()

        self._arrays[index] = value
        self._size += 1

    def isEmpty(self) -> bool:
        return self._size == 0

    def __repr__(self) -> str:
        return f"{self._arrays}"
