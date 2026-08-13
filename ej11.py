from ej9 import inverse_polish_parser
import ej10

def evaluate(expresion):
    arbol = inverse_polish_parser(expresion)
    return ej10.calculate(arbol)

print("evaluate('4 5 + 5 3 - *') =", evaluate("4 5 + 5 3 - *"))