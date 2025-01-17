from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST

class Primitivos(Instruccion):
    def __init__(self, tipo, valor, fila, columna):
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.arreglo = False

    def interpretar(self, tree, table,jconsola):
        
        return self.valor
    
    def getNodo(self):
        nodo = NodoAST("PRIMITIVO")
        nodo.agregarHijo(str(self.valor))
        return nodo
