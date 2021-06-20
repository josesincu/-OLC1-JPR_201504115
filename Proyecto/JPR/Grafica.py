from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter.ttk import *
import tkinter.scrolledtext as st
from tkinter import filedialog as FileDialog
from tkinter import colorchooser as ColorChooser
from tkinter.font import Font
from gramatica import parse,obtenerConsola,crearReporte
import os
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
    editor_font2 = Font(family="Helvetica", size=12, weight="normal" )
    editor.tag_config('otros', foreground='black', font=editor_font2)
    editor.tag_config('reservada', foreground="blue",font=editor_font2)
    editor.tag_config('cadenas', foreground='orange', font=editor_font2)
    editor.tag_config('numeros', foreground='#6a0dad', font=editor_font2)
    editor.tag_config('comentario', foreground='gray', font=editor_font2)
    
    
    
    

def aplicarColor():
    #______________________- EDITOR ____________________
    editor.tag_remove("reservada", '1.0', END)
    editor.tag_remove("numero", '1.0', END)
    editor.tag_remove("variables", '1.0', END)
    editor.tag_remove("variables", '1.0', END)

    #________________________ COLOREAR TEXTO _____________
    colorearTexto("numeros",r'\d+')
    colorearTexto("numeros",r'\d+\.\d+')
    colorearTexto("otros",r'[a-zA-Z][a-zA-Z_0-9]*')

    colorearTexto("reservada",r'break')
    colorearTexto("reservada", r'\'.*?\'')
    colorearTexto("reservada", r'\".*?\"')
    colorearTexto("reservada",r'main')
    colorearTexto("reservada",r'if')
    colorearTexto("reservada",r'int')
    colorearTexto("reservada",r'char')
    colorearTexto("reservada",r'double')
    colorearTexto("reservada",r'float')
    colorearTexto("reservada",r'char')
    colorearTexto("reservada",r'switch')
    colorearTexto("reservada",r'break')
    colorearTexto("reservada",r'var')

    colorearTexto("otros",r'\[')
    colorearTexto("otros",r'\]')
    colorearTexto("otros",r';')
    colorearTexto("otros",r'&')
    colorearTexto("otros",r'\(')
    colorearTexto("otros",r'\)')
    colorearTexto("otros",r'{')
    colorearTexto("otros",r'}')
    colorearTexto("otros",r'=')
    

    colorearTexto("cadenas",r'\"((?:[^"\\]|\\.)*)\"')
    colorearTexto("cadenas",r'\'.\'')

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
    colorearTextoAugus(tipo,regex)

def colorearTextoAugus(tipo,regex):
    count = IntVar(editor)
    pos = editorC3D.index("end")
    while True:
        pos = editorC3D.search(regex,  pos, "1.0",  backwards=True, regexp=True, count=count)
        if not pos:
            break
        index2  ='{}+{}c'.format(pos, count.get())
        editorC3D.tag_add(tipo, pos, index2)

def pintar_TS_IDE():
    for row in debugger.get_children():
        debugger.delete(row)

    if len(Inter.instrucciones)>0:
        lis_symbol=Inter.ts_global.simbolos
        lis_fun = Inter.ts_global.funciones
        for item in lis_symbol:
            sim=Inter.ts_global.obtener(item,1)
            if sim.tipo==TS.TIPO_DATO.ARREGLO:
                val=""
                padre=debugger.insert("", 1, text=sim.id, values=(val))
                for item_arr in sim.valor:
                    val=""
                    cad=item_arr.split('_')
                    for cad_item in cad:
                        if cad_item!="":
                            val+="["+cad_item+"]"
                    val+="="+str(sim.valor[item_arr])
                    debugger.insert(padre, END, text="", values=(val))
            else:
                debugger.insert("", END, text=sim.id, values=(sim.valor))

def ejec_ascendenteMinorC():
    #c3d.limpiarValores()
    cont=editor.get("1.0",END)
    #resultado=c3d.inicializarEjecucionAscendente(cont)
    resultado = parse(cont)
    editorC3D.delete(1.0, 'end')           
    editorC3D.insert('insert',obtenerConsola())
    consola.insert('insert',obtenerConsola())
    
    #ejec_ascendente()


def iniciar_debug():
    global no_instruccion,ejecucion_automatica
    ejecucion_automatica=0
    no_instruccion=0
    Inter.inicializarGUI(editorC3D,consola)
    Inter.limpiarValores()
    cont=editorC3D.get("1.0",END)
    Inter.inicializarEjecucionAscendente(cont)
    Inter.inicializarTS()

