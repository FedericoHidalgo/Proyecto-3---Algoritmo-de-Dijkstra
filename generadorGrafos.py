from generadorNodos import Nodo
from generadorAristas import Arista
import random

class Grafo:
    """
    Clase generadora de Grafos
    """
    def __init__(self, dirigido = False):
        """
        Constructor                                                   
        """
        self.nodos = {}         #Conjunto, para evitar duplicados
        self.aristas = {}
        self.costos = {}
        self.dirigido = dirigido    #Grafo no dirigido como valor de inicio
        self.attr = {}

    def agregarNodo(self, id):
        """
        Agrega un nuevo nodo al grafo
        """
        nodo = self.nodos.get(id)   #Verifica si el nodo existe
        #Si no existe se crea uno nuevo        
        if nodo == None:
            nodo = Nodo(id)
            self.nodos[id] = str(nodo)  #Agrega un nodo  
        return nodo
    
    def agregarArista(self, n1, n2, id, le = None):
        """
        Agrega una arista al grafo
        """
        arista = Arista(n1, n2, id)
        arista = self.aristas.get(str(arista))   #Verifica si la arista existe
        #Si no existe se crea uno nuevo        
        if arista == None:
            V0 = self.agregarNodo(n1)   #Agrega nodo base
            V1 = self.agregarNodo(n2)   #Agrega nodo adyacente 
            arista = str(Arista(V0, V1, id))        
            self.aristas[arista] = arista   #Agrega arista
            #Agrega el costo de recorrer una arista
            if le == None:
                self.costos[arista] = random.randint(0, 100)  #Si no hay un valor definido de arista
            else:
                self.costos[arista] = le    #Si ya existe un valor definido para esa arista
        return arista
       
    def __str__(self):
        """
        Convertir grafo en string
        """
        graf = "Nodos: "
        for i in self.nodos:
            graf += str(i) + ','

        graf += "\nAristas: "
        for i in self.aristas:
            graf += str(i) + ','
        return str(graf)
    
    def crearCadena(self, id):
        """
        Crea la cadena de aristas y nodos que es
        reconocida por Gephi
        """
        cadena = ''
        #Formato DOT
        cadena += 'digraph ' + id + '{\n'
        #Imprimir los nodos
        for nodo in self.nodos:
            if self.attr.get(nodo) == str(0):
                cadena += str(nodo) + '[label="N' + str(nodo) + ' (' + str(self.attr.get(nodo)) + '), ", color="red"];\n'
            else:
                cadena += str(nodo) + '[label="N' + str(nodo) + ' (' + str(self.attr.get(nodo)) + ')"];\n'
        #Imprimir las aristas
        for arista in self.aristas:
            cadena += str(arista) + '[label="' + str(self.costos.get(arista)) + '"];\n'
        #Final del formato
        cadena += '}\n'
        return cadena
    
    def crearArchivo(self, id, cadena):
        """
        Genera el archivo .gv y lo exporta
        """
        nombreArchivo = id + '.gv'
        #Escribimos el archivo de salida
        archivo = open(nombreArchivo, 'w+')
        archivo.write(cadena)
        archivo.close()
        return nombreArchivo     

    def graphViz(self, id):
        """
        Genera un archivo con formato GraphViz
        """
        cadena = self.crearCadena(id)
        archivo = self.crearArchivo(id, cadena)
        print('Archivo GraphViz generado: ' + archivo + '\n')        
        
    def getDiccionarios(self):
        """
        Visualizar en consola el diccionario creado
        """
        print("Nodos: ")
        print(self.nodos.items())
        print("Aristas: ")
        print(self.aristas.items())

    def setAtributo(self, id, distNB='inf'):
        """
        Asigna al nodo el costo de llegar desde el nodo base
        """
        self.attr[id] = str(distNB)     #Distancia del Nodo Base al nodo actual
        return True


