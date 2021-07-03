from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
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

    def interpretar(self, tree, table,jconsola):
        #self.declaracion.interpretar(tree,table) #NUEVO ENTORNO
        nuevaTabla = TablaSimbolos(table)
        self.declaracion.interpretar(tree,nuevaTabla,jconsola)
        while True:
            
            estado = self.condicion.interpretar(tree,nuevaTabla,jconsola)
            if isinstance(estado, Excepcion):
                return estado
            if self.condicion.tipo == TIPO.BOOLEANO:
               
                if estado == True:
                    nuevaTabl = TablaSimbolos(nuevaTabla)       #NUEVO ENTORNO
                    for instruccion in self.instrucciones:

                        result = instruccion.interpretar(tree, nuevaTabl,jconsola) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            #tree.updateConsola(result.toString())
                            jconsola.insert('insert',">>"+result.toString()+"\n")
                        if isinstance(result, Break): 
                            return None
                        if isinstance(result, Continue):
                            break
                        if isinstance(result,Return):
                            return result

                    self.incremento.interpretar(tree,nuevaTabl,jconsola)
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
    
    def getNodo(self):
        nodo = NodoAST("FOR")
        nodo.agregarHijoNodo(self.declaracion.getNodo())
        nodo.agregarHijoNodo(self.condicion.getNodo())
        nodo.agregarHijoNodo(self.incremento.getNodo())

        instrucciones = NodoAST("INSTRUCCIONES FOR")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo