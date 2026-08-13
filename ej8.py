from ej4 import Nodo

nodo_2a = Nodo(2)
nodo_6 = Nodo(6)
nodo_suma = Nodo("+", izquierda=nodo_2a, derecha=nodo_6)
nodo_8 = Nodo(8)
nodo_div = Nodo("/", izquierda=nodo_suma, derecha=nodo_8)
 
nodo_9 = Nodo(9)
nodo_2b = Nodo(2)
nodo_resta = Nodo("-", izquierda=nodo_9, derecha=nodo_2b)
 
raiz_expresion = Nodo("*", izquierda=nodo_div, derecha=nodo_resta)

def pre_order(nodo):
    if nodo is None:
        return ""
    if nodo.izquierda is None and nodo.derecha is None:
        return str(nodo.valor)
    return f"{nodo.valor} {pre_order(nodo.izquierda)} {pre_order(nodo.derecha)}"
 
 
def post_order(nodo):
    if nodo is None:
        return ""
    if nodo.izquierda is None and nodo.derecha is None:
        return str(nodo.valor)
    return f"{post_order(nodo.izquierda)} {post_order(nodo.derecha)} {nodo.valor}"
 
 
def in_order(nodo):
    if nodo is None:
        return ""
    if nodo.izquierda is None and nodo.derecha is None:
        return str(nodo.valor)
    return f"({in_order(nodo.izquierda)} {nodo.valor} {in_order(nodo.derecha)})"

if __name__ == "__main__":
    print("Expresión en prefijo:", pre_order(raiz_expresion))
    print("Expresión en postfijo:", post_order(raiz_expresion))
    print("Expresión en infijo:", in_order(raiz_expresion))