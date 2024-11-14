#Importamos el módulo queue que permite trabajar con colas de prioridad
from queue import PriorityQueue
from generadorGrafos import Grafo
from generadorModelos import *

def nodosDeArista(self, nodo):
    """
    Método que obtiene los nodos adyacentes a un nodo de interes
    Asignar un método de generación de grafo
    nodo -> nodo de interes
    """
    #Obtenemos las aristas generadas en el modelo
    aristaGrafo = self.aristas.values()
    #Generar una lista de nodos conectados por la arista
    n1 = []
    #Convertimos al nodo de busqueda en cadena
    nodo = str(nodo)
    #Obtenemos el segundo nodo unido a la arista
    for i in aristaGrafo:
        #Obtenemos los nodos (u, v)        
        n2 = i.split(' -> ', 1)
        if str(n2[0]) == nodo:       #Obtenemos el segundo nodo
            n1.append(n2[1])
        elif str(n2[1]) == nodo:     #Obtenemos el segundo nodo
            n1.append(n2[0])
    #Retornamos la lista de nodos adyacentes
    return n1

def getCostoArista(self, n1, n2=False):
    """
    Método que obtiene los costos de recorrer las aristas que
    se encuentran unidas al nodo
    """
    #Obtenemos las aristas generadas en el modelo
    aristaGrafo = self.aristas.values()
    for i in aristaGrafo:        
        pass

    

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
        #Para cada arista saliente de nodo
        for i in nodosDeArista(modelo, nodo):
            print("Nodos ady: ", i)
            #Si i no se encuentra en la lista S
            """
            if int(i) not in S:                
                print(f"{i} no se encuentra en {S}")
                """
            print(f"Costo de recorrer {i} {modelo.costos.get(i)}")
                



    print("Cola Vacia?", colaPrioridad.empty())
    print("Lista de nodos recorridos", S)

    return True

modelo = modeloMalla(4, 4)
print(modelo)
#x = Dijkstra(modelo, 4)
#print(x)
getCostoArista(modelo)

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