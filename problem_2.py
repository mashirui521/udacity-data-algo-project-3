def binary_search(nums, target, begin_idx, end_idx):
    if begin_idx > end_idx:
        return -1

    mid_idx = (begin_idx + end_idx) // 2
    mid_value = nums[mid_idx]

    if mid_value == target:
        return mid_idx

    left_idx = binary_search(nums, target, begin_idx, mid_idx - 1)
    right_idx = binary_search(nums, target, mid_idx + 1, end_idx)

    return max(left_idx, right_idx)


def rotated_array_search(nums, target):
    return binary_search(nums, target, 0, len(nums) - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Normal cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge cases
test_function([[], -1])
test_function([[1], 0])
