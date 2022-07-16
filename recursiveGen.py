def algoDriver(n, counter):
    counter+=1
    if n == 1:
        return counter
    elif (n % 2) == 0:
        return algoDriver((n/2), counter)
    else:
        return algoDriver((3*n+1), counter)

def findY(max_val):
    length, val_y = 0,0

    for x in range(1, max_val+1):
        chain_len = algoDriver(x, counter=0)
        if chain_len >= length:
            length = chain_len
            val_y = x
    
    return val_y

def genOutputList(n_values):
    y_list = []
    for n in n_values:
        y_list.append(findY(n))
    
    return y_list

def test_genOutputList():
    print('Starting test. You may enter your own test values after')
    test_vals = [
        [5,10],
        [15,25],
        [65,93]
    ]
    for values in test_vals:
        print(f'Input values: {values}')
        print(f'Result: {genOutputList(values)}')

test_genOutputList()

values = input(f'\nInput your N values as a comma separated list please: ')

n_list = values.split(",")
n_list = [int(i) for i in n_list]

print(genOutputList(n_list))