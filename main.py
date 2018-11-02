import networkx as net

print('Molino 9')

class Tablero(object):

    def __init__(self):
        self.grafo = net.Graph()
        self.grafo.add_nodes_from(list(range(1,25)),estado='nada')
        self.grafo.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),(9,10),(10,11),
        (11,12),(12,13),(13,14),(14,15),(15,16),(16,9),(17,18),(18,19),(19,20),(20,21),(21,22),
        (22,23),(23,24),(24,17),(2,10),(10,18),(4,12),(12,20),(6,14),(14,22),(8,16),(16,24)])

    def adyacentes(self,nodo):
        return [n for n in self.grafo[nodo]]

    def ver_estado(self,nodo):
        return self.grafo.node[nodo]['estado']

    def cambiar_estado(self,nodo,estado):
        self.grafo.node[nodo]['estado'] = estado

t = Tablero()
print(t.ver_estado(12))
t.cambiar_estado(12,'blanco')
print(t.ver_estado(12))
print(t.ver_estado(13))
