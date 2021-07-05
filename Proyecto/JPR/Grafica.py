
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter.ttk import *
import tkinter.scrolledtext as st
from tkinter import filedialog as FileDialog
from tkinter import colorchooser as ColorChooser
from tkinter.font import Font
from gramatica import parse,getErrores
import os
#import os
from Abstract.NodoAST import NodoAST
import webbrowser


#/home/dark/A_2021/Vaciones_Junio/Compi1/Laboratorio/Proyecto1/Proyecto/JPR/gramatica.py
#__________________________importando analizador sintactico _______________________

#==============================================================

#==============================================================

pathFile=''
nombreFile=''
comando_consola=''

no_instruccion=0
ejecucion_automatica=1



def font_resaltar():
    '''
    editor_font2 = Font(family="Helvetica", size=12, weight="normal" )
    editor.tag_config('otros', foreground='black', font=editor_font2)
    editor.tag_config('reservada', foreground="blue",font=editor_font2)
    editor.tag_config('cadenas', foreground='orange', font=editor_font2)
    editor.tag_config('numeros', foreground='#6a0dad', font=editor_font2)
    editor.tag_config('comentario', foreground='gray', font=editor_font2)
    '''
    editor_font2 = Font(family="Helvetica", size=12, weight="normal" )
    editor.tag_config('numeros', foreground='#6a0dad', font=editor_font2)
    editor.tag_config('otros', foreground='black', font=editor_font2)
    editor.tag_config('cadenas', foreground='orange', font=editor_font2)
    editor.tag_config('reservada', foreground="blue",font=editor_font2)
    editor.tag_config('comentario', foreground='gray', font=editor_font2)

    
def aplicarColor():
    #______________________- EDITOR ____________________
    
    editor.tag_remove("numeros", '1.0', END)
    editor.tag_remove("otros", '1.0', END)
    editor.tag_remove("cadenas", '1.0', END)
    editor.tag_remove("reservada", '1.0', END)
    editor.tag_remove("comentario", '1.0', END)
    

    #________________________ COLOREAR TEXTO _____________
    colorearTexto("numeros",r'\d+')
    colorearTexto("numeros",r'\d+\.\d+')

    colorearTexto("otros",r'\[')
    colorearTexto("otros",r'\]')
    colorearTexto("otros",r';')
    colorearTexto("otros",r'&')
    colorearTexto("otros",r'\(')
    colorearTexto("otros",r'\)')
    colorearTexto("otros",r'{')
    colorearTexto("otros",r'}')
    colorearTexto("otros",r'=')
    colorearTexto("otros",r'[a-zA-Z][a-zA-Z_0-9]*')
    
    colorearTexto("cadenas",r'\"((?:[^"\\]|\\.)*)\"')#cadena string
    colorearTexto("cadenas",r"\'((?:[^'\\]|\\(t|\'|\n|\"|r|\\))*)\'")#caracter

    colorearTexto("reservada",r'int')
    colorearTexto("reservada",r'break')

    colorearTexto("reservada",r'main')
    colorearTexto("reservada",r'if')
    
    colorearTexto("reservada",r'char')
    colorearTexto("reservada",r'double')
    colorearTexto("reservada",r'float')
    colorearTexto("reservada",r'char')
    colorearTexto("reservada",r'switch')
    colorearTexto("reservada",r'break')
    colorearTexto("reservada",r'var')
    colorearTexto("reservada",r'func')
    colorearTexto("reservada",r'return')


    colorearTexto("comentario",r'\#\*(.|\n)*?\*\#')
    colorearTexto("comentario",r'\#.*\n')
    
    

    

def colorearTexto(tipo,regex):
    count = IntVar(editor)
    pos = editor.index("end")
    while True:
        pos = editor.search(regex,  pos, "1.0",  backwards=True, regexp=True, count=count)
        if not pos:
            break
        index2  ='{}+{}c'.format(pos, count.get())
        editor.tag_add(tipo, pos, index2)
    

