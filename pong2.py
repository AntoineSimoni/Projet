from tkinter import *
Joueur_1 = 0
Joueur_2 = 0

tk = Tk()
tk.title("J1 : "+str(Joueur_1)+"  ||  J2 : "+str(Joueur_2))

X = 1080
Y = 720
Speed = 20
element_color = "white"
background_color = "black"
play = False

J1_haut = "<z>"
J1_bas ="<s>"
J2_haut = "<Up>"
J2_bas = "<Down>"

class pong :
    def __init__(self):
        self.tx = 20
        self.ty = 20
        self.r1 = Raquette(30, Y/2-self.ty/2,J1_haut,J1_bas)
        self.r1 = Raquette(X-30, Y/2-self.ty/2,J2_haut,J2_bas)


class Raquette :
    def __init__(self, x, y, haut,bas):
        self.x = x
        self.y = y
        self.tx = 10
        self.ty = 50
        self.vitesse = 10
        self.haut = haut
        self.bas = bas
        self.ra = terrain.create_rectangle(self.x, self.y, self.x+self.tx, self.y+self.ty, fill=COLOR)
        tk.bind_all(self.haut, self.monter)
        tk.bind_all(self.bas, self.descendre)

    def monter(self, event):
        self.deplacer(-self.vitesse)
    def descendre(self, event):
        self.deplacer(self.vitesse)



    def deplacer (self, dy):
        if PLAY :
            self.y += dy
            if self.y < 0:
                self.y = 0
            if self.y > Y - self.ty:
                self.y = Y - self.ty
            self.raffraichir()


    def placer(self, x, y):
        self.x = x
        self.y = y
        terrain.coords(self.ra, self.x, self.y, self.x + self.tx, self.y + self.ty)


    def raffraichir(self):
        terrain.coords(self.ra, self.x, self.y, self.x + self.tx, self.y + self.ty)



while play:


    tk.mainloop()