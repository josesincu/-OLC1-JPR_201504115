from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Return import Return

class While(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table,jconsola):
        while True:
            condicion = self.condicion.interpretar(tree, table,jconsola)
            if isinstance(condicion, Excepcion): return condicion

            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION
                    nuevaTabla = TablaSimbolos(table,"WHILE")       #NUEVO ENTORNO
                    for instruccion in self.instrucciones:
                        
                        result = instruccion.interpretar(tree, nuevaTabla,jconsola) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            #tree.updateConsola(result.toString())
                            jconsola.insert('insert',">>"+result.toString()+"\n")
                        if isinstance(result, Break): 
                            return None
                        if isinstance(result,Continue):
                            break
                        if isinstance(result,Return):
                            return result
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)
    
    def getNodo(self):
        nodo = NodoAST("WHILE")

        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo