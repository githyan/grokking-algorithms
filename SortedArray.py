from typing import TypeVarTuple, Union
from core import Array


class SortedArray:
    def __init__(self, max_size: int, typecode: str = "l") -> None:
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> Union[float, int]:
        if index < 0 or index >= self._size:
            raise IndexError(f"Index out of bound: {index}")
        return self._array[index]

    def __iter__(self):
        for i in range(self._size):
            yield self._array[i]

    def __repr__(self) -> str:
        return f"SortedArray({self._array._array[:self._size]})"

    def binary_search(self, target: int) -> None:
        left: int = 0
        right: int = self._size - 1

        while left <= right:
            mid_index: int = (left + right) // 2
            mid_val: int = self._array[mid_index]
            if mid_val == target:
                return mid_index
            elif mid_val < target:
                left = mid_index + 1
            else:
                right = mid_index - 1

        return None

    def linear_search(self, target: int) -> int:
        for i in range(self._size):
            if self._array[i] == target:
                return i
            elif self._array[i] > target:
                return -1

        return -1

    def insert(self, value: Union[int, float]) -> None:
        if self._size >= self._max_size:
            raise ValueError(
                f"The array is already full, maximum size :{self._max_size}"
            )

        for i in range(self._size, 0, -1):
            if self._array[i - 1] <= value:
                self._array[i] = value
                self._size += 1
                return
            else:
                self._array[i] = self._array[i - 1]

        self._array[0] = value
        self._size += 1

    def delete(self, target: int):
        index = self.linear_search(target)

        if index is None:
            raise ValueError(
                f"Unable to delete this element({index}) because it's not inside of array"
            )

        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1
