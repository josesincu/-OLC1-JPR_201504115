from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion

#___________________ IMPORT DIALOG PARA READ _________________________
from tkinter import simpledialog

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA

    def interpretar(self, tree, table):
        #print(tree.getConsola()) #IMPRIME LA CONSOLA
        #print("Ingreso a un READ. Ingrese el valor")
        #tree.setConsola("")     #RESETEA LA CONSOLA
        # ESTO SOLO ES DE EJEMPLO
        #lectura = input() # OBTENERME EL VALOR INGRESADO
        #return lectura
        lectura = simpledialog.askstring("Input", "Ingresa el valor que se te pide en consola")
        if lectura is not None:
            return lectura 
        else:
            return Excepcion("Semantico", "Valor no Aceptable en read.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("READ")
        return nodo