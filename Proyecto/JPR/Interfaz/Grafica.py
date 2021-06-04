from tkinter import *
from tkinter import Menu


window = Tk()
#window.grid(column=0, row=0) 
window.geometry('1150x550')
window.title('JPR') 
    opciones(window)









#main loop sirve para mostrar la ventna
window.mainloop()

def opciones(ventana):
    menu =  Menu(ventana)
    menu.add_command(label = 'File')
    ventana.config(menu=menu)