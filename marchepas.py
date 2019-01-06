

    def bonus(self):
            global X,Y
            tk.after(1000)
            self.bul = randrange(0,3,1)
            if self.bul == 0:
                bul_x_j = randrange(50,X-90)
                bul_y_j = randrange(5,Y-45)
                bonus_j = tk.create_oval((bul_x_j,bul_y_j),(bul_x_j+40,bul_y_j+40),fill="yellow",tags="Bonus_jaune")
                if ((tk.coords(self.x,self.y)[1]<=tk.coords(bonus_j)[3]) and (tk.coords(self.x,self.y)[3]>=tk.coords(bonus_j)[1]) and (tk.coords(self.x,self.y)[2]>=tk.coords(bonus_j)[0]) and (tk.coords(self.x,self.y)[0]<=tk.coords(bonus_j)[2])):
                    tk.delete("Bonus_jaune")
            if self.bul == 1:
                bul_x_v = randrange(50,X-90)
                bul_y_v = randrange(5,Y-45)
                bonus_v = tk.create_oval((bul_x_v,bul_y_v),(bul_x_v+40,bul_y_v+40),fill="green")
                if ((tk.coords(self.x,self.y)[1]<=tk.coords(bonus_v)[3]) and (tk.coords(self.x,self.y)[3]>=tk.coords(bonus_v)[1]) and (tk.coords(self.x,self.y)[2]>=tk.coords(bonus_v)[0]) and (tk.coords(self.x,self.y)[0]<=tk.coords(bonus_v)[2])):
                    tk.delete(bonus_v)
                    pass
            if self.bul == 2:
                bul_x_r = randrange(50,X-90)
                bul_y_r = randrange(5,Y-45)
                bonus_r = tk.create_oval((bul_x_r,bul_y_r),(bul_x_r+40,bul_y_r+40),fill="red")
                if ((tk.coords(self.x,self.y)[1]<=tk.coords(bonus_r)[3]) and (tk.coords(self.x,self.y)[3]>=tk.coords(bonus_r)[1]) and (tk.coords(self.x,self.y)[2]>=tk.coords(bonus_r)[0]) and (tk.coords(self.x,self.y)[0]<=tk.coords(bonus_r)[2])):
                    tk.delete(bonus_r)
                    pass
