from generadorModelos import *
from Dijkstra import *

#Numero de muestras que se graficaran por modelo
numNodos = [30, 500]
#Matriz para el modelo malla
matriz = {30:[6, 5], 500: [25, 20]}

"""
Modelo Malla
"""
#Nodo Fuente para crear el arbol
nodoFuente = 15
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
"""
#Nodo Fuente para crear el arbol
nodoFuente = 0
for i in numNodos:
    #Generamos el modelo para 30 y 500 nodos
    modelo = modeloErdosRenyi(i, i-1)
    nombreArchivo = "Erdos-Renyi " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    arbol = Dijkstra(modelo, nodoFuente)
    nombreArchivo = "Dijkstra ErdosRenyi " + str(i) + " nodos"
    #Generamos el archivo .gv
    arbol.graphViz(nombreArchivo)

"""
Modelo Gilbert
"""
#Nodo Fuente para crear el arbol
nodoFuente = 10
p = 0.01
#Damos una probabilidad de 0.1 para la conexión de nodos
for i in numNodos:
    #Generamos el modelo para 30 y 500 nodos
    modelo = modeloGilbert(p, i)
    nombreArchivo = "Gilbert "  + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    #Genera Dijkstra
    arbol = Dijkstra(modelo, nodoFuente)
    nombreArchivo = " Dijkstra Arbol Gilbert " + str(i) + " nodos"
    #Generamos el archivo .gv
    arbol.graphViz(nombreArchivo)

"""
Modelo Geografico Simple
"""
#Nodo Fuente para crear el arbol
nodoFuente = 10
r = 0.1 #Distancia máxima entre nodos
for i in numNodos:
    #Generamos el modelo para 30 y 500 nodos
    modelo = modeloGeograficoSimple(i, r)
    nombreArchivo = "GeograficoSimple " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    #Genera Dijkstra
    arbol = Dijkstra(modelo, nodoFuente)
    nombreArchivo = "Dijkstra Geografico " + str(i) + " nodos"
    #Generamos el archivo .gv
    arbol.graphViz(nombreArchivo)

"""
Modelo Barabasi-Albert
"""
#Nodo Fuente para crear el arbol
nodoFuente = 10
d = 8 #Número máximo de conexiones por vertice
for i in numNodos:
    #Generamos el modelo para 30 y 500 nodos
    modelo = modeloBarabasiAlbert(i, d)
    nombreArchivo = "Barabasi-Albert " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    #Genera Dijkstra
    arbol = Dijkstra(modelo, nodoFuente)
    nombreArchivo = "Dijkstra Barabasi " + str(i) + " nodos"
    #Generamos el archivo .gv
    arbol.graphViz(nombreArchivo)

"""
Módelo Dorogovtsev Mendes
"""
#Nodo Fuente para crear el arbol
nodoFuente = 10
for i in numNodos:
    #Generamos el modelo para 30 y 500 nodos
    modelo = modeloDorogovtsevMendes(i)
    nombreArchivo = "Dorogovtsev-Mendes " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    #Genera Dijkstra
    arbol = Dijkstra(modelo, nodoFuente)
    nombreArchivo = "Dijkstra Dorogovtsev " + str(i) + " nodos"
    #Generamos el archivo .gv
    arbol.graphViz(nombreArchivo)
