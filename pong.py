from tkinter import *
from random import randrange
J1 = 0
J2 = 0

tk = Tk()
tk.title("J1 : "+str(J1)+"  |||  J2 : "+str(J2))


X = 800 #taille de la fenetre en X
Y = 420 # taille de la fenetre en Y
VITESSE = 8 #la vitesse de deplacement de la balle
COLOR = "white"
BGCOLOR = "black"

PLAY = False #est-ce qu'on est en train de jouer

def JEUX():
    class Pong : # la classe gerant la balle de pong
        def __init__(self): #le constructeur de la balle de pong
            global men
            self.tx = 10 # taille en X de la balle
            self.ty = 10 # taille en Y de la balle
            self.r1 = Raquette(30, Y/2-self.ty/2, "<z>","<s>") #on recup les deux raquettes pour plus tard check la hitbox
            self.r2 = Raquette(X-30, Y/2-self.ty/2, "<Up>","<Down>")
            self.dummy = randrange(0, 100) #une valeur aleatoire pour savoir vers qui va la balle

            self.x = X/2 - self.tx/2 #on place la balle au centre de l'ecran
            self.y = Y/2 - self.ty/2
            self.dx = 0 # on fixe le deplacement horizontal a 0, elle ira donc a plat et ne bougera pas
            if self.dummy < 50 : #si le dummy est < 50, la balle va a gauche sinon a droite
                self.dx = -1
            else :
               self.dx = 1

            self.dy = float(randrange(-100,100))/100 # on defini si la balle va monter ou descendre

            self.balle = terrain.create_rectangle(self.x, self.y, self.x + self.tx, self.y + self.ty, fill=COLOR)
		    		#on creer un rectangle qui va etre rempli avec une couleur
            self.deplacer()
		    		#on deplace la balle d'un cran
            tk.bind_all("<Return>", self.pause) #si return est press, met le jeu sur pause

        def pause(self, event): # met le jeu en pause ou non
            global PLAY, men
            if PLAY :
                PLAY = False
            else :
                PLAY = True

        def raffraichir(self): #on rafraichi la position de la bougie
            global men
            terrain.coords(self.balle, self.x, self.y, self.x+self.tx, self.y+self.ty)

        def deplacer(self):
            global J1, J2, PLAY, men
            if PLAY :
                self.x += self.dx * VITESSE # on deplace la balle sur dx, defini plus haut, a une vitesse donnée
                self.y += self.dy * VITESSE # on deplace la balle sur dy, defini plus haut, a une vitesse donnée

                if self.y <= 0 or self.y >= Y-self.ty : #si on atteint un cote haut ou bas de l'ecran, on inverse la direction de dy
                    self.dy =- self.dy
                if self.r1.y <= self.y + self.ty and self.r1.y + self.r1.ty >= self.y : #si on est entre le haut et le bas de la raquette 1
                    if self.x <= self.r1.x + self.r1.tx and not self.x + self.tx <= self.r1.x: #si on touche sur l'axe X la raquette 1
                        self.dx =- self.dx #on inverse la direction de la balle sur X
                        self.dy = float(randrange(-100, 100))/100 #defini une nouvelle direction aleatoire sur Y

                if self.r2.y <= self.y + self.ty and self.r2.y + self.r2.ty >= self.y : # meme chose sur la raquette 2
                    if self.x + self.tx >= self.r2.x and not self.x >= self.r2.x + self.r2.tx :
                        self.dx =- self.dx
                        self.dy = float(randrange(-100, 100))/100

                if self.x + self.tx < 0 : #si on touche la partie de droite de l'ecran (joueur 1 a perdu)
                    self.x = X/2 - self.tx/2 #on reset la balle
                    self.y = Y/2 - self.ty/2
                    J2 += 1 #plus un point pour le J2
                    self.dx =- self.dx  #on reset les directions 
                    self.dy = float(randrange(-100, 100))/100
                    self.r1.placer(30, Y/2-self.ty/2) #on replace les deux raquettes
                    self.r2.placer(X-30, Y/2-self.ty/2)
                    PLAY = False #on met le jeu en pause avant de redemarrer 


                if self.x+self.tx>X : #meme chose mais pour le joueur 2 qui a perdu
                    self.x = X/2 - self.tx/2
                    self.y = Y/2 - self.ty/2
                    J1 += 1
                    self.dx =- self.dx
                    self.dy = float(randrange(-100, 100))/100
                    self.r1.placer(30, Y/2-self.ty/2)
                    self.r2.placer(X-30, Y/2-self.ty/2)
                    PLAY = False



                tk.title("J1 : "+str(J1)+"  |||  J2 : "+str(J2)) #on change le titre de la fenetre pour servir de score
                self.raffraichir() #on rafraichi l'ecran apres avoir bouger la balle

            tk.after(30, self.deplacer) #on refait le deplacement tout les 30 millisecondes


    class Raquette :
        def __init__(self, x, y, haut,bas):
            global men
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

        def monter(self, event): #la fonction pour monter
            global men
            self.deplacer(-self.vitesse) #on se deplace de - la vitesse, probablement vers le haut)
        def descendre(self, event): #la fonction pour descendre
            global men
            self.deplacer(self.vitesse) #on se deplace de + la vitesse, pour descendre)



        def deplacer (self, dy): #fonction deplacer
            global men
            if PLAY : #si play est actif
                self.y += dy # tu deplaces le player de dy (qu'il soit positif ou negatif)
                if self.y < 0: #si le nouveau self.y est inferieur a 0, on est sorti de la fenetre)
                    self.y = 0 #on le remet donc dans la fenetre
                if self.y > Y - self.ty: # si a l'inverse on sort de l'autre cote
                    self.y = Y - self.ty #on le remet dans le bon endroit
                self.raffraichir() #on rafraichi l'ecran pour deplacer visuellement le joueur


        def placer(self, x, y):
            global men
            self.x = x
            self.y = y
            terrain.coords(self.ra, self.x, self.y, self.x + self.tx, self.y + self.ty)


        def raffraichir(self):
            global men
            terrain.coords(self.ra, self.x, self.y, self.x + self.tx, self.y + self.ty)

def Menuu() :
    menu = Tk()
    menu.title("[Pong]")
    menu.geometry("260x90")
    ButtonJouer = Button(menu, text ="   Play   ", command = JEUX)
    ButtonJouer.pack(padx = 5, pady = 5)
    ButtonQuitter = Button(menu, text ="   Exit    ", command = menu.destroy)
    ButtonQuitter.pack(padx = 5, pady = 5)
    return menu
 


if __name__ == '__main__':
    tk.resizable(width=False, height=False)
    terrain = Canvas(tk, bg=BGCOLOR, height=Y, width=X)
    terrain.pack()
    menu2 = Menuu()
    menu2.mainloop()
    tk.mainloop()

if __name__ == '__main__':
    tk.resizable(width=False, height=False)
    terrain = Canvas(tk, bg=BGCOLOR, height=Y, width=X)
    terrain.pack()
    jeu = Pong()
    tk.mainloop()