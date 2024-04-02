import turtle

def write_turtle(text):
    tur = turtle.Turtle()
    tur.goto(130, 60)  
    tur.width(3)
    tur.speed(0.5)
    for x in text:
        if x[0] == False:
            tur.pendown()
        else:
            tur.penup()
        if x[1]:
            tur.right(x[2])
        else:
            tur.left(x[2])
        tur.forward(x[3])

    turtle.done()

def vault_unlock():
    write_turtle([(False,True,0,20),(False,True,90,100),(False,True,90,55),(False,True,90,100),
                  (False,True,90,20),(False,True,90,80),(False,False,90,15),(False,False,90,80),
                  (True,False,110,90),(False,False,25,0),(False,False,0,20),(False,True,90,20),
                  (False,False,90,20),(False,False,90,20),(False,False,90,20),(False,True,90,20),
                  (False,False,90,20),(False,False,90,20),(True,False,135,30),(True,False,90,20),
                  (False,True,90,27),(False,True,90,60),(False,False,45,60),(False,True,90,20),
                  (False,True,90,67),(False,True,45,60),(False,False,90,10),(False,True,90,10),
                  (True,True,180,130),(False,True,45,40),(False,False,90,40),(False,False,90,13),
                  (False,False,90,27),(False,True,90,40),(False,True,135,90),(False,False,45,10),
                  (False,False,45,70),(False,False,90,300),(False,False,90,15),(False,False,90,285),
                  (False,True,90,45),(False,True,45,5),(False,True,45,110),(False,False,135,50),
                  (True,False,135,60),(True,True,90,10),(False,True,45,20),(False,False,90,20),
                  (False,False,90,20),(False,False,90,20)])

print('Welcome to question 4')
print('The final answer: at123')
vault_unlock()