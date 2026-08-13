from ej4 import Nodo
import ej8 

class Stack:
    def __init__(self):
        self.elementos = []
 
    def push(self, valor):
        self.elementos.append(valor)
 
    def pop(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop()
 
    def esta_vacia(self):
        return len(self.elementos) == 0

def es_operador(token):
    return token in ("+", "-", "*", "/")

def inverse_polish_parser(expresion):
    pila = Stack()
    tokens = expresion.split()

    for token in tokens:
        if es_operador(token):
            derecha = pila.pop()
            izquierda = pila.pop()
            nuevo_nodo = Nodo(token, izquierda=izquierda, derecha=derecha)
            pila.push(nuevo_nodo)
        else:
            numero = float(token)
            if numero == int(numero):
                numero = int(numero)
            pila.push(Nodo(numero))

    return pila.pop()

if __name__ == "__main__":
    expresion = "4 5 + 5 3 - *"
    raiz = inverse_polish_parser(expresion)
    print("Árbol construido a partir de la expresión en notación polaca inversa:")
    def imprimir_arbol(nodo, nivel=0):
        if nodo is not None:
            imprimir_arbol(nodo.derecha, nivel + 1)
            print("    " * nivel + str(nodo.valor))
            imprimir_arbol(nodo.izquierda, nivel + 1)

    imprimir_arbol(raiz)
    print("Expresión en postfijo:", ej8.post_order(raiz))
