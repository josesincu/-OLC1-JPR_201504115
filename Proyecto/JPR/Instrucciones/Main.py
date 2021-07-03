from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Declaracion import Declaracion

class Main(Instruccion):
    def __init__(self, instrucciones, fila, columna):
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table,jconsola):
        nuevaTabla = TablaSimbolos(table,"Main")
        for instruccion in self.instrucciones:      # REALIZAR LAS ACCIONES
            value = instruccion.interpretar(tree,nuevaTabla,jconsola)
            if isinstance(instruccion,Declaracion):
                tree.addSim_Tabla((instruccion.identificador,"Variable","----","Main",instruccion.expresion,instruccion.fila,instruccion.columna))
            if isinstance(value, Excepcion) :
                tree.getExcepciones().append(value)
                #tree.updateConsola(value.toString())
                jconsola.insert('insert',">>"+value.toString()+"\n")
            if isinstance(value, Break): 
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.getExcepciones().append(err)
                #tree.updateConsola(err.toString())
                jconsola.insert('insert',">>"+value.toString()+"\n")
    
    def getNodo(self):
        nodo = NodoAST("MAIN")

        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo