import operations

if __name__ == '__main__':

    print('Welcome to this AWSome Calculator!!')

    print('''
    [1] ADD
    [2] SUB
    ''')

    result = None

    operation = int(input('Select operation: '))
    num_a = int(input('Enter number A: '))
    num_b = int(input('Enter number B: '))

    print('----------')
    print('INPUT VALUES')
    print('Operation: ',operation)
    print('Number A: ',num_a)
    print('Number B: ',num_b)

    if operation == 1:
        result = operations.add(num_a,num_b)

    if operation == 2:
        result = operations.sub(num_a,num_b)

    print('----------')
    print('OUTPUT VALUES')
    print('Result: ',result)
