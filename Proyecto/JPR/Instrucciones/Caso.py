from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class Caso(Instruccion):
    def __init__(self,expresion,instrucciones,fila,columna):
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
    
    def interpretar(self,tree,table,jconsola):
        return self

    def getNodo(self):
        nodo = NodoAST("CASO")
        return nodo