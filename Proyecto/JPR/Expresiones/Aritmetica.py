from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorAritmetico

class Aritmetica(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = None
        self.arreglo = False

    
    def interpretar(self, tree, table,jconsola):
        izq = self.OperacionIzq.interpretar(tree, table,jconsola)
        if isinstance(izq, Excepcion): return izq
        if self.OperacionDer != None:
            der = self.OperacionDer.interpretar(tree, table,jconsola)
            if isinstance(der, Excepcion): return der


        if self.operador == OperadorAritmetico.MAS: #SUMA
            #I-----------------INT VRS TIPOS------------------------------------
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                #int + int
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                #int + double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                 #int + boolean
                self.tipo = TIPO.ENTERO
                boleano_entero = 0
                if(self.obtenerVal(self.OperacionDer.tipo, der)):
                    boleano_entero = 1
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + boleano_entero
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.CADENA:
                #int + string
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
           
            #---------------------------- double vrs tipos  -------------------------------
            if self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                #double + int
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                #double + double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO:
                 #double + boolean
                self.tipo = TIPO.DECIMAL
                boleano_entero = 0
                if(self.obtenerVal(self.OperacionDer.tipo, der)):
                    boleano_entero = 1
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + boleano_entero
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.CADENA:
                #double + string
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)

            #--------------------------- boolean vrs tipos ----------------------------------
            if self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO:
                #boolean + int
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL:
                #boolean + double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                 #boolean + boolean
                self.tipo = TIPO.DECIMAL
                boleano_izq = 0
                boleano_der = 0
                if(self.obtenerVal(self.OperacionDer.tipo, der)):
                    boleano_der = 1
                if(self.obtenerVal(self.OperacionIzq.tipo, izq)):
                    boleano_izq = 1
                return boleano_izq + boleano_der
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.CADENA:
                #boolean + string
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            
            #----------------------- char vrs tipos -----------------------------------------
            if self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CHARACTER:
                #char + char
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CADENA:
                #char +string
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            
            #------------------------ string vrs tipos ---------------------------------------
            if self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:
                #cadena + int
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:
                #cadena + double
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.BOOLEANO:
                 #cadena + boolean
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CHARACTER:
                #cadena + char
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA:
                #cadena + cadena
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            return Excepcion("Semantico", "Tipo Erroneo de operacion para +.", self.fila, self.columna)

        elif self.operador == OperadorAritmetico.MENOS: #RESTA
            #------------------------------ int vrs tipos ----------------------------------
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                # int  - int 
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                #int - double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                #int - boolean
                self.tipo = TIPO.ENTERO
                boleano_entero = 0
                if(self.obtenerVal(self.OperacionDer.tipo, der)):
                    boleano_entero = 1
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - boleano_entero
            
            #-------------------------------double vrs tipos --------------------------------
            if self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                #double - int
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                #double - double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO:
                #double - boolean
                self.tipo = TIPO.DECIMAL
                boleano_entero = 0
                if(self.obtenerVal(self.OperacionDer.tipo, der)):
                    boleano_entero = 1
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - boleano_entero
            #---------------------------- boolean vrs tipos ------------------------------------
            if self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO:
                #boolean - int
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL:
                #boolean - double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para -.", self.fila, self.columna)
        
        elif self.operador == OperadorAritmetico.POR: #Multiplicacion
            #--------------------------- int vrs tipos ------------------------------------
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                #int * int
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                #int * double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)

            #-------------------------- double vrs tipos -------------------------------------
            if self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                #double * int
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                #double * double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para *.", self.fila, self.columna)

        elif self.operador == OperadorAritmetico.DIV: #Division
            #--------------------------- int vrs tipos ------------------------------------
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                #int / int
                self.tipo = TIPO.DECIMAL
                return float(self.obtenerVal(self.OperacionIzq.tipo, izq)) / float(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                #int / double
                self.tipo = TIPO.DECIMAL
                return float(self.obtenerVal(self.OperacionIzq.tipo, izq)) / float(self.obtenerVal(self.OperacionDer.tipo, der))

            #-------------------------- double vrs tipos -------------------------------------
            if self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                #double / int
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                #double / double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para /.", self.fila, self.columna)
        
        elif self.operador == OperadorAritmetico.POT: #POTENCIA
            #--------------------------- int vrs tipos ------------------------------------
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                #int ** int
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                #int ** double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)

            #-------------------------- double vrs tipos -------------------------------------
            if self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                #double ** int
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                #double ** double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para **.", self.fila, self.columna)
        
        elif self.operador == OperadorAritmetico.MOD: #MODULO
            #--------------------------- int vrs tipos ------------------------------------
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                #int % int
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                #int % double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)

            #-------------------------- double vrs tipos -------------------------------------
            if self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                #double % int
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                #double % double
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para %.", self.fila, self.columna)
        if self.operador == OperadorAritmetico.UMENOS: #NEGACION UNARIA
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para - unario.", self.fila, self.columna)
        return Excepcion("Semantico", "Tipo de Operacion no Especificado.", self.fila, self.columna)



    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            
                
            return bool(val)
        return str(val)
    
    def getNodo(self):
        nodo = NodoAST("ARITMETICA")
        if self.OperacionDer != None:
            nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.OperacionDer.getNodo())
        else:
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
        
        return nodo
        