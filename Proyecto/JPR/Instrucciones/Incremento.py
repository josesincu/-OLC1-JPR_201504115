from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
from TS.Tipo import OperadorIncremento


class Incremento(Instruccion):
    def __init__(self, identificador,tipo_aumento, fila, columna):
        self.identificador = identificador
        self.tipo_aumento = tipo_aumento
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        temp_simbolo = table.getTabla(self.identificador)
        
        if self.tipo_aumento == OperadorIncremento.MASMAS:
            temp_simbolo.valor = temp_simbolo.valor+1
        elif  self.tipo_aumento == OperadorIncremento.MENOSMENOS:
            temp_simbolo.valor = temp_simbolo.valor-1
        #simbolo = Simbolo(self.identificador, self.expresion.tipo, self.fila, self.columna, value)
        result = table.actualizarTabla(temp_simbolo)

        if isinstance(result, Excepcion): return result
        return None