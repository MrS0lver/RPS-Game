from tkinter import *
from tkinter import messagebox,ttk
from PIL import ImageTk,Image
import random

class Game(Tk):
     def __init__(self):
          super().__init__()
          self.geometry("600x500")
          self.title("Game & fun")
          self.config(bg="white")
          self.resizable(False,False)
     def setup(self):
          self.rock = ImageTk.PhotoImage(file="rock1.png")
          self.paper = ImageTk.PhotoImage(file="paper1.png")
          self.sesor = ImageTk.PhotoImage(file="sesor1.png")
     def buttons(self):
          Button(image=self.rock,bg="white",width=105,height=120,command=self.rock1).grid()
          Button(image=self.paper, bg="white",width=105,height=120,command=self.paper1).grid()
          Button(image=self.sesor, bg="white",width=105,height=120,command=self.sesor1).grid()
          Button(text="Fullscreen", font=("consolas", 15), command=self.screen).grid()#$place(x=518, y=1)
          Button(text="    Cancel", font=("consolas", 15), command=self.cancel).grid()#place(x=465, y=1)

          Button(text="Stop",font=("consolas",20)).place(y=400,x=290)

          self.yin = Label(bg="white", fg="white")
          self.yin.place(x=300)

          a = self.rock
          b = self.paper
          c = self.sesor

     def test(self):
         l = [self.rock, self.paper, self.sesor]
         mo = random.choice(l)
         self.yin1 = Label(bg="white",fg="white")
         self.yin1.place(x=300,y=200)
         self.yin1.config(image=mo)
         self.yin1.after(200,self.test)




     def rock1(self):
         a = self.rock
         b = self.paper
         c = self.sesor
         self.yin.config(image=self.rock)
         l = [a,b,c]
         mo = random.choice(l)


         self.com = Label(bg="white",fg="white",image=mo)
         self.com.place(x=300,y=200)
         self.yin1.destroy()
         # messagebox.askretrycancel("helow","try")
         if self.yin == self.com:
            print("yes")
         else:
             pass



     def paper1(self):
         self.yin.config(image=self.paper)
         l = [self.rock, self.paper, self.sesor]
         mo = random.choice(l)
         self.com = Label(bg="white", fg="white", image=mo)
         self.com.place(x=300, y=200)
         self.yin1.destroy()
     def sesor1(self):
         self.yin.config(image=self.sesor)
         l = [self.rock, self.paper, self.sesor]
         mo = random.choice(l)
         self.com = Label(bg="white", fg="white", image=mo)
         self.com.place(x=300, y=200)
         self.yin1.destroy()

     def screen(self):
         self.attributes('-fullscreen',True)
     def cancel(self):
         self.attributes('-fullscreen',False)
















obj = Game()
obj.setup()
obj.buttons()
obj.test()
obj.mainloop()
