from TS.Tipo import TIPO
#from Instrucciones.Return import Return
from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Return import Return


class Funcion(Instruccion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table,jconsola):
        nuevaTabla = TablaSimbolos(table,"FUNCION "+self.nombre.upper()) 
        for instruccion in self.instrucciones:      # REALIZAR LAS ACCIONES
            value = instruccion.interpretar(tree,nuevaTabla,jconsola)
            if isinstance(value, Excepcion) :
                tree.getExcepciones().append(value)
                #tree.updateConsola(value.toString())
                jconsola.insert('insert',">>"+value.toString()+"\n")
            if isinstance(value, Break): 
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.getExcepciones().append(err)
                #tree.updateConsola(err.toString())
                jconsola.insert('insert',">>"+err.toString()+"\n")
            if isinstance(value, Return):
                self.tipo = value.tipo
                return value.result
            
        return None
    
    def getNodo(self):
        nodo = NodoAST("FUNCION")
        nodo.agregarHijo(str(self.nombre))
        parametros = NodoAST("PARAMETROS")
        for param in self.parametros:
            parametro = NodoAST("PARAMETRO")
            parametro.agregarHijo(param["tipo"])
            parametro.agregarHijo(param["identificador"])
            parametros.agregarHijoNodo(parametro)
        nodo.agregarHijoNodo(parametros)

        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo
