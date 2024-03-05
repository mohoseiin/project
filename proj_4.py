print('Fahrenheit to Celsius => 1')
print('Celsius to Fahrenheit => 2')

typework = input('plese enter type convert:')
num = input('plese enter number:')

if int(typework) == 1:
    print((int(num) - 32) / 1.8) 

elif int(typework) == 2:
    print((int(num) * 1.8) + 32)

else:
    print('format is not true')