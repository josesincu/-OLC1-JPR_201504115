from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion


class Length(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla(("toLength##Param1").lower())
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de Length", self.fila, self.columna)
        
        
        if simbolo.getTipo() != TIPO.CADENA and simbolo.getTipo()!= TIPO.ARREGLO:
            return Excepcion("Semantico", "Tipo de parametro de Length  no es cadena o arreglo.", self.fila, self.columna)
        
        self.tipo = TIPO.ENTERO
        return len(simbolo.getValor())