from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion


class ToUpper(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table,jconsola):
        simbolo = table.getTabla(("toUpper##Param1").lower())
        
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de ToUpper", self.fila, self.columna)

        if simbolo.getTipo() != TIPO.CADENA:
            return Excepcion("Semantico", "Tipo de parametro de ToUpper no es cadena.", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        return simbolo.getValor().upper()