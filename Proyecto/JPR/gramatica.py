''' 
------------------------------
Jose Castro Sincu
201504115
VACACIONES DE JUNIO 2020
-------------------------------
'''
import re
from TS.Excepcion import Excepcion
#______________________________________ LEXICO ___________________________
errores = []
reservadas = {
    'int'   : 'Rint',
    'double' : 'Rdouble',
    'boolean':'Rboolean',
    'char' :'Rchar',
    'string': 'Rstring',
    'var':'Rvar',
    'if':'Rif',
    'else':'Relse',
    'print' : 'Rprint',
    'break' : 'Rbreak',
    'while' : 'Rwhile'
}

tokens  = [
    'PUNTOCOMA',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'POT',
    'MOD',
    'MENORIGUAL',
    'MENOR',
    'MAYORIGUAL',
    'MAYOR',
    'IGUALIGUAL',
    'DISTINTO',
    'AND',
    'OR',
    'NOT',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'TRUE',
    'FALSE',
    'NULL',
    'IGUAL',
    'CARACTER',
    'ID',
    'MASMAS',
    'MENOSMENOS'
] + list(reservadas.values())

# Tokens
t_PUNTOCOMA     = r';'
t_PARA          = r'\('
t_PARC          = r'\)'
t_LLAVEA        = r'{'
t_LLAVEC        = r'}'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIV           = r'/'
t_POT           = r'\*\*'
t_MOD           = r'%'
t_MENOR         = r'<'
t_MENORIGUAL    = r'<='
t_MAYOR         = r'>'
t_MAYORIGUAL    = r'>='
t_IGUALIGUAL    = r'=='
t_DISTINTO      = r'=!'
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_IGUAL         = r'='
t_MASMAS        = r'\+\+'
t_MENOSMENOS    = r'--'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Double value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_TRUE(t):
    r'true'
    try:
        t.value = True
    except ValueError:
        print('Error no se puede convertir a booleano esto %d',t.value)
        t.value = None
    return t

def t_FALSE(t):
    r'false'
    try:
        t.value = False
    except ValueError:
        print('Error no se puede convertir a booleano esto %d',t.value)
        t.value = None
    return t

def t_ID(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_CARACTER(t):
    r'\'.\''
    t.value = t.value[1:-1] # remuevo las comillas simples
    return t
# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex(reflags=re.IGNORECASE)


#______________________ Asociación de operadores y precedencia ____________________________
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UNOT'),
    ('left','IGUALIGUAL','DISTINTO', 'MENOR','MENORIGUAL','MAYOR','MAYORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','DIV','POR','MOD'),
    ('right','UMENOS'),
    )



# Definición de la gramática

#_______________________________  Abstract ______________________________________
from Abstract.Instruccion import Instruccion
#_______________________________ TIPOS DE INSTRUCCION ___________________________
from Instrucciones.Imprimir import Imprimir
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Asignacion import Asignacion
from Instrucciones.If import If
from Instrucciones.Break import Break
from Instrucciones.While import While
from Instrucciones.Incremento import Incremento


#________________________________ OPERADORES Y TABLA SE SIMBOLO ___________________
from TS.Tipo import OperadorAritmetico, TIPO,OperadorRelacional,OperadorLogico,OperadorIncremento

#________________________________ TIPOS DE EXPRESIONES ____________________________
from Expresiones.Primitivos import Primitivos
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Expresiones.Identificador import Identificador

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t) :
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    
#_______________________________________ INSTRUCCIONES _________________________________

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

#_______________________________________ INSTRUCCION ___________________________________

def p_instruccion(t) :
    '''instruccion      : imprimir_instr
                        | declaracion
                        | asignacion
                        | if
                        | break 
                        | while
                        | tipo_incremento '''
    t[0] = t[1]

def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
    errores.append(Excepcion("Sintáctico","Error Sintáctico." + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""
#_______________________________________ IMPRIMIR ______________________________________

def p_imprimir(t) :
    'imprimir_instr : Rprint PARA expresion PARC fin_instr'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))

#_______________________________________ DECLARACION __________________________________
def p_declaracion(t):
    'declaracion     : tipo ID IGUAL expresion fin_instr'
    t[0] = Declaracion(t[1], t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])

def p_tipo(t):
    '''tipo : Rint
            | Rdouble
            | Rstring
            | Rboolean
            | Rchar 
            | Rvar '''

    if t[1] == 'int':
        t[0] = TIPO.ENTERO
    elif t[1] == 'double':
        t[0] = TIPO.DECIMAL
    elif t[1] == 'string':
        t[0] = TIPO.CADENA
    elif t[1] == 'boolean':
        t[0] = TIPO.BOOLEANO
    elif t[1] == 'char':
        t[0] = TIPO.CHARACTER
    elif t[1] == 'var':
        t[0] = TIPO.VAR
