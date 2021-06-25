from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO


class Declaracion_sinAsignacion(Instruccion):
    def __init__(self, tipo, identificador, fila, columna):
        self.identificador = identificador.lower()
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        

    def interpretar(self, tree, table):
        if self.tipo == TIPO.VAR:
            self.tipo = TIPO.NULO
        simbolo = Simbolo(str(self.identificador), self.tipo, self.fila, self.columna,None)

        result = table.setTabla(simbolo)

        if isinstance(result, Excepcion): 
            return result
        return None
    
    def getNodo(self):
        nodo = NodoAST("DECLARACION_SINAGNACION")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijo(str(self.identificador))
        return nodo
