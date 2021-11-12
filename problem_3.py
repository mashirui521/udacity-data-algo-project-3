def mergesort(nums):
    if len(nums) <= 1:
        return nums

    mid_idx = len(nums) // 2

    left = mergesort(nums[:mid_idx])
    right = mergesort(nums[mid_idx:])

    return merge(left, right)


def merge(left, right):
    merged = list()

    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged += left[left_idx:]
    merged += right[right_idx:]

    return merged


def rearrange_digits(nums):
    nums_sorted = mergesort(nums)

    left_digits = str()
    right_digits = str()
    for idx in range(len(nums_sorted)):
        if idx % 2 == 0:
            left_digits += str(nums_sorted[idx])
        else:
            right_digits += str(nums_sorted[idx])

    return [int(left_digits) if left_digits != '' else 0, int(right_digits) if right_digits != '' else 0]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Normal cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Edge cases
test_function([[], []])
test_function([[1], [1]])
