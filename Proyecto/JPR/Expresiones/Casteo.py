from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorLogico

class Casteo(Instruccion):
    def __init__(self, tipo, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    
    def interpretar(self, tree, table):
        val = self.expresion.interpretar(tree, table)
        if self.tipo == TIPO.DECIMAL:
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Float. entero", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.CADENA:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Float Cadena.", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.CHARACTER:
                try:
                    return float(ord(self.obtenerVal(self.expresion.tipo,val)))
                except:
                    return Excepcion("Semantico", "No se puede castear para Float Char.", self.fila, self.columna)

            return Excepcion("Semantico", "Tipo Erroneo de casteo para Double.", self.fila, self.columna)
        if self.tipo == TIPO.ENTERO:
            if self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Int. en decimal", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.CADENA:
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Int en cadena.", self.fila, self.columna)
            elif self.expresion.tipo == TIPO.CHARACTER:
                try:
                    return int(ord(self.obtenerVal(self.expresion.tipo,val)))
                except:
                    return Excepcion("Semantico", "No se puede castear para Int en caracter.", self.fila, self.columna)

            return Excepcion("Semantico", "Tipo Erroneo de casteo para Int.", self.fila, self.columna)
        if self.tipo == TIPO.CADENA:
            if self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para String. en decimal", self.fila, self.columna)
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para String. en entero", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para String.", self.fila, self.columna)
            
        if self.tipo == TIPO.CHARACTER:
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return chr(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para caracter. en decimal", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Caracter.", self.fila, self.columna)
        if self.tipo == TIPO.BOOLEANO:
            if self.expresion.tipo == TIPO.CADENA:
                try:
                    return bool(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para booleano. en decimal", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Caracter.", self.fila, self.columna)
        return Excepcion("Semantico", "Tipo "+str(self.tipo)+" No Forma Parte de Casteo.", self.fila, self.columna)


        
    def getNodo(self):
        nodo = NodoAST("CASTEO")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo

    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)