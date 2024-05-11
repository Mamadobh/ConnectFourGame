import numpy as np 
from tkinter import *
import time
from tkinter import *
from tkinter import messagebox

# ==========================================================================================

class Grille:
    def __init__(self):
        self.grille=np.zeros((6,7))
    def update(self,x,y,q):
        self.grille[x][y]=q
        # print(self.grille)
       

    def gagne(self):
        for i in range(3):
            for j in range(4):
                t=self.grille[i:i+4,j:j+4]
                if(list(t.diagonal()).count(1)==4) or (list(np.fliplr(t).diagonal()).count(1)==4):
                    return 1
                if(list(t.diagonal()).count(2)==4) or (list(np.fliplr(t).diagonal()).count(2)==4):
                    return 2

                for k in range(4):
                    m=t[k,:]
                    m1=t[:,k]
                    if(list(m).count(1)==4 or list(m1).count(1)==4):
                        return 1
                    elif(list(m).count(2)==4) or (list(m1).count(2)==4):
                        return 2
                        
        # for i in range(6):
        if(list(self.grille[0,:]).count(0)==0):
            return 0
        return 3
# ==========================================================================================
                    



# ==========================================================================================

class Ligne:
    def __init__(self):
        self.ligne=0
    def update(self,x):
        self.ligne=x//54
# ==========================================================================================
# ==========================================================================================

class Colonne:
    def __init__(self):
        self.colonne=0
    def update(self,x):
        self.colonne=(x-33)//54
# ==========================================================================================
        
# ==========================================================================================
class Joueur:
    def __init__(self,a,b,c):
        self.nom=a
        self.num=b
        self.couleur=c
    def set_nom(self,ch):
        self.nom=ch   
    def set_couleur(self,x):
        self.couleur=x
# ==========================================================================================

# ==========================================================================================

matrice=Grille()
ligne_matrice=Ligne()
colonne_matrice=Colonne()
joueur_1=Joueur("",1,"")
joueur_2=Joueur("",2,"")
# ==========================================================================================

