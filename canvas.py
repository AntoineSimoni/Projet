from tkinter import *

points = [[2, 2], [4, 6], [6, 2]]
traits=[[0,1],[1,2],[2,0]]
angle = 30  
taille_cube = 40
hauteur = taille_cube * 20
largeur = taille_cube * 20
def init_canevas():
    for i in range(20):
        canevas.create_line((0,taille_cube*i),(largeur,taille_cube*i), fill="white", dash=(4,4), width = 1)
        canevas.create_line((taille_cube*i,0),(taille_cube*i,hauteur), fill="white", dash=(4,4), width = 1)
    canevas.create_line(change_coo(0,10), change_coo(0,-10), fill="blue", width = 2)
    canevas.create_line(change_coo(10,0), change_coo(-10,0), fill="blue", width = 2)

def change_coo(x, y):
    x1=taille_cube*(x+10)
    y1=hauteur-taille_cube*(y+10)
    return x1,y1

def triangle(points):
    for i in range(3):
        point_0=points[traits[i][0]]
        point_1=points[traits[i][1]]
        canevas.create_line(change_coo(point_0[0],point_0[1]), change_coo(point_1[0],point_1[1]), fill="red", width = 2)

def rotation():
        int(e_angle.get())/180 * 3.14
        r=[[cos(a),-sin(a)],[sin(a),cos(a)]]

fenetre = Tk()
canevas = Canvas(fenetre, width = largeur, height = hauteur, bg="grey")
canevas.grid(row=0, column = 0, columnspan=4)


init_canevas()
triangle(points)
fenetre.mainloop()