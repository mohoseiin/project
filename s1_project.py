
def decrypt_clue(text):
    file = open(text, "r")

    allKeywords = ['False','class','from','or','None','continue','global','pass','True','def','if','raise','and','del','import','return','as','elif','in','try','assert','else','is','while','async','except','lambda','with','await','finally','nonlocal','yield','break','for','not']
    Words_that_can_be_similar = []
    status = 0
    sta = True
    success = ''
    y = 0
    loc = 0
    sds = 0
    data = file.read()
    data = data.replace(" ", "")

    for y in allKeywords:
        status = len(y)
        loc = 0
        for x in data:
            if sta:
                if y[0] == x:
                    success = x
                    sta = False
                    sds = loc
            else:
                if len(success) == status:
                    Words_that_can_be_similar.append((sds,success))
                    sta = True
                    success = ''
                    sds = 0
                else:
                    success = success + x
            loc += 1
    out = []
    out_final = []
    for y in allKeywords:
        for x in Words_that_can_be_similar:
            if x[1] == y:
                out.append(x)

    for y in range(len(data)):
        for x in out:
            if y == x[0]:
                out_final.append(x[1])
    print(out_final)

print('Welcome to question 1')
decrypt_clue("mysterious.txt")