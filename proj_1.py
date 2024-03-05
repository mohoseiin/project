def convert(i):
    if i.isdigit():
        return int(i)
    elif ',' in data:
        return i.split(',')
    elif i == "true" or i == "True" or i == "false" or i == "False":
        if i == "true" or i == "True":
            return True
        else:
            return False
    else:
        return data


data = input('plese enter input')
print(type(convert(data)))