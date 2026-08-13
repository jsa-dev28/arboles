from ej4 import Nodo

d = Nodo("D")
c = Nodo("C", izquierda=d)
e = Nodo("E")
b = Nodo("B", izquierda=c, derecha=e)
 
g = Nodo("G")
f = Nodo("F", izquierda=g)
 
raiz = Nodo("A", izquierda=b, derecha=f)