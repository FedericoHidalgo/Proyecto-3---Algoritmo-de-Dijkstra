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
    #Generar una lista de los pesos de recorrer cada camino
    camino = []
    #Convertimos al nodo de busqueda en cadena
    nodo = str(nodo)
    #Obtenemos el segundo nodo unido a la arista
    for i in aristaGrafo:
        #Obtenemos los nodos (u, v)        
        n2 = i.split(' -> ', 1)
        if str(n2[0]) == nodo:       #Obtenemos el segundo nodo
            n1.append(int(n2[1]))
            #Agregamos nuestra lista de caminos
            camino.append(self.costos.get(i))
        elif str(int(n2[1])) == nodo:     #Obtenemos el segundo nodo
            n1.append(n2[0])
            #Agregamos nuestra lista de caminos
            camino.append(self.costos.get(i))
    #Retornamos la lista de nodos adyacentes y distancia de cada camino
    return n1, camino

def Dijkstra(modelo, s, dirigido = False):
    """
    Algoritmo de Dijkstra. Dado un nodo fuente (s), 
    calcula el árbol de caminos más cortos.
    """ 
    G = Grafo(dirigido)
    #Cola de prioridades
    colaPrioridad = PriorityQueue()
    #Conjunto de nodos explorados
    S = []
    #Diccionario auxiliar para almacenar los valores de la cola
    c = {}
    #Nodo fuente
    nodoFuente = modelo.nodos.get(s)
    #Costo de recorrer cada arista
    costo = modelo.costos.copy()
    #Si el nodo fuente no existe, termina el proceso
    if nodoFuente == None:
        print("El nodo Fuente no pertenece al modelo")
        return False
    nodoFuente = int(nodoFuente)    
    contadorNodos = 0
    #Agregamos a la cola de prioridades los nodos con prioridad de infinito
    while modelo.nodos.get(contadorNodos) != None:
        if contadorNodos != nodoFuente:
            c[contadorNodos] = float('inf')
        else:
            #Asignar en cola de Prioridades el nodo fuente con valor 0
            colaPrioridad.put((0, nodoFuente))
            c[nodoFuente] = 0 
        contadorNodos += 1
    #Mientras la cola de Prioridades no este vacia
    while not colaPrioridad.empty():
        #Obtenemos el primer elemento de la cola    
        prioridad, nodo = colaPrioridad.get()
        if nodo not in S:
            nodo = int(nodo)
            print(f"\nNodo evaluado: {nodo}")
            #Agregamos el nodo a la lista S
            S.append(nodo)
            print(f"Se actualiza S: {S}")
            #Agregamos el nodo al archivo .gv
            G.setAtributo(nodo, prioridad)
            print(f"Se actualizan atributos del nodo: {nodo}, {prioridad}")
            #Para cada arista saliente de nodo
            n1, camino = nodosDeArista(modelo, nodo)       
            for i in range(len(n1)): 
                v = int(n1[i])  #Nodo v 
                le = camino[i]  #Costo de recorrer desde nodo a v  
                print(f"N1: {nodo}, N2: {v}, C: {le}")                  
                #Si v no se encuentra en la lista S
                if v not in S:   
                    print(f"{v} no esta en S")          
                    #Agregamos una arista al archivo .gv
                    G.agregarArista(nodo, v, ' -- ', le)  
                    #Si d(v) > d(u) + l
                    caminoPrevio = c.get(nodo) + le
                    print(f"Valor de recorrer ese nodo: {caminoPrevio}")
                    if c.get(v) > caminoPrevio:
                        print("d(v) > d(u) + l")   
                        print(f"d(v) = d(u) + l: {round(c.get(nodo) + le, 4)}")
                        #d(v) = d(u) + l
                        c[v] = round(c.get(nodo) + le, 4)
                        print(f"Nva prioridad c[v]: {c.get(v)}")
                        #Actualizar en cola de prioridad d(v)
                        colaPrioridad.put((c.get(v), v))                                         
    return G