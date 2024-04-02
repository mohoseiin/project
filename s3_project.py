import random
import time

def calculate_magic_numbers(start,end):
    x = random.uniform(0, 1)
    x = x * (end-start) + start
    print("%.2f" % x)

def numbers_exam():

    binary = ""
    decimal = 0
    for i in range(4):
        x = random.randint(0, 1)
        binary += str(x)
        if i == 0:
            decimal = decimal + x * 8
        elif i == 1:
            decimal = decimal + x * 4
        elif i == 2:
            decimal = decimal + x * 2
        else:
            decimal = decimal + x

    print('You have 20 seconds to convert the binary number '+ binary +' to decimal',end='\n')

    start_time = time.time()

    data = input("Decimal:")

    end_time = time.time()

    if end_time - start_time > 20:
        print('Your time is up and you failed\n')
    else:
        if int(data) == decimal:
            print('You are successful\n')
        else:
            print('You did not succeed  Correct decimal ' + str(decimal))

def check_pass():
    
    punctuation = ['.','?','!',',',';',':','_','-','(',')','[',']','{','}','@','#','$','%','^','&','*','/']
    big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    user = ()
    y = list(user)

    us = 1
    print('Enter the user name and password and type the word exit to exit')

    while True:
        name = input('name user ' + str(us) + ' :\n')
        if name == 'exit':
            break

        password = input('password user ' + str(us) + ' :\n')
        if password == 'exit':
            break

        y.append((name,password))
        us += 1

    user = tuple(y)
    print('Users whose password was correct:\n')
    for x in user:
        if len(x[1]) >= 8:
            access_text_big = False
            access_text_small = False
            access_punctuation = False
            for y in x[1]:
                for z in punctuation:
                    if y == z:
                        access_punctuation = True
                for z in small:
                    if y == z:
                        access_text_small = True
                for z in big:
                    if y == z:
                        access_text_big = True
            if access_text_big and access_text_small and access_punctuation:
                print('  user name : ' + x[0] + '\n' + '  password : ' + x[1] +'\n')

print('Welcome to question 3')

while True:

    data = input(' 1 => Making the magic number ("calculate_magic_numbers")\n 2 => The question of converting binary number to decimal("numbers_exam")\n 3 => Checking the difficulty of users passwords("check_pass") \n')

    if int(data) == 1:

        print('Specify the numeric range\n')
        x = input('Starting from the number: ')
        y = input('\nend to number: ')

        if x.isnumeric and y.isnumeric:
            if int(x) < int(y):
                calculate_magic_numbers(int(x),int(y))
            else:
                print('The entered numbers are not correct')
        else:
            print('Please enter a number')


    elif int(data) == 2:
        numbers_exam()

    elif int(data) == 3:
        check_pass()

    else:
        print('This number is not supported')