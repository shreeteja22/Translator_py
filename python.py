from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg = 'Red')

lab_txt= Label(root,text='Translator',font=("Arial ",30,"bold"))
lab_txt.place(x=100,y=20,height=100,width=300)

frame = Frame(root).pack(side=BOTTOM)

sor_txt = Text(frame,font=("Arial ",20,"bold"),wrap=WORD)

root.mainloop()
