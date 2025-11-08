from core import Array


class DynamicArrays:
    def __init__(self, initial_capacity: int = 1, typecode: str = "l") -> None:
        self._arrays = Array(initial_capacity, typecode)
        self._capacity = initial_capacity
        self._typecode = typecode
        self._size = 0

    def grows_capacity(self) -> None:
        """
        Menambahkan kapasitas ukuran pada fundamental array statis.

        Returns:
            None
        Langkah Prosedural:
            cheking kontrol pada ukuran _size
            membuat array baru dengan kapasitas dikalikan 2
            iterasi array baru untuk membangun kerangka array sesuai dengan ukuran _size
        """
        assert self._size == self._capacity
        old_array = self._arrays
        self._arrays = Array(self._capacity * 2, self._typecode)
        self._capacity *= 2

        for i in range(self._size):
            self._arrays[i] = old_array[i]

    def halve_size(self):

        assert self._capacity > 1 and self._size <= self._capacity / 4
        old_array = self._arrays
        self._arrays = Array(self._capacity // 2, self._typecode)
        self._capacity //= 2
        for i in range(self._size):
            self._arrays[i] = old_array[i]

    def add(self, value: int) -> None:
        """
        Fungsi operator menambahkan array

        Returns:
            None
        Parameter:
            integer value
        Langkah Prosedural:
            _size akan bertambah sesuai dengan iterasi pada array baru. Jika mempunyai nilai yang sama dengan kapasitas akhir array,
            maka fungsi grows_capacity() ditangkap agar menambahkan ukuran size array menjadi 2x lipat.
            membuat array baru untuk diisi nilai berdasarkan pada parameter integer value.
        """
        if self._size >= self._capacity:
            self.grows_capacity()

        self._arrays[self._size] = value
        self._size += 1

    def insert(self, index: int, value: int) -> None:

        if self._size >= self._capacity:
            self.grows_capacity()

        self._arrays[index] = value
        self._size += 1

    def find(self, target: int):
        left: int = 0
        right: int = self._size - 1

        while left <= right:
            mid_index: int = (left + right) // 2
            mid_arrays = self._arrays[mid_index]

            if mid_arrays == target:
                return mid_index
            elif mid_arrays < target:
                left = mid_index + 1
            else:
                right = mid_index - 1

    def delete(self, target: int):

        index = self.find(target)

        if index is None:
            raise ValueError(
                f"Unable to delete element {target}: the entry is not in the array"
            )

        for i in range(index, self._size - 1):
            self._arrays[i] = self._arrays[i + 1]
        self._size -= 1

        if self._capacity > 1 and self._size <= self._capacity / 4:
            self.halve_size()

    def isEmpty(self) -> bool:
        return self._size == 0

    def __iter__(self):
        for index in range(self._size):
            yield self._arrays[index]

    def __repr__(self) -> str:
        return f"{self._arrays}"
        # return f"{[self._arrays[x] for x in range(self._size)]}"
