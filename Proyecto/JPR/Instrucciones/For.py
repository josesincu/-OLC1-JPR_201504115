from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class For(Instruccion):
    def __init__(self,declaracion,condicion,incremento,instrucciones,fila,columna):
        self.declaracion = declaracion
        self.condicion = condicion
        self.incremento =  incremento
        self.instrucciones = instrucciones

    def interpretar(self, tree, table):
        pass
