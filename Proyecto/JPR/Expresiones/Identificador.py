from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST


class Identificador(Instruccion):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador.lower()
        self.fila = fila
        self.columna = columna
        self.tipo = None
        self.arreglo = False

    def interpretar(self, tree, table,jconsola):
        simbolo = table.getTabla(self.identificador)
        if simbolo == None:
            return Excepcion("Semantico", "Variable " + self.identificador + " no encontrada.", self.fila, self.columna)
        self.tipo = simbolo.getTipo()
        self.arreglo = simbolo.getArreglo()
        return simbolo.getValor()

    def getNodo(self):
        nodo = NodoAST("IDENTIFICADOR")
        nodo.agregarHijo(str(self.identificador))
        return nodo
        
    
        