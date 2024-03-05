import turtle

size = input('plese enter size sharp:')
color = input('plese enter color sharp: red , greed , blue , yellow')

tur = turtle.Turtle()
tur.shape('turtle')

if (color == 'red' or color == 'greed' or color == 'yellow' or color == 'blue') and size.isnumeric :

    tur.color(color)
    for i in range(4):
        tur.forward(int(size))
        tur.right(90)
        
    turtle.done()
else:
    print('format is not true')
