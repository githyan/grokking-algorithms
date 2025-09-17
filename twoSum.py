def twoSum(nums: list[int], target: int) -> list[int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] in hash_map:
            return [hash_map[nums[i]], i]
        else:
            hash_map[target - nums[i]] = i

    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + j == target:
    #             return [i, j]
    return [x for x in range(len(nums)) if target == nums[x]]


if __name__ == "__main__":
    arrays = [2, 7, 11, 15]
    print(twoSum(nums=arrays, target=9))
