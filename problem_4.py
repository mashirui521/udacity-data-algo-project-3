def sort_012(nums):
    next_0_idx = 0
    front = 0
    next_2_idx = len(nums) - 1

    while front <= next_2_idx:
        if nums[front] == 0:
            nums[front] = nums[next_0_idx]
            nums[next_0_idx] = 0
            next_0_idx += 1
            front += 1
        elif nums[front] == 2:
            nums[front] = nums[next_2_idx]
            nums[next_2_idx] = 2
            next_2_idx -= 1
        else:
            front += 1


def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Normal cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
              2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# Edge cases
test_function([])
test_function([2])