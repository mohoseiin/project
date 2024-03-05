money = 0
while True:
    print('I want to deposit money => 1')
    print('I want to withdraw money => 2')
    print('I want to check my balance => 3')
    data = input('get type work:')

    if int(data) == 1:
        moneyy = input('Enter the amount of money :')
        money = money + int(moneyy)

    elif int(data) == 2:
        moneyy = input('Enter the amount of money :')
        if money - int(moneyy) >= 0:
            money = money - int(moneyy)
        else:
            print('The account balance is low')

    elif int(data) == 3:
        print(money)

    else:
        print('format is not true')