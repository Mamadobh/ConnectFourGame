from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np 
import time
from class_poo import *
root =Tk()
root.title("Connect 4 Game")
root.resizable(width=False,height=False)
root.geometry("600x400")
icon=PhotoImage(file='images.jpeg')
root.iconphoto(False,icon)
root.eval('tk::PlaceWindow . center')

# =========================================================================================
# Start first interface
f1=LabelFrame(root,bd=0,bg="#416cea",width=600,height=400)
f1.pack()
f11=LabelFrame(f1,bg="#416cea",bd=0)
f11.place(x=0,y=0,relheight=1,relwidth=0.5)
im1=PhotoImage(file="bg1.png")
ap1= Label(f11,image=im1,borderwidth=0,bg="#416cea")
ap1.place(x=8.5,y=0,rely=0.12)
f12=LabelFrame(f1,bd=0,bg="#416cea",width=300)
f12.place(x=0,y=0,relheight=1,relwidth=0.5,relx=0.5)
l1=Label(f12,text="Welcome here !",fg="#ffffff",bg="#416cea",font=("Yu Gothic Medium", 12,"bold"))
l1.place(relx=0,rely=0.35,x=0)
l2=Label(f12,text="CONNECT 4 GAME",fg="#ffffff",bg="#416cea",font=("Arial", 23,"bold"))
l2.place(x=0,relx=0,rely=0.45)
# End first interface
# =====================================
# Satrt button to navigate for second interface 
def action1():
    global e1
    f1.pack_forget()
    f2.pack()
    e1.focus_set()
b1=Button(f12,text = "PALY NOW !",font=("Arial", 15,"bold"),bg="#ffffff",bd=0 ,command=action1)  
b1.place(x=0,relx=0,rely=0.6,relwidth=0.94)
# End button to navigate for second interface 
# =====================================

# ==========================================================================================



# ==========================================================================================
# start second interface 
f2=LabelFrame(root,width=600,height=400,bd=0,bg="#416cea")
f21=LabelFrame(f2,bd=0,height=160,bg="#416cea",width=600)
f21.grid(row=0,column=0)
f22=LabelFrame(f2,bd=0,bg="#416cea",height=160,width=600)
f22.grid(row=1,column=0)
f23=LabelFrame(f2,bd=0,bg="#416cea",height=80,width=600)
f23.grid(row=2,column=0)
l3=Label(f21,text="PLAYER 1:",fg="#ffffff",bg="#416cea",font=("Arial", 20,"bold","italic"))
l3.place(x=0,y=30,relx=0.1)
l4=Label(f21,text="NAME:",fg="#ffffff",bg="#416cea",font=("Arial", 12,"bold"))
l4.place(x=0,y=0,rely=0.6,relx=0.1)
e1=Entry(f21)
e1.place(x=0,y=0,rely=0.6,relx=0.25)
joueur_1.set_nom(e1.get())
l5=Label(f21,text="COLOR:",fg="#ffffff",bg="#416cea",font=("Arial", 12,"bold"))
l5.place(x=0,y=0,rely=0.6,relx=0.5)
l=["Red","Yellow","Green","Pink","Orange","Black","Purple"]
lc1=ttk.Combobox(f21,values=l)
lc1.config(state='readonly')
lc1.current(0)
lc1.place(x=0,y=0,rely=0.6,relx=0.7)
l6=Label(f22,text="PLAYER 2:",fg="#ffffff",bg="#416cea",font=("Arial", 20,"bold","italic"))
l6.place(x=0,y=30,relx=0.1)
l7=Label(f22,text="NAME:",fg="#ffffff",bg="#416cea",font=("Arial", 12,"bold"))
l7.place(x=0,y=0,rely=0.6,relx=0.1)
e2=Entry(f22)
e2.place(x=0,y=0,rely=0.6,relx=0.25)
joueur_2.set_nom(e2.get())
l8=Label(f22,text="COLOR:",fg="#ffffff",bg="#416cea",font=("Arial", 12,"bold"))
l8.place(x=0,y=0,rely=0.6,relx=0.5)
l1=["Red","Yellow","Green","Pink","Orange","Black","Purple"]
lc2=ttk.Combobox(f22,values=l1)
lc2.config(state='readonly')
lc2.current(1)
lc2.place(x=0,y=0,rely=0.6,relx=0.7)

# End Second interface
# ==========================================================================================

# ===========================================================
# Start button to navigate for third interface 
def action2():

    if e1.get()=="" or e2.get()=="" or not lc1.get() in l or not lc2.get() in l or lc1.get()==lc2.get() or e1.get()==e2.get():
   
        messagebox.showinfo('Warning', "check your informations!")    
    else:
        joueur_1.set_couleur(lc1.get())
        joueur_2.set_couleur(lc2.get())
        joueur_1.set_nom(e1.get())
        joueur_2.set_nom(e2.get()) 

        f2.pack_forget()
        f3.pack()
        l32.configure(text=joueur_1.nom)
        l34.configure(text=joueur_2.nom)
        c1.itemconfigure(rond1,fill=joueur_1.couleur)
        c2.itemconfigure(rond2,fill=joueur_2.couleur)
b2=Button(f23,text = "START PLAY!",font=("Arial", 15,"bold"),bg="#ffffff",bd=0,command=action2)
b2.place(x=0,y=0,relx=0.5,rely=0.5,anchor=CENTER,relwidth=0.4)
# End button to navigate for third interface 
# ===========================================================


