from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO

class Imprimir(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table,jconsola):
        value = self.expresion.interpretar(tree, table,jconsola)  # RETORNA CUALQUIER VALOR
        if isinstance(value, Excepcion) :
            return value
        
        if self.expresion.tipo == TIPO.ARREGLO:
            return Excepcion("Semantico", "No se puede imprimir un arreglo completo", self.fila, self.columna)
        
        jconsola.insert('insert',">>"+str(value)+"\n")
        jconsola.see("end")
        #tree.updateConsola(value)
    
    def getNodo(self):
        nodo = NodoAST("IMPRIMIR")
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo