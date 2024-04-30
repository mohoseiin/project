# id , person , person attack , Target و type work , status
info = [[1,'a','a','c','Meeting','unknown'],[2,'a','a','b','criminal','unknown'],[3,'a','a','a','The driver is a detective',True],
        [1,'b','b','d','not criminal','unknown'],[2,'b',3,'d','fake','unknown'],[3,'b','b','b','not criminal','unknown'],
        [1,'c','c','a','not Meeting','unknown'],[2,'c','c','b','not criminal','unknown'],[3,'c','c','d','driving','unknown'],
        [1,'d',1,'b','fake','unknown'],[2,'d','d','d','not driving','unknown'],[3,'d','d','a','criminal','unknown'],]

true = 6
false = 6

Binary_contradictions = []

for itemx in info:
    match itemx[4]:
        case 'Meeting':

            for itemy in info:
                if itemy[4] == 'not Meeting' and itemx[2] == itemy[3] and itemx[3] == itemy[2]:
                    Binary_contradictions.append([itemx,itemy])

        case 'criminal':

            for itemy in info:
                if itemy[4] == 'not criminal' and itemx[3] == itemy[2] and itemx[3] == itemy[3]:
                    Binary_contradictions.append([itemx,itemy])
    
        case 'driving':

            for itemy in info:
                if itemy[4] == 'not driving' and itemx[3] == itemy[3]:
                    Binary_contradictions.append([itemx,itemy])

        case 'fake':

            for itemy in info:
                if itemx[3] == itemy[1] and itemx[2] == itemy[0]:
                    Binary_contradictions.append([itemx,itemy])

print('\nThere are '+ str(len(Binary_contradictions)) +' contradictions in the statements')

print('so One is right and one is wrong.')

x = 12 - len(Binary_contradictions) * 2

print('So ' + str(x) + ' propositions remain\n')

print('Of these two, the statement that says the thief did not know the car was for the detective is true.Because it is stated in the assumption of the problem. And there is only one statement that is wrong and it says that he is not a thief, but if he is')

print('\nB is imposter')
