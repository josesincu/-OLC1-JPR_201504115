from tkinter import *
from tkinter import Menu
from tkinter import filedialog

def abrirArchivo():
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))


def crearArchivo():
    print('Crear archivo')


def textArea(contenedor):
    texto = Text(contenedor)
    texto.pack(fill='both', expand=1)
    texto.pack(side=RIGHT)
    texto.config(padx=6, pady=4, bd=2, font=("Consolas", 12))


def contadorLinea(contenedor):
    texto = Text(contenedor)
    texto.pack(fill='both', expand=1)
    texto.pack(side=LEFT)
    texto.config(padx=6, pady=4, bd=2, font=("Consolas", 12))


def menuOpcion(ventana):
    #crealdo encabezado file
    menu =  Menu(ventana)
    #menu.add_command(label = 'File')
    #Crear archivo
    sub_file = Menu(menu,tearoff=0)
    sub_file.add_command(label = 'Crear Archivo',command = crearArchivo)
    sub_file.add_separator()
    #Abrir Archivo
    sub_file.add_command(label = 'Abrir Archivo',command = abrirArchivo)
    sub_file.add_separator()
    #menu.add_cascade(label = 'File',menu=sub_menu)
    #Guardar
    sub_file.add_command(label = 'Guardar')
    sub_file.add_separator()
    #menu.add_cascade(label = 'File',menu=sub_menu)

    #Guardar Como
    sub_file.add_command(label = 'Guardar Como')
    menu.add_cascade(label = 'File',menu=sub_file)

    #fin de opciones file

    #inicio de opciones herramienta
    sub_herra = Menu(menu,tearoff=0)
    #Ejecutar
    sub_herra.add_command(label='Ejecutar')
    sub_herra.add_separator()

    #Debuger
    sub_herra.add_command(label='Debuger')
    menu.add_cascade(label = 'Herramienas',menu=sub_herra)
    menu.add_command(label = 'Reportes')
    menu.add_command(label = 'Caracteristicas')
    ventana.config(menu=menu)

def contenedor(ventana):
    _contenedor=Frame(ventana)
    _contenedor.pack(side=LEFT)
    _contenedor.config(width=200,height=200) 
    _contenedor.config(bd=10)
    textArea(_contenedor)
    contadorLinea(_contenedor)
    #cajaInferior=Frame(ventana)
    #cajaInferior.pack(side=BOTTOM)


#aqui empieza la grafica
window = Tk()
#window.grid(column=0, row=0) 
window.geometry('1150x550')
window.title('JPR')
menuOpcion(window)
contenedor(window)
#textArea(window)
#menuHerramientas(window)
#main loop sirve para mostrar la ventna
window.mainloop()