#__________________ Tabla ________________________________
from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos
from TS.Excepcion import Excepcion
#________________importanto instrucciones _________________
#from Instrucciones.Imprimir import Imprimir
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Declaracion_sinAsignacion import Declaracion_sinAsignacion
from Instrucciones.Asignacion import Asignacion
#from Instrucciones.If import If
from Instrucciones.Break import Break
#from Instrucciones.While import While
#from Instrucciones.Incremento import Incremento
#from Instrucciones.For import For
#from Instrucciones.Switch import Switch
#from Instrucciones.Caso import Caso
#from Instrucciones.Continue import Continue
from Instrucciones.Main import Main
from Instrucciones.Funcion import Funcion
from Instrucciones.Return import Return
from Instrucciones.ModificarArreglo import ModificarArreglo
from Instrucciones.DeclaracionArreglo import DeclaracionArreglo
from Instrucciones.DeclaracionArreglo2 import DeclaracionArreglo2
#_______________________ FUNCIONES NATIVAS ______________________________________
from Nativas.ToUpper import ToUpper
from Nativas.ToLower import ToLower
from Nativas.Length import Length
from Nativas.Truncate import Truncate
from Nativas.Round import Round
from Nativas.TypeOf import TypeOf
#__________________________________ TS ___________________________________________
from TS.Tipo import TIPO
#___________________________________ REPORTE ______________________________________
from Reporte.Reporte import reporte
#___________________________________ READ _______________________________________
from Expresiones.Read import Read
from Expresiones.AccesoArreglo import AccesoArreglo

