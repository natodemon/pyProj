def isPandigital(num):
    num_digits = str(num)

    num_list = []

    for digit in num_digits:
        if digit in num_list:
            return False
        else:
            num_list.append(digit)

    regular_pan = []
    for x in range(1, len(num_digits)+1):
        regular_pan.append(str(x))

    if sorted(num_list) == regular_pan:
        return True
    else:
        return False

def numSetGen(max_val):
    num_set = set()
    num_set.add(1)
    for x in range(2, max_val+1):
        #print(i)
        if isPandigital(x):
            num_set.add(x)

    return len(num_set)

def test_numSetGen():
    print(f'Running tests, you may enter your own test values later\n')
    test_vals = [10, 22, 350]
    for val in test_vals:
        print(f'Input value: {val}')
        print(f'Result: {numSetGen(val)}')


test_numSetGen()

val = input(f'\nPlease enter D: ')

print(numSetGen(int(val)))