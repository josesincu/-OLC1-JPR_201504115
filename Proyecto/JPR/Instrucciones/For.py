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
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        self.declaracion.interpretar(tree,table)
        
        while True:
            estado = self.condicion.interpretar(tree,table)
            if isinstance(estado, Excepcion):
                return estado
            if self.condicion.tipo == TIPO.BOOLEANO:
                if estado == True:
                    nuevaTabla = TablaSimbolos(table)       #NUEVO ENTORNO
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                    self.incremento.interpretar(tree,table)
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
            