#_______________________________________ ASIGNACION __________________________________
def p_asignacion(t):
    ''' asignacion : ID IGUAL  expresion fin_instr'''
    t[0] =  Asignacion(t[1],t[3],t.lineno(1), find_column(input, t.slice[1]))
#_______________________________________ IF _________________________________________
def p_if(t) :
    'if     : Rif PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_if_else(t) :
    'if     : Rif PARA expresion PARC LLAVEA instrucciones LLAVEC Relse LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], t[10], None, t.lineno(1), find_column(input, t.slice[1]))

def p_if_elseIf_else(t) :
    'if     : Rif PARA expresion PARC LLAVEA instrucciones LLAVEC Relse if'
    t[0] = If(t[3], t[6], None, t[9], t.lineno(1), find_column(input, t.slice[1]))

#______________________________________ BREAK ________________________________________
def p_break(t):
    'break : Rbreak fin_instr'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))

#______________________________________ WHILE _______________________________________
def p_while(t):
    ''' while : Rwhile PARA expresion PARC LLAVEA instrucciones LLAVEC '''
    t[0] = While(t[3],t[6],t.lineno(1), find_column(input, t.slice[1]))

#______________________________________ TIPO INCREMENTO _____________________________
def p_incrementos(t):
    ''' tipo_incremento : ID MASMAS fin_instr
                        | ID MENOSMENOS fin_instr '''
    if t[2]=='++':
        t[0] = Incremento(t[1],OperadorIncremento.MASMAS,t.lineno(1), find_column(input, t.slice[1]))
    elif t[2]=='--':
        t[0] = Incremento(t[1],OperadorIncremento.MENOSMENOS,t.lineno(1), find_column(input, t.slice[1]))

#_______________________________________ PUNTO COMA __________________________________
def p_puntocoma(t):
    ''' fin_instr : PUNTOCOMA
                    | '''
    t[0]=None

#_______________________________________ EXPRESION ____________________________________

def p_expresion_binaria(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion POT expresion
            | expresion MOD expresion
            | expresion MENORIGUAL expresion
            | expresion MENOR expresion
            | expresion MAYORIGUAL expresion
            | expresion MAYOR expresion
            | expresion IGUALIGUAL expresion
            | expresion DISTINTO expresion
            | expresion AND expresion
            | expresion OR expresion
    '''
    if t[2] == '+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '**':
        t[0] = Aritmetica(OperadorAritmetico.POT,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MOD,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENOR,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENORIGUAL,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYOR,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '=!':
        t[0] = Relacional(OperadorRelacional.DISTINTO,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR,t[1],t[3],t.lineno(2), find_column(input, t.slice[2]))
    
  
def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS 
            | NOT expresion %prec UNOT 
    '''
    if t[1] == '-':
        t[0] = Aritmetica(OperadorAritmetico.UMENOS, t[2],None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Logica(OperadorLogico.NOT, t[2],None, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_parentesis(t):
    ''' expresion : PARA expresion PARC '''
    t[0] = t[2]

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(TIPO.ENTERO,t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(TIPO.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(TIPO.CADENA,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_true(t):
    '''expresion : TRUE'''
    t[0] = Primitivos(TIPO.BOOLEANO,t[1],t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_false(t):
    '''expresion : FALSE'''
    t[0] = Primitivos(TIPO.BOOLEANO,t[1],t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_caracter(t):
    '''expresion : CARACTER'''
    t[0] = Primitivos(TIPO.CHARACTER,t[1],t.lineno(1), find_column(input, t.slice[1]))
def p_identificador(t):
    '''expresion : ID '''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))


import ply.yacc as yacc
parser = yacc.yacc()

input = ''

def getErrores():
    return errores

def parse(inp) :
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex()
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

#INTERFAZ

f = open("./entrada.txt", "r")
entrada = f.read()

from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos

instrucciones = parse(entrada) #ARBOL AST
ast = Arbol(instrucciones)
TSGlobal = TablaSimbolos()
ast.setTSglobal(TSGlobal)
for error in errores:                   #CAPTURA DE ERRORES LEXICOS Y SINTACTICOS
    ast.getExcepciones().append(error)
    ast.updateConsola(error.toString())

for instruccion in ast.getInstrucciones():      # REALIZAR LAS ACCIONES
    value = instruccion.interpretar(ast,TSGlobal)
    if isinstance(value, Excepcion) :
        ast.getExcepciones().append(value)
        ast.updateConsola(value.toString())

print(ast.getConsola())