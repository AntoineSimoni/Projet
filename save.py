from tkinter import *


taille_cube = 25
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

def triangle():
    point_0 = [2, 2]
    point_1 = [4, 6]
    point_2 = [6, 2]
    canevas.create_line(change_coo(point_0[0],point_0[1]), change_coo(point_1[0],point_1[1]), fill="red", width = 2)
    canevas.create_line(change_coo(point_1[0],point_1[1]), change_coo(point_2[0],point_2[1]), fill="red", width = 2)
    canevas.create_line(change_coo(point_0[0],point_0[1]), change_coo(point_2[0],point_2[1]), fill="red", width = 2) 


fenetre = Tk()
canevas = Canvas(fenetre, width = largeur, height = hauteur, bg="grey")
canevas.grid(row=0, column = 0, columnspan=4)


init_canevas()
triangle()
fenetre.mainloop()