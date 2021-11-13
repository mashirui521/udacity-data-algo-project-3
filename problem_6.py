import random


def get_min_max(nums):
    if len(nums) == 1:
        return nums[0], nums[0]

    min_value = None
    max_value = None
    for idx in range(len(nums)-1):
        value = nums[idx]
        value_next = nums[idx+1]

        if value > value_next:
            if min_value is None or min_value > value_next:
                min_value = value_next
            if max_value is None or max_value < value:
                max_value = value
        else:
            if min_value is None or min_value > value:
                min_value = value
            if max_value is None or max_value < value_next:
                max_value = value_next

    return min_value, max_value


def test_function(test_case):
    print(test_case)
    if get_min_max(test_case) == (min(test_case), max(test_case)):
        print("Pass")
    else:
        print("Fail")


# Normal cases
test_function([4, 6, 2, 5, 9, 8])
test_function([4, -4, -100, 5, 9, 8])

# Edge cases
test_function([4])
print(get_min_max([])) # Output: (None, None)
