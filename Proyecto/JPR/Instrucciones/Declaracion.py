from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO

class Declaracion(Instruccion):
    def __init__(self,tipo,id,expresion = None,fila,columna)
        self.tipo = tipo
        self.id = id
        self.fila = fila
        self.columna = columna
    
    def interpretar(self,tree,table):
        value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
        if isinstance(value, Excepcion): return value

        if self.tipo != self.expresion.tipo:
            return Excepcion("Semantico", "Tipo de dato diferente en Declaracion", self.fila, self.columna)

        simbolo = Simbolo(str(self.identificador), self.tipo, self.fila, self.columna, value)

        result = table.setTabla(simbolo)

        if isinstance(result, Excepcion): return result
        return None