# ==========================================================================================
# Start third interface 
f3=LabelFrame(root,padx=0,pady=0,bd=0)
f31=LabelFrame(f3,padx=0,pady=0,bd=0)
f31.grid(row=0,column=0)
f32=LabelFrame(f3,padx=0,pady=0,bd=0)
f32.grid(row=0,column=1)
# ================================================
# Start pop-up
def replay():
      pop.destroy()
      c3.delete('all')
      global gr ,gri,en,matrice,tour,r1,r2,r3,r4,r5,r6,r7
      matrice=Grille()
      gri=c3.create_image(218,200,image=gr)
      r1,r2,r3,r4,r5,r6,r7=355,355,355,355,355,355,355
      en=True
      tour=0
def back():
      pop.destroy()
      c3.delete('all')
      global gr ,gri,e1,e2,en,matrice,tour,r1,r2,r3,r4,r5,r6,r7
      matrice=Grille()
      e1.delete(0, END)
      e2.delete(0, END)
      e1.focus_set()
      gri=c3.create_image(218,200,image=gr)
      r1,r2,r3,r4,r5,r6,r7=355,355,355,355,355,355,355
      en=True
      tour=0
      f3.forget()
      f2.pack()

def Result(result,img_l):
	global img1 ,root,pop,res
	img1="result.png"
	pop = Toplevel(root)
	pop.iconbitmap(img1)
	pop.title("RESULT")
	pop.geometry("250x150")
	pop.config(bg="#416cea")
	pop.resizable(width=False,height=False)
	res = PhotoImage(file=img_l)
	my_frame = Frame(pop,bg="#416cea")
	my_frame.place(x=0,y=0,relheight=0.6,relwidth=1)
	res_pic = Label(my_frame, image=res, borderwidth=0)
	res_pic.place(relheight=0.8,x=10,y=10)
	pop_label = Label(my_frame, bg="#416cea",text=result, fg="white", font=("helvetica",14))
	pop_label.place(relx=0.35,y=40)
	btn_frame=Frame(pop, bg="#416cea")
	btn_frame.place(rely=0.6,relheight=0.4,relwidth=1)
	replay_bt=Button(btn_frame, text="REPLAY", bg="orange",bd=0,font=("helvetica",10),command=replay)
	replay_bt.place(relx=0.25,relheight=0.6,rely=0.18,relwidth=0.3)
	back_bt=Button(btn_frame, text="BACK",bg="orange" ,bd=0,font=("helvetica",10),command=back)
	back_bt.place(relx=0.65,relwidth=0.3,relheight=0.6,rely=0.18)

# End pop-up
# ==========================================



# ==========================================
# Start  function that moving the ball into thier suitable position in the grid 
def moving_oval(x,y,c,k,j,s):
        global r1,r2,r3,r4,r5,r6,r7,en,chc,tour
        chc=joueur_2.couleur if tour%2!=0  else joueur_1.couleur
        rond3=c3.create_oval(x,y,c,k,fill=chc)
        c3.tag_raise(gri)
        en=False
        while k<s:
            c3.move(rond3,0,1)
            k+=1
            time.sleep(0.002)
            c3.update()
        s-=54
        ligne_matrice.update(s)
        colonne_matrice.update(j)
        matrice.update(ligne_matrice.ligne,colonne_matrice.colonne,tour%2+1)
        tour+=1
        en=True
        if(matrice.gagne()==1):
            Result(f"** {joueur_1.nom} Win ! **","win.png")
            en=False
        elif(matrice.gagne()==2):       
            Result(f"** {joueur_2.nom} Win ! **","win.png")
            en=False
        elif(matrice.gagne()==0):    
            Result("** Equal Game ! **","equal.png")
            en=False   
        return s
# end function which moving the ball into thier suitable position in the grid 
# ==========================================



# ==========================================
#Satrt function that identify the suitable column   
def put(e):
    
    a=e.x
    z=65
    global r1,r2,r3,r4,r5,r6,r7,en,chc,tour

    if a>32 and a<79 and r1>40 and en:
        r1=moving_oval(33,20,79,z,a,r1)
    elif a>86 and a<133 and r2>40 and en:
        r2=moving_oval(87,20,132,z,a,r2)
    elif a>140 and a<187 and r3>40 and en:
        r3=moving_oval(141,20,186,z,a,r3)
    elif a>194 and a<241 and r4>40 and en:
        r4=moving_oval(195,20,240,z,a,r4)
    elif a>248 and a<295 and r5>40 and en:
        r5=moving_oval(249,20,294,z,a,r5)
    elif a>302 and a<349 and r6>40 and en:
        r6=moving_oval(303,20,348,z,a,r6)
    elif a>356 and a<403 and r7>40 and en:
        r7=moving_oval(357,20,402,z,a,r7)

#End  function that identify the suitable column        
# ==========================================


l31=Label(f31,height=2,text="PLAYER 1:",font=("Arial",18,"bold"))
l31.pack()
l32=Label(f31,height=2,text="name1",font=("Arial",18,"bold"))
l32.pack()
c1=Canvas(f31,width=50,height=50)
c1.pack()
rond1=c1.create_oval(5,5,45,45,fill=joueur_1.couleur)
l33=Label(f31,height=2,text="PLAYER 2:",font=("Arial",18,"bold"))
l33.pack()
l34=Label(f31,height=2,text="name2",font=("Arial",18,"bold"))
l34.pack()
c2=Canvas(f31,width=50,height=50)
c2.pack()
rond2=c2.create_oval(5,5,45,45,fill=joueur_2.couleur,)
c3=Canvas(f32,width=420,height=380)
c3.pack()
gr=PhotoImage(file="im331.png")
gri=c3.create_image(218,200,image=gr)
r1,r2,r3,r4,r5,r6,r7=355,355,355,355,355,355,355
en=True
chc=joueur_1.couleur
tour=0
c3.bind('<Button-1>',put)
# End the third interface 
# ==========================================================================================

root.mainloop()

