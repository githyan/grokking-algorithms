from core import Array


class UnsortedArray:
    def __init__(self, max_size: int, typecode: str = "l") -> None:
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0

    def __len__(self):
        return self._array

    def insert(self, new_entry: int) -> None:
        if self._size >= len(self._array):
            raise ValueError("The array is already full")
        self._array[self._size] = new_entry
        self._size += 1

    def remove(self, index: int) -> None:
        if index == 0:
            raise ValueError("Remove from an empty array")
        elif index < 0 or index >= self._size:
            raise ValueError(f"index {index} out of range", index)
        else:
            self._array[index] = self._array[self._size - 1]
            self._size -= 1

    def find(self, target: int):
        for index in range(0, self._size):
            if target == self._array[index]:
                return index

        return None

    def min_max_array(self, callback):
        array = self._array
        min_value, max_value = 0, 0

        for index in range(self._size):
            if array[index] < array[min_value]:
                min_value = index
            elif array[index] > array[max_value]:
                max_value = index

        callback(
            f"min_value: ({min_value}, {array[min_value]}), max_value: ({max_value}, {array[max_value]})"
        )

    def traverse(self, callback):
        sequences = [self._array[index] for index in range(self._size)]
        callback(sequences)