waitForCommand=0
def ejec_debug():
    global ts_debug, no_instruccion, waitForCommand
    if waitForCommand==0 or waitForCommand==2: #0=Sin Entrada, 1=Esperando, 2=Comando Ingresado
        if no_instruccion<len(Inter.instrucciones) :
            is_asig=Inter.instrucciones[no_instruccion]
            if isinstance(is_asig,Asignacion): 
                # COMANDO PARA LEER DE CONSOLA
                if isinstance(is_asig.valor,Read) and waitForCommand==0:
                    waitForCommand=1
                    return None
            #EJECUTAR INSTRUCCION
            instr_temp=Inter.ejecutarInstruccionUnitaria(1,no_instruccion)
            if instr_temp is not None:
                if instr_temp==-10 : # EXIT
                    no_instruccion=len(Inter.instrucciones)
                else: #GOTO
                    no_instruccion=instr_temp
            waitForCommand=0
            no_instruccion+=1
            pintar_TS_IDE()
        else:
            MessageBox.showinfo("Finalizado","Ultima instruccion ejecutada.")
    

def comando_ingresado(event):
    #consola.insert("end","\n>>")
    global waitForCommand
    waitForCommand=2
    if ejecucion_automatica == 1:
        continuar_ejecucionAsc()
    elif ejecucion_automatica == 2:
        continuar_ejecucionDesc()

def getSaltoLinea(cadena):
    cont=0
    for i in cadena:
        if i=='\n':
            cont=cont+1
    return cont

def draw_instruction(indexDeb):

    start=0
    last=0
    editor.tag_remove("buscar","1.0",END)
    arreglo=re.split(';|:',editor.get("1.0",END))
    
    for i in range(0,len(arreglo)):
        if i<indexDeb:
            start+=getSaltoLinea(arreglo[i])
        else:
            #last=len(arreglo[i])
            break
    start=start+1 # main no tiene salto
    #start=start+1 # arreglo empieza en 0

    primero=str(float(start)+0.1)
    ultimo=str(float(start)+0.81)
    editor.tag_add("buscar", primero, ultimo)
    
def ast_grafica():
    c3d.graficarAST()
    #Inter.generarReporteAST()

def gram_desc():
    Inter.generarReporteGramaticalDesc()

def rep_tablasimbolos():
    c3d.tabla_simbolosMinusC()
    #Inter.generarReporteTS()

def rep_errores():
    #Cambia la ruta para indicar la localización del archivo
    nombreArchivo = '/home/dark/A_2021/Vaciones_Junio/Compi1/Laboratorio/Proyecto1/Proyecto/JPR/' +nombreFile+'.html'
    crearReporte(nombreFile)
    webbrowser.open_new_tab(nombreArchivo)

def continuar_ejecucionDesc():
    global no_instruccion, waitForCommand

    while no_instruccion<len(Inter.instrucciones):
        if waitForCommand==0 or waitForCommand==2: #0=Sin Entrada, 1=Esperando, 2=Comando Ingresado
            if no_instruccion<len(Inter.instrucciones) :
                is_asig=Inter.instrucciones[no_instruccion]
                if isinstance(is_asig,Asignacion): 
                    # COMANDO PARA LEER DE CONSOLA
                    if isinstance(is_asig.valor,Read) and waitForCommand==0:
                        waitForCommand=1
                        #no_instruccion=i
                        return None
                #EJECUTAR INSTRUCCION
                instr_temp=Inter.ejecutarInstruccionUnitaria(1,no_instruccion)
                if instr_temp is not None:
                    if instr_temp==-10 : # EXIT
                        no_instruccion=len(Inter.instrucciones)
                    else: #GOTO
                        no_instruccion=instr_temp
                waitForCommand=0
                no_instruccion+=1
            else:
                MessageBox.showinfo("Finalizado","Ultima instruccion ejecutada.")


def wait_for_command():
    global comando_consola
    comando_consola=''
    print('Entro al wait for....')
    while comando_consola == '':
        print('Waiting...')
        time.sleep(0.3) 
    consola.insert('end','>>')
    hilo2 = threading.Thread(target=reemplazar)   
    hilo2.start()
    return comando_consola


def getInput(event):
    global comando_consola
    contenido=consola.get("1.0","end-1c")
    lines = contenido.split(">>")

    last_line = lines[len(lines)-1]
    #print('El comando es: ',last_line)
    comando_consola=last_line


def reemplazar():
    txt1=txt_buscar.get()
    txt2=txt_reemplazar.get()
    if txt2 == "":
        txt2=txt1

    sustituciones = {txt1:txt2}

    regex = r'\y(?:{})\y'.format('|'.join(sustituciones.keys()))
    editor.tag_remove("buscar", '1.0', END)

    count = IntVar(editor)
    pos = editor.index("end")

    while True:
        pos = editor.search(regex,  pos, "1.0",  backwards=True, regexp=True, count=count)
        if not pos:
            break

        idx2  ='{}+{}c'.format(pos, count.get())
        editor.tag_add("found", pos, idx2)
        new = sustituciones[editor.get(pos, idx2)]
        editor.delete(pos, idx2)
        editor.insert(pos, new)
        editor.tag_add("buscar", pos, '{}+{}c'.format(pos, len(new)))

    txt_reemplazar.delete(0,'end')

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

    pathFile = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=( 
            ("Archivos de texto", "*"),  
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
            defaultextension=".txt")
    if archivo is not None:
        pathFile = archivo.name  
        contenido = editor.get(1.0, 'end-1c')  
        archivo = open(pathFile, 'w+') 
        archivo.write(contenido) 
        archivo.close()
        MessageBox.showinfo("Archivo guardado","El archivo se guardo exitosamente")
    else:
        MessageBox.showinfo("Archivo no guardado - Augus","El archivo no se guardó")


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
ejecutarmenu.add_command(label="Analizar", command=ejec_ascendenteMinorC)
ejecutarmenu.add_separator()

