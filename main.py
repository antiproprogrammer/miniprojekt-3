import turtle 

def rita_triangel(t, sida, farg):
    t.pencolor(farg)
    for _ in range(3):
        t.forward(sida)
        t.left(120)