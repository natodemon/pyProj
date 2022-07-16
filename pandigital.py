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

    return num_set


val = input('Please enter D: ')

pandigitals = numSetGen(int(val))
print(len(pandigitals))