ejecutarmenu.add_command(label="AST", command=ast_grafica)
ejecutarmenu.add_command(label="Tabla de Simbolos", command=rep_tablasimbolos)
ejecutarmenu.add_command(label="Reporte Errores", command=rep_errores)
ejecutarmenu.add_separator()
ejecutarmenu.add_command(label="Iniciar Debugger",command=iniciar_debug)
ejecutarmenu.add_command(label="Siguiente Paso", command=ejec_debug)


#___________________________________ EDITAR MENU ____________________
editarmenu = Menu(menubar, tearoff=0)
editarmenu.add_command(label="Buscar y Reemplazar", command=reemplazar)
editarmenu.add_command(label="Buscar", command=reemplazar)

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editarmenu)
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

label = Label(topSide, text="Buscar")
label.grid(row=0,column=0, sticky=W, padx=5, pady=5)

txt_buscar = Entry(topSide)
txt_buscar.grid(row=0,column=1, padx=5, pady=5)

btn_buscar=Button(topSide, text="OK", command=reemplazar)
btn_buscar.config(width=2)
btn_buscar.grid(row=0, column=2, padx=5,pady=5)

label2 = Label(topSide, text="Reemplazar Por")
label2.grid(row=0,column=3, sticky=W, padx=5, pady=5)

txt_reemplazar = Entry(topSide)
txt_reemplazar.grid(row=0,column=4, padx=5, pady=5)

btn_buscar=Button(topSide, text="OK", command=reemplazar)
btn_buscar.config(width=2)
btn_buscar.grid(row=0, column=5, padx=5,pady=5)

label2 = Label(topSide, text="Debug")
label2.grid(row=0,column=6, sticky=W, padx=5, pady=5)

btn_iniciar=Button(topSide, text="Inicio",command=iniciar_debug)
btn_iniciar.config(width=4)
btn_iniciar.grid(row=0, column=7, padx=5,pady=5)

btn_cont=Button(topSide, text="»»", command=ejec_debug)
btn_cont.config(width=2)
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
editorC3D = Text(cajaPrincipal)
editorC3D.pack(side=RIGHT)
editorC3D.config(width=30, height=25,bg="#D5DBDB",
             padx=0, pady=0, background="white")
select_font = Font(family="Helvetica", size=8, weight="normal" )
editor.tag_config('buscar', background='#ffff00', font=select_font)
font_resaltar()

editor.pack(side=LEFT)
editor.config(width=90, height=25,
             padx=0, pady=0)
editor.bind("<MouseWheel>",pintar_lineas)
editor.bind("<Key>",pintar_lineas)

rightBOTTOM=Frame(cajaInferior)
rightBOTTOM.pack(side=LEFT)
leftBOTTOM=Frame(cajaInferior)
leftBOTTOM.pack(side=RIGHT)

consola = Text(leftBOTTOM)
consola.pack(side=LEFT)
consola_font = Font(family="Helvetica", size=10, weight="normal" )
consola.config(width=95,height=11,padx=1, pady=3, font=consola_font, cursor="arrow",borderwidth=7,
                selectbackground="black",background="black", foreground="white")
#consola.insert('end','>>JPR-Compiladores1-USAC\n>>')
#consola.insert('end','>>HOla MUNDO')
consola.bind("<Return>",comando_ingresado)
consola.bind("<Key>",agregarSalto)
consola.config(insertbackground="white")

scroll2 = Scrollbar(leftBOTTOM, orient=VERTICAL)
consola.configure(yscrollcommand = scroll2.set)
scroll2.config( command = consola.yview ) 
scroll2.pack(side=RIGHT, fill=Y)
#-------------DEBUGER--------------------
#-------------------------------------------

debugger =Treeview(leftBOTTOM)
debugger["columns"]=("valor")
debugger.column("#0", width=70, minwidth=30)
debugger.column("valor", width=140, minwidth=60)

debugger.heading("#0", text="ID",anchor=W)
debugger.heading("valor", text="Valor",anchor=W)
debugger.pack(side=TOP,fill=Y)

#-------------SCROLL--------------------
scroll = Scrollbar(cajaPrincipal, orient=VERTICAL ,command=multiple_yview)
FrameLines.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)


root.mainloop()
