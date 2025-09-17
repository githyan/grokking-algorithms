from UnsortedArray import UnsortedArray
from SortedArray import SortedArray


if __name__ == "__main__":

    arr = UnsortedArray(6)

    arr.insert(3)
    arr.insert(4)
    arr.insert(5)
    arr.insert(6)
    arr.insert(7)

    arr.traverse(print)

    sorted = SortedArray(6)
    sorted.insert(7)
    sorted.insert(10)
    sorted.insert(8)
    sorted.insert(9)

    print("sorting array")
    sorted.traverse(print)

    # print("min and max value at indexed")
    # arr.min_max_array(print)
    # # Output of array is inserted
    # print("array is inserted :")
    # arr.traverse(print)
    #
    # # Removing array by index
    # print("array is removing :")
    # arr.remove(1)
    # arr.traverse(print)
    #
    # print("min and max value at indexed")
    # arr.min_max_array(print)
