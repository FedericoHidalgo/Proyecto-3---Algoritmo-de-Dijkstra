#Importamos el módulo queue que permite trabajar con colas de prioridad
from queue import PriorityQueue
from generadorGrafos import Grafo
from generadorModelos import *

def Dijkstra(modelo, s):
    """
    Algoritmo de Dijkstra. Dado un nodo fuente (s), 
    calcula el árbol de caminos más cortos.
    """ 
    #Cola de prioridades
    colaPrioridad = PriorityQueue()
    #Conjunto de nodos explorados
    S = []
    #Nodo fuente
    nodoFuente = modelo.nodos.get(s)
    #Si el nodo fuente no existe, termina el proceso
    if nodoFuente == None:
        print("El nodo Fuente no pertenece al modelo")
        return False
    contadorNodos = 0
    #Agregamos a la cola de prioridades los nodos con prioridad de infinito
    while modelo.nodos.get(contadorNodos) != None:
        if contadorNodos != int(nodoFuente):
            colaPrioridad.put((float('inf'), contadorNodos))
        else:
            #Asignar en cola de Prioridades el nodo fuente con valor 0
            colaPrioridad.put((0, int(nodoFuente)))        
        contadorNodos += 1
    #Mientras la cola de Prioridades no este vacia
    while not colaPrioridad.empty():
        #Obtenemos el primer elemento de la cola
        prioridad, nodo = colaPrioridad.get()
        print(f"Prioridad: {prioridad}, Nodo: {nodo}")
        #Agregamos el nodo a la lista S
        S.append(nodo)
    print("Cola Vacia?", colaPrioridad.empty())
    print("Lista de nodos recorridos", S)

    return True

modelo = modeloMalla(4, 4)
x = Dijkstra(modelo, 4)
print(x)

"""
#Ejemplo colas de prioridad
colaPrioridad = PriorityQueue()
colaPrioridad.put((3, "Sin importancia"))
colaPrioridad.put((1, "Urgente"))
colaPrioridad.put((2, "Importante"))

while not colaPrioridad.empty():
    prioridad, tarea = colaPrioridad.get()
    print(f"Prioridad: {prioridad}, Tarea: {tarea}")
"""