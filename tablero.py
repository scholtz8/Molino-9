import networkx as net

class Tablero(object):

    # representacion del tablero por un grafo, donde los nodos con los puntos donde se pueden poner las fichas y 
    # los vertices las lineas del tablero que los conectan
    def __init__(self):
        self.grafo = net.Graph()
        self.grafo.add_nodes_from(list(range(1,25)),estado='V')
        self.grafo.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),(9,10),(10,11),
        (11,12),(12,13),(13,14),(14,15),(15,16),(16,9),(17,18),(18,19),(19,20),(20,21),(21,22),
        (22,23),(23,24),(24,17),(2,10),(10,18),(4,12),(12,20),(6,14),(14,22),(8,16),(16,24)])

    # obtener nodos adyacentes a un nodo
    def adyacentes(self,nodo):
        return [n for n in self.grafo[nodo]]

    # ver si el nodo esta vacio(V) o ocupado por una ficha blanca(B) o negra(N)
    def ver_estado(self,nodo):
        return self.grafo.node[nodo]['estado']

    # obtener nodos adyacentes vacios a un nodo
    def adyacentes_vacios(self,nodo):
        ady = self.adyacentes(nodo)
        for a in ady:
            if self.ver_estado(a) != 'V':
                ady.remove(a)
        return ady

    # cambiar el estado del noda al poner o mover una ficha del o hacia el nodo
    def cambiar_estado(self,nodo,estado):
        self.grafo.node[nodo]['estado'] = estado

    # print del tablero
    def ver_tablero(self):
        print(self.ver_estado(1)+"01"+"-"*17+self.ver_estado(2)+"02"+"-"*17+self.ver_estado(3)+"03")
        print(" |"+" "*19+"|"+" "*19+"|")
        print(" |     "+self.ver_estado(9)+"09"+"-"*10+self.ver_estado(10)+"10"+"-"*10+self.ver_estado(11)+"11"+"     |")
        print(" |"+" "*6+"|"+" "*12+"|"+" "*12+"|"+" "*6+"|")
        print(" |      |    "+self.ver_estado(17)+"17----"+self.ver_estado(18)+"18----"+self.ver_estado(19)+"19    |      |")
        print(" |"+" "*6+"|"+" "*5+"|"+" "*13+"|"+" "*5+"|"+" "*6+"|")
        print(self.ver_estado(8)+"08"+"-"*4+self.ver_estado(16)+"16"+"-"*3+self.ver_estado(24)+"24"+" "*11+self.ver_estado(20)+"20"+"-"*3+self.ver_estado(12)+"12"+"-"*4+self.ver_estado(4)+"04")
        print(" |"+" "*6+"|"+" "*5+"|"+" "*13+"|"+" "*5+"|"+" "*6+"|")
        print(" |      |    "+self.ver_estado(23)+"23----"+self.ver_estado(22)+"22----"+self.ver_estado(21)+"21    |      |")
        print(" |"+" "*6+"|"+" "*12+"|"+" "*12+"|"+" "*6+"|")
        print(" |     "+self.ver_estado(15)+"15"+"-"*10+self.ver_estado(14)+"14"+"-"*10+self.ver_estado(13)+"13"+"     |")
        print(" |"+" "*19+"|"+" "*19+"|")
        print(self.ver_estado(7)+"07"+"-"*17+self.ver_estado(6)+"06"+"-"*17+self.ver_estado(5)+"05")