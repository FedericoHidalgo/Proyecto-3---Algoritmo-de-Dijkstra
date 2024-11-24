from generadorModelos import *
from Dijkstra import *

#Numero de muestras que se graficaran por modelo
numNodos = [9]
#Matriz para el modelo malla
matriz = {9:[3, 3], 500: [25, 20]}
#Nodo Fuente para crear el arbol
nodoFuente = 0

"""
Modelo Malla
"""
#i -> 30 y 500 nodos
for i in numNodos:   
    #Genera el modelo de grafo  
    modelo = modeloMalla(matriz[i][0], matriz[i][1])
    nombreArchivo = "Malla " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    arbol = Dijkstra(modelo, nodoFuente)
    nombreArchivo = "Dijkstra malla " + str(i) + " nodos"
    arbol.graphViz(nombreArchivo)

"""
Modelo Erdos Renyi

for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloErdosRenyi(i, i-1)
    nombreArchivo = "Erdos-Renyi " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    k = 0       #Var auxiliar para nombrar los archivos
    for j in algoritmo:
        #Genera el arbol de Erdos Renyi
        #j -> BFS, DFS recursiva y DFS iterativa
        arbol = j(modelo, nodoFuente)
        nombreArchivo = "Arbol ErdosRenyi " + algNombre[k] + str(i) + " nodos"
        #Generamos el archivo .gv
        arbol.graphViz(nombreArchivo)
        #Var auxiliar para nombrar los archivos
        k += 1


Modelo Gilbert

p = 0.1
#Damos una probabilidad de 0.1 para la conexión de nodos
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloGilbert(p, i)
    nombreArchivo = "Gilbert "  + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    k = 0       #Var auxiliar para nombrar los archivos
    for j in algoritmo:
        #Genera el arbol de malla
        #j -> BFS, DFS recursiva y DFS iterativa
        arbol = j(modelo, nodoFuente)
        nombreArchivo = "Arbol Gilbert " + algNombre[k] + str(i) + " nodos"
        #Generamos el archivo .gv
        arbol.graphViz(nombreArchivo)
        #Var auxiliar para nombrar los archivos
        k += 1


Modelo Geografico Simple

r = 0.25 #Distancia máxima entre nodos
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloGeograficoSimple(i, r)
    nombreArchivo = "GeograficoSimple " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    k = 0       #Var auxiliar para nombrar los archivos
    for j in algoritmo:
        #Genera el arbol de malla
        #j -> BFS, DFS recursiva y DFS iterativa
        arbol = j(modelo, nodoFuente)
        nombreArchivo = "Arbol Geografico " + algNombre[k] + str(i) + " nodos"
        #Generamos el archivo .gv
        arbol.graphViz(nombreArchivo)
        #Var auxiliar para nombrar los archivos
        k += 1


Modelo Barabasi-Albert

d = 8 #Número máximo de conexiones por vertice
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloBarabasiAlbert(i, d)
    nombreArchivo = "Barabasi-Albert " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    k = 0       #Var auxiliar para nombrar los archivos
    for j in algoritmo:
        #Genera el arbol de malla
        #j -> BFS, DFS recursiva y DFS iterativa
        arbol = j(modelo, nodoFuente)
        nombreArchivo = "Arbol Barabasi " + algNombre[k] + str(i) + " nodos"
        #Generamos el archivo .gv
        arbol.graphViz(nombreArchivo)
        #Var auxiliar para nombrar los archivos
        k += 1


Módelo Dorogovtsev Mendes

for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloDorogovtsevMendes(i)
    nombreArchivo = "Dorogovtsev-Mendes " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    k = 0       #Var auxiliar para nombrar los archivos
    for j in algoritmo:
        #Genera el arbol de malla
        #j -> BFS, DFS recursiva y DFS iterativa
        arbol = j(modelo, nodoFuente)
        nombreArchivo = "Arbol Dorogovtsev " + algNombre[k] + str(i) + " nodos"
        #Generamos el archivo .gv
        arbol.graphViz(nombreArchivo)
        #Var auxiliar para nombrar los archivos
        k += 1
"""