def crearNativas(ast):
    #toUpper
    nombre = "toUpper"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'toUpper##Param1'}]
    instrucciones = []
    toUpper = ToUpper(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(toUpper)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    #toLower
    nombre = "toLower"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'toLower##Param1'}]
    instrucciones = []
    toLower = ToLower(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(toLower)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
    
    #length
    nombre = "Length"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'toLength##Param1'}]
    instrucciones = []
    length = Length(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(length)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    #truncate 
    nombre = "Truncate"
    parametros = [{'tipo':TIPO.DECIMAL,'identificador':'toTruncate##Param1'}]#si queres otro paramteo solo agregar , y otra lista
    instrucciones = []
    truncate = Truncate(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(truncate)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    #Round
    nombre = "Round"
    parametros = [{'tipo':TIPO.DECIMAL,'identificador':'toRound##Param1'}]#si queres otro paramteo solo agregar , y otra lista
    instrucciones = []
    roundd = Round(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(roundd)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    #typeof
    nombre_t = "TypeOf"
    parametros_t = [{'tipo':TIPO.CUALQUIERA,'identificador':'toTypeOf##Param1'}]#si queres otro paramteo solo agregar , y otra lista
    instrucciones_t = []
    typeOf = TypeOf(nombre_t, parametros_t, instrucciones_t, -1, -1)
    ast.addFuncion(typeOf)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)



def ejecutar_entrada():
    cont=editor.get("1.0",END)
    
    instrucciones = parse(cont) # ARBOL AST
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolos(None,"Global")
    ast.setTSglobal(TSGlobal)
    crearNativas(ast)
    
    for error in getErrores():                   # CAPTURA DE ERRORES LEXICOS Y SINTACTICOS
        ast.getExcepciones().append(error)
        #ast.updateConsola(error.toString())
        consola.insert('insert',">>"+error.toString()+"\n")

    for instruccion in ast.getInstrucciones():      # 1ERA PASADA (DECLARACIONES Y ASIGNACIONES)
        
        if isinstance(instruccion, Funcion):
            ast.addFuncion(instruccion)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
            #ast.addSim_Tabla((instruccion.nombre,"Funcion","----","Global",'----',instruccion.fila,instruccion.columna))
        if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion,Declaracion_sinAsignacion) or isinstance(instruccion,DeclaracionArreglo) or isinstance(instruccion,ModificarArreglo) or isinstance(instruccion,AccesoArreglo) or isinstance(instruccion,DeclaracionArreglo2):
            #if isinstance(instruccion,Declaracion):
            #   ast.addSim_Tabla((instruccion.identificador,"Variable","----","Global",instruccion.expresion,instruccion.fila,instruccion.columna))
            value = instruccion.interpretar(ast,TSGlobal,consola)
            if isinstance(value, Excepcion) :
                ast.getExcepciones().append(value)
                #ast.updateConsola(value.toString())
                consola.insert('insert',">>"+value.toString()+"\n")
            if isinstance(value, Break): 
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                #ast.updateConsola(err.toString())
                consola.insert('insert',">>"+err.toString()+"\n")
        
    for instruccion in ast.getInstrucciones():      # 2DA PASADA (MAIN)
        contador = 0
        if isinstance(instruccion, Main):
            contador += 1
            if contador == 2: # VERIFICAR LA DUPLICIDAD
                err = Excepcion("Semantico", "Existen 2 funciones Main", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                #ast.updateConsola(err.toString())
                consola.insert('insert',">>"+err.toString()+"\n")
                break

            
            value = instruccion.interpretar(ast,TSGlobal,consola)
            
            if isinstance(value, Excepcion) :
                ast.getExcepciones().append(value)
                #ast.updateConsola(value.toString())
                consola.insert('insert',">>"+value.toString()+"\n")
            if isinstance(value, Break): 
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                #ast.updateConsola(err.toString())
                consola.insert('insert',">>"+err.toString()+"\n")
            if isinstance(value,Return):
                err = Excepcion("Semantico", "Sentencia Return fuera de funcion o ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                #ast.updateConsola(err.toString())
                consola.insert('insert',">>"+err.toString()+"\n")

        
    for instruccion in ast.getInstrucciones():    # 3ERA PASADA (SENTENCIAS FUERA DE MAIN)
        if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion, Funcion) or isinstance(instruccion,Declaracion_sinAsignacion) or isinstance(instruccion,DeclaracionArreglo) or isinstance(instruccion,ModificarArreglo) or isinstance(instruccion,AccesoArreglo) or isinstance(instruccion,DeclaracionArreglo2)):
            err = Excepcion("Semantico", "Sentencias fuera de Main", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            #ast.updateConsola(err.toString())
            consola.insert('insert',">>"+err.toString()+"\n")
    init = NodoAST("RAIZ")
    instr = NodoAST("INSTRUCCIONES")

    for instruccion in ast.getInstrucciones():
        instr.agregarHijoNodo(instruccion.getNodo())

    init.agregarHijoNodo(instr)
    grafo = ast.getDot(init) #DEVUELVE EL CODIGO GRAPHVIZ DEL AST

    dirname = os.path.dirname(__file__)
    direcc = os.path.join(dirname, nombreFile+'.dot')
    arch = open(direcc, "w+")
    arch.write(grafo)
    arch.close()
    os.system('dot -T pdf -o '+nombreFile+'.pdf '+ nombreFile+'.dot')

    #_________________________________________________
    reporte(nombreFile,ast.getExcepciones())
    #consola.insert('insert',ast.getConsola())
    for contact in ast.getSim_Tabla():
        tabla_simbolo.insert('',END, values=contact)
    


def iniciar_debug():
    pass
waitForCommand=0

def ejec_debug():
    pass
    
def getSaltoLinea(cadena):
    cont=0
    for i in cadena:
        if i=='\n':
            cont=cont+1
    return cont


def ast_grafica():
    #Cambia la ruta para indicar la localización del archivo
    nombreArchivo = './' +nombreFile+'.pdf'
    #crearReporte(nombreFile)
    webbrowser.open_new_tab(nombreArchivo)
    

def rep_tablasimbolos():
    pass

def rep_errores():
    #Cambia la ruta para indicar la localización del archivo
    nombreArchivo = './Archivos/' +nombreFile+'.html'
    #crearReporte(nombreFile)
    webbrowser.open_new_tab(nombreArchivo)


def acerca_de():
    MessageBox.showinfo("JPR-Compiladores1","\n Facultad de Ingenieria, USAC \nJose Castro Sincu \n201504115")

def ayuda():
    MessageBox.showinfo("Ayuda-JPR",
                        '''Compilador JPR - USAC. \nJPR  esta basado en java,python, misma sintaxis con menor cantiad de instrucciones. \nCompila distitos tipos de instrucciones''')

def nuevo():
    global pathFile
    pathFile = ""
    editor.delete(1.0, "end")
    root.title("JPR")

def abrir(): 
    global pathFile
    global nombreFile
    tabla_simbolo.delete(*tabla_simbolo.get_children())
    consola.delete('1.0', END)

    pathFile = FileDialog.askopenfilename(
        initialdir='./Archivos/',
        filetypes=( 
            ("Archivos de texto", "*.jpr"),  
        ), 
        title="Abrir Archivo"
    )

    if pathFile != "":  
        nombreFile=os.path.basename(pathFile)[0:-4]
        archivo = open(pathFile, 'r',encoding="utf8",errors='ignore')
        contenido = archivo.read()
        editor.delete(1.0, 'end')           
        editor.insert('insert', contenido)  
        archivo.close()                    
        root.title(pathFile + " -JPR") 
        aplicarColor()

def guardar():
    global pathFile
    if pathFile != "":
        contenido = editor.get(1.0, 'end-1c') 
        archivo = open(pathFile, 'w+')         
        archivo.write(contenido)           
        archivo.close()
        MessageBox.showinfo("Archivo guardado","El archivo se guardo exitosamente")
    else :
        MessageBox.showwarning("Guardar","Abra un archivo primero")

def guardar_como():
    global pathFile
    archivo = FileDialog.asksaveasfile(title="Guardar archivo", mode='w',
            defaultextension=".jpr")
    if archivo is not None:
        pathFile = archivo.name  
        contenido = editor.get(1.0, 'end-1c')  
        archivo = open(pathFile, 'w+') 
        archivo.write(contenido) 
        archivo.close()
        MessageBox.showinfo("Archivo guardado","El archivo se guardo exitosamente")
    else:
        MessageBox.showinfo("El archivo no se guardó")


def multiple_yview(*args):
    editor.yview(*args)
    FrameLines.yview(*args)

def pintar_lineas(event):
    index = 0
    (line,c) = map(int, event.widget.index('end-1c').split('.'))
    FrameLines.delete(1.0,'end')

    for i in range(1,line+2,1):
        FrameLines.insert('insert',str(i)+'\n')
        a,b=editor.vbar.get()
        FrameLines.yview_moveto(a)
        pass
    
    aplicarColor()

def agregarSalto(event):
    print('Entre en salo de linea')
    index = 0
    for i in range(1,line+2,1):
        consola.insert('insert',">>")
        a,b=consola.vbar.get()
        consola.yview_moveto(a)
        pass
    
    aplicarColor()

#==============================================================
#==============================================================
#                   INTERFAZ
#==============================================================
#==============================================================

root = Tk()
menubar = Menu(root)
root.config(menu=menubar)

#____________________________ FILE _________________________________
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_command(label="Cerrar", command=nuevo)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

#___________________________ AYUDA _________________________________
ayudamenu = Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Ayuda",command=ayuda)
ayudamenu.add_separator()
ayudamenu.add_command(label="Acerca de...", command=acerca_de)

#__________________________ EJECUTAR ________________________________
ejecutarmenu = Menu(menubar, tearoff=0)
ejecutarmenu.add_command(label="Analizar", command=ejecutar_entrada)
ejecutarmenu.add_separator()

ejecutarmenu.add_command(label="AST", command=ast_grafica)
ejecutarmenu.add_command(label="Tabla de Simbolos", command=rep_tablasimbolos)
ejecutarmenu.add_command(label="Reporte Errores", command=rep_errores)
ejecutarmenu.add_separator()

#__________________________  MENU PRINCIPAL ________________________
menubar.add_cascade(label="Archivo", menu=filemenu)
#menubar.add_cascade(label="Editar", menu=editarmenu)
menubar.add_cascade(label="Ejecutar", menu=ejecutarmenu)

menubar.add_cascade(label="Ayuda", menu=ayudamenu)

#-------------------------------------------
#-----------EDITOR Y CONSOLA----------------
#-------------------------------------------
leftside=Frame(root)
leftside.pack(side=LEFT)     
#-------------------------------------------
#-----------BOTONES SUPERIOES---------------
topSide=Frame(leftside)
topSide.pack(side=TOP)
topSide.config(width=80, height=5)

label2 = Label(topSide, text="Linea Actual")
label2.grid(row=0,column=3, sticky=W, padx=5, pady=5)

label3 = Label(topSide,text="0")
label3.grid(row=0,column=4, padx=5, pady=5)

label2 = Label(topSide, text="Debug")
label2.grid(row=0,column=6, sticky=W, padx=5, pady=5)

btn_iniciar=Button(topSide, text="Inicio",command=iniciar_debug)
btn_iniciar.config(width=10)
btn_iniciar.grid(row=0, column=7, padx=5,pady=5)

btn_cont=Button(topSide, text=">>", command=ejec_debug)
btn_cont.config(width=8)
btn_cont.grid(row=0, column=8, padx=5,pady=5)

#----------------------------------------------
cajaPrincipal=Frame(leftside)
cajaPrincipal.pack(side=TOP)
cajaInferior=Frame(leftside)
cajaInferior.pack(side=BOTTOM)
#-------------------------------------------
FrameLines= Text(cajaPrincipal)
FrameLines.pack(side=LEFT)  
FrameLines.config(width=5, height=25,bg="#D5DBDB",
             padx=0, pady=0, selectbackground="black")

editor = st.ScrolledText(cajaPrincipal)

select_font = Font(family="Helvetica", size=8, weight="normal" )
editor.tag_config('buscar', background='#ffff00', font=select_font)
font_resaltar()

editor.pack(side=LEFT)
editor.config(width=66, height=25,
             padx=0, pady=0)
editor.bind("<MouseWheel>",pintar_lineas)
editor.bind("<Key>",pintar_lineas)

rightBOTTOM=Frame(cajaInferior)
rightBOTTOM.pack(side=LEFT)
leftBOTTOM=Frame(cajaInferior)
leftBOTTOM.pack(side=RIGHT)

consola = Text(cajaPrincipal)

consola_font = Font(family="Helvetica", size=12, weight="normal" )
consola.config(width=66,height=25,padx=0.5, pady=0.5, font=consola_font, cursor="arrow",borderwidth=0,
                selectbackground="black",background="black", foreground="white")

#consola.insert('end','>>JPR-Compiladores1-USAC\n>>')
#consola.insert('end','>>HOla MUNDO')
#consola.bind("<Return>",comando_ingresado)
consola.bind("<Key>",agregarSalto)
consola.config(insertbackground="white")

scroll2 = Scrollbar(cajaPrincipal, orient=VERTICAL)
consola.configure(yscrollcommand = scroll2.set)
scroll2.config( command = consola.yview ) 
scroll2.pack(side=RIGHT, fill=Y)
consola.pack(side=RIGHT)

#s-------------DEBUGER--------------------
#-------------------------------------------

columnas = ('#1','#2','#3','#4','#5','#6','#7')
tabla_simbolo =Treeview(leftBOTTOM,columns=columnas, show='headings')

tabla_simbolo.heading('#1', text="Identificador",anchor=W)
tabla_simbolo.heading("#2", text="Tipo",anchor=W)
tabla_simbolo.heading("#3", text="Tipo",anchor=W)
tabla_simbolo.heading("#4", text="Entorno",anchor=W)
tabla_simbolo.heading("#5", text="Valor",anchor=W)
tabla_simbolo.heading("#6", text="Linea",anchor=W)
tabla_simbolo.heading("#7", text="Columna",anchor=W)

scroll3 = Scrollbar(leftBOTTOM, orient=VERTICAL)
tabla_simbolo.configure(yscrollcommand = scroll3.set)
scroll3.config( command = tabla_simbolo.yview ) 
scroll3.pack(side=RIGHT, fill=Y)


tabla_simbolo.pack(side=TOP,fill=Y)


#-------------SCROLL--------------------
scroll = Scrollbar(cajaPrincipal, orient=VERTICAL ,command=multiple_yview)
FrameLines.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)

root.geometry("1212x600")
root.resizable(width=False, height=False)
root.mainloop()

