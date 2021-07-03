from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO


class Declaracion(Instruccion):
    def __init__(self, tipo, identificador, fila, columna, expresion=None):
        self.identificador = identificador.lower()
        self.tipo = tipo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table,jconsola):
        
        if self.tipo == TIPO.VAR:
            self.tipo = TIPO.NULO
        
        value = self.expresion.interpretar(tree, table,jconsola) # Valor a asignar a la variable
        if isinstance(value, Excepcion): 
            return value

        if self.tipo == TIPO.NULO:
            simbolo = Simbolo(str(self.identificador), self.expresion.tipo, self.fila, self.columna, value)
            result = table.setTabla(simbolo)

            if isinstance(result, Excepcion): return result
            return None

        if self.tipo != self.expresion.tipo:
            return Excepcion("Semantico", "Tipo de dato diferente en Declaracion", self.fila, self.columna)

        simbolo = Simbolo(str(self.identificador), self.tipo, self.fila, self.columna, value)

        result = table.setTabla(simbolo)

        if isinstance(result, Excepcion): return result
        return None
    
    def getNodo(self):
        nodo = NodoAST("DECLARACION")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijo(str(self.identificador))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo
