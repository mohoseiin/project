typework = input('plese enter The type of operation : sum , difference , multiple , divide')
num1 = input('plese enter number 1')
num2 = input('plese enter number 2')

if typework == 'sum':
    print(int(num1) + int(num2))

elif typework == 'difference':
    print(int(num1) - int(num2))

elif typework == 'multiple':
    print(int(num1) * int(num2))

elif typework == 'divide':
    print(int(num1) / int(num2))

else:
    print('format operation is not true')