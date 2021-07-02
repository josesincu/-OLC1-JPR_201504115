from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion

from decimal import Decimal, ROUND_HALF_UP


class Round(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
    

    def interpretar(self, tree, table):
        simbolo = table.getTabla(("toRound##Param1").lower())
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de Round", self.fila, self.columna)

        
        if simbolo.getTipo() != TIPO.DECIMAL and simbolo.getTipo() != TIPO.ENTERO:
            return Excepcion("Semantico", "Tipo de parametro de Rouend  no es enetero o decimal.", self.fila, self.columna)
        
        self.tipo = TIPO.ENTERO
        return Decimal(simbolo.getValor()).quantize(0, ROUND_HALF_UP)
    
    
