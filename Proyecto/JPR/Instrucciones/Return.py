from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos

class Return(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = None
        self.result = None

    def interpretar(self, tree, table,jconsola):
        result = self.expresion.interpretar(tree, table,jconsola)
        if isinstance(result, Excepcion): return result

        self.tipo = self.expresion.tipo #TIPO DEL RESULT
        self.result = result            #VALOR DEL RESULT

        return self
    
    def getNodo(self):
        nodo = NodoAST("RETURN")
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo