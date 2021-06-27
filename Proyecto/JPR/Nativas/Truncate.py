from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion
import math #libreria para truncate


class Truncate(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        print(self.nombre)
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla(("toTruncate##Param1").lower())
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de truncate", self.fila, self.columna)

        if simbolo.getTipo() != TIPO.DECIMAL and simbolo.getTipo() != TIPO.ENTERO:
            return Excepcion("Semantico", "Tipo de parametro de truncate no es un decimal o entero.", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        return math.trunc(simbolo.getValor())