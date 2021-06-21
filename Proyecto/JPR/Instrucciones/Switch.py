from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Expresiones.Identificador import Identificador


class Switch(Instruccion):
    def __init__(self,expresion,listaCaso,casoDefault,fila,columna):
        self.expresion = expresion  #2
        self.listaCaso = listaCaso
        self.casoDefault = casoDefault
        self.fila = fila
        self.columna = columna
    
    def interpretar(self,tree,table):
        #valor_expresion = 
        self.expresion.interpretar(tree,table)
        #if isinstance(valor_expresion,int):
        #    print("soy entero")
        #elif isinstance(valor_expresion,str):
        #    print("soy string")
        #elif isinstance(valor_expresion,float):
        #   print("soy flotante")
        hayBreak = False
        ejecutado = False
        cont = 1

        for x in range(0,len(self.listaCaso),1):

            if self.expresion.tipo == TIPO.ENTERO and self.listaCaso[x].expresion.tipo == TIPO.ENTERO :
                #__________________________entero == entero && entero == entero
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if valor_expresion == valor_caso:
                    
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None

            elif self.expresion.tipo == TIPO.ENTERO and self.listaCaso[x].expresion.tipo == TIPO.DECIMAL :
                #__________________________entero == entero && decimal == decimal
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if valor_expresion == float(valor_caso):
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None

            elif self.expresion.tipo == TIPO.ENTERO and self.listaCaso[x].expresion.tipo == TIPO.CADENA :
                #__________________________entero == entero && cadeba == cadena
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if str(valor_expresion) == valor_caso:
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None

            elif self.expresion.tipo == TIPO.DECIMAL and self.listaCaso[x].expresion.tipo == TIPO.ENTERO :
                #__________________________ decimal == decimal && entero == entero
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if valor_expresion == float(valor_caso):
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None
            
            elif self.expresion.tipo == TIPO.DECIMAL and self.listaCaso[x].expresion.tipo == TIPO.DECIMAL :
                #__________________________ decimal == decimal && decimal == decimal
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if valor_expresion == valor_caso:
                    ejecutado = True
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None
            
            elif self.expresion.tipo == TIPO.DECIMAL and self.listaCaso[x].expresion.tipo == TIPO.CADENA :
                #__________________________ decimal == decimal && cadena == cadena
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if str(valor_expresion) == valor_caso:
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None
            
            elif self.expresion.tipo == TIPO.BOOLEANO and self.listaCaso[x].expresion.tipo == TIPO.BOOLEANO :
                #__________________________ boleano == boleano && boleano == boleano
                
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if valor_expresion == valor_caso:
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None
            
            elif self.expresion.tipo == TIPO.BOOLEANO and self.listaCaso[x].expresion.tipo == TIPO.CADENA :
                #__________________________ boleano == boleano && cadena == cadena
                
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if str(valor_expresion) == valor_caso:
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None
            
            elif self.expresion.tipo == TIPO.CHARACTER and self.listaCaso[x].expresion.tipo == TIPO.CHARACTER :
                #__________________________ caracter == caracter && caracter == caracter
                
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if valor_expresion == valor_caso:
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None
            
            elif self.expresion.tipo == TIPO.CADENA and self.listaCaso[x].expresion.tipo == TIPO.ENTERO :
                #__________________________ cadena == cadena && int == int
                
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if valor_expresion == str(valor_caso):
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None
            
            elif self.expresion.tipo == TIPO.CADENA and self.listaCaso[x].expresion.tipo == TIPO.DECIMAL :
                #__________________________ cadena == cadena && decimal == decimal
                
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if valor_expresion == str(valor_caso):
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None
            
            elif self.expresion.tipo == TIPO.CADENA and self.listaCaso[x].expresion.tipo == TIPO.BOOLEANO :
                #__________________________ cadena == cadena && booleano == boleano
                
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if valor_expresion == str(valor_caso):
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None

            elif self.expresion.tipo == TIPO.CADENA and self.listaCaso[x].expresion.tipo == TIPO.CADENA :
                #__________________________ cadena == cadena && cadena == cadena
                
                valor_expresion = self.expresion.interpretar(tree,table)
                if isinstance(valor_expresion,Excepcion):
                    return valor_expresion
                valor_caso = self.listaCaso[x].expresion.interpretar(tree,table)
                if isinstance(valor_caso,Excepcion):
                    return valor_caso
                if valor_expresion == valor_caso:
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.listaCaso[x].instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break):
                            hayBreak = True
                            ejecutado = True
                            return None
            

            if hayBreak == False and (x<len(self.listaCaso)):
               #caso_temp = self.listaCaso[cont]
               #cont = cont+1
               ejecutado = False
               #self.expresion = caso_temp.expresion
            
            
            #return Excepcion("Semantico", "Tipo Erroneo de operacion para ==.", self.fila, self.columna)
        
        if ejecutado == False and self.casoDefault != None:
            nuevaTabla = TablaSimbolos(table)
            for instruccion in self.casoDefault:
                result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                if isinstance(result, Excepcion) :
                    tree.getExcepciones().append(result)
                    tree.updateConsola(result.toString())
                if isinstance(result, Break):
                    hayBreak = True
                    ejecutado = True
                    return None

        
            

                
            
            


        
        
                


    
