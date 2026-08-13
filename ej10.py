import ej8
import ej9
def calculate(nodo):
    if nodo is None:
        return 0
    
    if nodo.izquierda is None and nodo.derecha is None:
        return nodo.valor
 
    valor_izquierda = calculate(nodo.izquierda)
    valor_derecha = calculate(nodo.derecha)
 
    if nodo.valor == "+":
        return valor_izquierda + valor_derecha
    elif nodo.valor == "-":
        return valor_izquierda - valor_derecha
    elif nodo.valor == "*":
        return valor_izquierda * valor_derecha
    elif nodo.valor == "/":
        return valor_izquierda / valor_derecha
    else:
        raise ValueError(f"Operador desconocido: {nodo.valor}")
    
if __name__ == "__main__":
    resultado = calculate(ej8.raiz_expresion)
    print("Resultado de la expresión:", resultado)
    resultado = calculate(ej9.inverse_polish_parser("4 5 + 5 3 - *"))
    print("Resultado de la expresión en notación polaca inversa:", resultado)