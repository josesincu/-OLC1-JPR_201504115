from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO

#___________________ IMPORT DIALOG PARA READ _________________________
from tkinter import simpledialog

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA

    def interpretar(self, tree, table,jconsola):
        lectura = simpledialog.askstring("Input", "Ver consola")
        if lectura is not None:
            jconsola.insert('insert',">>"+str(lectura)+"\n")
            return lectura 
        else:
            return Excepcion("Semantico", "Valor no Aceptable en read.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("READ")
        return nodo