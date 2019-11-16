from tkinter import *

class MyApp:
   def __init__(self, parent):
       self.myParent = parent  ### (7) remember my parent, the root
       self.myContainer1 = Frame(parent)
       self.myContainer1.pack()

       self.button1 = Button(self.myContainer1)
       self.button1.configure(text="OK", background= "green")
       self.button1.pack(side=LEFT)
       self.button1.bind("<Button-1>", lambda e, win=self:
button1Click(win)) ### (1)

       self.button2 = Button(self.myContainer1)
       self.button2.configure(text="Cancel", background="red")
       self.button2.pack(side=RIGHT)
       self.button2.bind("<Button-1>", lambda e, win=self:
button2Click(win)) ### (2)

def button1Click(win):
   if win.button1["background"] == "green": ### (4)
       win.button1["background"] = "yellow"
   else:
       win.button2["background"] = "green"

def button2Click(win):
       win.myParent.destroy()     ### (6)


root = Tk()
myapp = MyApp(root)
root.mainloop()