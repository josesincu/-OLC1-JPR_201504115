from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion


class TypeOf(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla(("totypeof##Param1").lower())
        cadena = ""
        if simbolo == None : 
            return Excepcion("Semantico", "No se encontró el parámetro de Typeof", self.fila, self.columna)
        if simbolo.getTipo() == TIPO.DECIMAL:
            cadena = "DOUBLE"
        elif simbolo.getTipo() == TIPO.ENTERO:
            cadena = "INT"
        elif simbolo.getTipo() == TIPO.BOOLEANO:
            cadena = "BOOLEAN"
        elif simbolo.getTipo() == TIPO.CADENA:
            cadena = "STRING"
        elif simbolo.getTipo() == TIPO.CHARACTER:
            cadena = "CHAR"        
        self.tipo = TIPO.CADENA
        return str(cadena)