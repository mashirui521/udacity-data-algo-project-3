import math

def square_root(target):

    if target == 0:
        return 0

    if target == 1:
        return 1

    if target < 0 or not isinstance(target, int):
        raise ValueError('target must be positive integer') 

    value_begin = 0
    value_end = target

    while value_begin < value_end:
        value_mid = math.floor((value_begin + value_end)/2)
        
        if value_begin == value_mid:
            break

        current = value_mid**2
        if current > target:
            value_end = value_mid
        elif current < target:
            value_begin = value_mid
        else:
            break

    return value_mid

print('Pass' if square_root(36) == 6 else 'Fail')
print('Pass' if square_root(27) == 5 else 'Fail')
print('Pass' if square_root(0) == 0 else 'Fail')
print('Pass' if square_root(1) == 1 else 'Fail')

try:
    square_root(-1)        # ValueError: target must be positive integer
except ValueError as e:
    print(e)

try:
    square_root(2.456)     # ValueError: target must be positive integer
except ValueError as e:
    print(e)