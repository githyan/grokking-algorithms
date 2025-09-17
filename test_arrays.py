from typing import Union


class Arrays:

    def __init__(self, max_size: int) -> None:
        self.arrays = [0] * max_size
        self.max_size = max_size
        self.incr_size = 0

    def __getitem__(self, key):
        return self.arrays[key]

    def __setitem__(self, key, value):
        self.arrays[key] = value
        self.incr_size += 1

    def __repr__(self) -> str:
        return f"arrays({self.arrays.arrays[:self.incr_size]})"

    def __len__(self) -> int:
        return self.incr_size
