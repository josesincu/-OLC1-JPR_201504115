from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Return import Return

class For(Instruccion):
    def __init__(self,declaracion,condicion,incremento,instrucciones,fila,columna):
        self.declaracion = declaracion
        self.condicion = condicion
        self.incremento =  incremento
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        #self.declaracion.interpretar(tree,table) #NUEVO ENTORNO
        nuevaTabla = TablaSimbolos(table)
        self.declaracion.interpretar(tree,nuevaTabla)
        while True:
            print(self.declaracion)
           # self.declaracion.interpretar(tree,nuevaTabla)
            estado = self.condicion.interpretar(tree,nuevaTabla)
            if isinstance(estado, Excepcion):
                return estado
            if self.condicion.tipo == TIPO.BOOLEANO:
               
                if estado == True:
                    nuevaTabl = TablaSimbolos(nuevaTabla)       #NUEVO ENTORNO
                    for instruccion in self.instrucciones:

                        result = instruccion.interpretar(tree, nuevaTabl) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): 
                            return None
                        if isinstance(result, Continue):
                            break
                        if isinstance(result,Return):
                            return result

                    self.incremento.interpretar(tree,nuevaTabl)
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
            


'''
nuevaTabla = TablaSimbolos(table)
        while True:
            
            self.declaracion.interpretar(tree,nuevaTabla)
            estado = self.condicion.interpretar(tree,nuevaTabla)
            if isinstance(estado, Excepcion):
                return estado
            if self.condicion.tipo == TIPO.BOOLEANO:
               
                if estado == True:
                    nuevaTabl = TablaSimbolos(table)       #NUEVO ENTORNO
                    for instruccion in self.instrucciones:

                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): 
                            return None
                        if isinstance(result, Continue):
                            break
                    self.incremento.interpretar(tree,nuevaTabla)
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
            
'''
