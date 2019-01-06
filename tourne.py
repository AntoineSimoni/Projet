from tkinter import *
from math import sin, cos, sqrt


t_cube = 25 
largeur = t_cube*20
hauteur = t_cube*0
angle = 30
point_0 = [2, 2] 
point_1 = [4, 6]
point_2 = [6, 2]

def init_canevas ():
    for i in range(20):
        canevas.create_line(0, (t_cube*i),(largeur,t_cube*i), fill="white" ,dash=(4,4),width=2)
        canevas.create_line((t_cube*i,0),(t_cube*i, hauteur), fill="white" ,dash=(4,4),width=2)
    canevas.create_line(change_coo(10 , 0),change_coo(-10 , 0), fill="blue", width="2")
    canevas.create_line(change_coo(0, 10),change_coo(0,-10), fill="blue", width="2")

def triangle ():
    canevas.create_line(change_coo(point_0[0], point_0[1]),change_coo(point_1[0],point_1[1]), fill="red",width="2")
    canevas.create_line(change_coo(point_1[0], point_1[1]),change_coo(point_2[0],point_2[1]), fill="red",width="2")
    canevas.create_line(change_coo(point_2[0], point_2[1]),change_coo(point_0[0],point_0[1]), fill="red",width="2")

def change_coo(x, y):
    x1 = t_cube * (x+10)
    y1 = hauteur-t_cube * (y+10)
    return x1, y1



def rotation (point, point2):

    rx1 = point[0] * (sqrt(3)/2) + point[1] * (-1/2)
    ry1 = point[0] * (1/2) + point[1] * (sqrt(3)/2)

    rx2 = point2[0] * (sqrt(3)/2) + point2[1] * (-1/2)
    ry2 = point2[0] * (1/2) + point2[1] * (sqrt(3)/2)

    canevas.create_line(change_coo(rx1, ry1),change_coo(rx2, ry2), fill="green",width="2")





fenetre = Tk()
canevas= Canvas(fenetre,width=largeur, height= hauteur, bg= 'grey')
canevas.grid(row=0, column= 0,columnspan = 4)



init_canevas()
triangle()

rotation(point_0, point_1)
rotation(point_1, point_2)
rotation(point_2, point_0)

fenetre.mainloop()

