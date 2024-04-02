import ast

def puzzles_solve(puzzles):
    # get data
    data = []
    with open(puzzles) as file:
        data = file.readlines()
    file.close()
    # get data

    # delete \n
    loc = 0
    for x in data:
        data[loc] = x.strip()
        loc += 1
    # delete \n
    
    loc = 0
    # convert type
    for x in data:
        if x.isnumeric():
            data[loc] = int(x)
        elif x == 'None':
            data[loc] = None

        elif x[0] == "[" and x[len(x)-1] == "]":
            data[loc] = ast.literal_eval(x)

        elif x[0] == "{" and x[len(x)-1] == "}":
            data[loc] = ast.literal_eval(x)

        elif x[0] == '-':
            data[loc] = float(x)

        elif x[0] == '0':
            data[loc] = float(x)

        elif x == 'True' or x == 'False':
            if x == 'True':
                data[loc] = True
            else:
                data[loc] = False
        else:
            if x[0] == "'" and x[len(x)-1] == "'" or x[0] == '"' and x[len(x)-1] == '"':
                data[loc] = ''
                for y in x:
                    if y == "'" or y == '"':
                        continue
                    data[loc] = data[loc] + y
        loc += 1
    # convert type
        
    # convert to bool data
    loc = 0
    for x in data:
        data[loc] = bool(x)
        loc += 1
    print(data)
    #convert to bool data

print('Welcome to question 2')
puzzles_solve("puzzles.txt")