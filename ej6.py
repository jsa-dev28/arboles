from ej4 import Nodo

d = Nodo("D")
c = Nodo("C", izquierda=d)
e = Nodo("E")
b = Nodo("B", izquierda=c, derecha=e)
 
g = Nodo("G")
f = Nodo("F", izquierda=g)
 
raiz = Nodo("A", izquierda=b, derecha=f)

def pre_order(nodo, resultado=None):
    if resultado is None:
        resultado = []
    if nodo is not None:
        resultado.append(nodo.valor)
        pre_order(nodo.izquierda, resultado)
        pre_order(nodo.derecha, resultado)
    return resultado
 
 
def in_order(nodo, resultado=None):
    if resultado is None:
        resultado = []
    if nodo is not None:
        in_order(nodo.izquierda, resultado)
        resultado.append(nodo.valor)
        in_order(nodo.derecha, resultado)
    return resultado
 
 
def post_order(nodo, resultado=None):
    if resultado is None:
        resultado = []
    if nodo is not None:
        post_order(nodo.izquierda, resultado)
        post_order(nodo.derecha, resultado)
        resultado.append(nodo.valor)
    return resultado
 
 
def level_order(nodo):
    resultado = []
    if nodo is None:
        return resultado
 
    cola = [nodo]
    while len(cola) > 0:
        actual = cola.pop(0)
        resultado.append(actual.valor)
        if actual.izquierda is not None:
            cola.append(actual.izquierda)
        if actual.derecha is not None:
            cola.append(actual.derecha)
 
    return resultado

if __name__ == "__main__":
    print("Pre-order:", pre_order(raiz))
    print("In-order:", in_order(raiz))
    print("Post-order:", post_order(raiz))
    print("Level-order:", level_order(raiz))