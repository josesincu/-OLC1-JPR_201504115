from enum import Enum

class TIPO(Enum):
    ENTERO = 1
    DECIMAL = 2
    BOOLEANO = 3
    CHARACTER = 4
    CADENA = 5
    NULO = 6
    ARREGLO = 7
    VAR = 8
    CUALQUIERA = 9

class OperadorAritmetico(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIV = 4
    POT = 5
    MOD = 6
    UMENOS = 7

class OperadorRelacional(Enum):
    MENOR = 1
    MAYOR = 2
    MENORIGUAL = 3
    MAYORIGUAL = 4
    IGUALIGUAL = 5
    DISTINTO = 6

class OperadorLogico(Enum):
    NOT = 1
    AND = 2
    OR = 3
class OperadorIncremento(Enum):
    MASMAS = 1
    MENOSMENOS = 2