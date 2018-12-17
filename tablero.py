import networkx as net
import pygame
from pygame.locals import *
from functools import partial
import os
import sys

nodos9 = list(range(1,25))
vertices9 = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),(9,10),(10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,9),(17,18),(18,19),(19,20),(20,21),(21,22),(22,23),(23,24),(24,17),(2,10),(10,18),(4,12),(12,20),(6,14),(14,22),(8,16),(16,24)]
molinos9 = [[1,2,3],[3,4,5],[5,6,7],[7,8,1],[9,10,11],[11,12,13],[13,14,15],[15,16,9],[17,18,19],[19,20,21],[21,22,23],[23,24,17],[2,10,18],[4,12,20],[6,14,22],[8,16,24]]

nodos3 = list(range(1,10))
vertices3 = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),(2,9),(4,9),(6,9),(8,9)]
molinos3 = [[1,2,3],[3,4,5],[5,6,7],[7,8,1],[2,9,6],[8,9,4]]

nodos56 = list(range(1,17))
vertices56 = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),(9,10),(10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,9),(2,10),(4,12),(6,14),(8,16)]
molinos56 = [[1,2,3],[3,4,5],[5,6,7],[7,8,1],[9,10,11],[11,12,13],[13,14,15],[15,16,9]]

nodos7 = list(range(1,18))
vertices7 = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),(9,10),(10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,9),(2,10),(4,12),(6,14),(8,16),(10,17),(12,17),(14,17),(16,17)]
molinos7 = [[1,2,3],[3,4,5],[5,6,7],[7,8,1],[9,10,11],[11,12,13],[13,14,15],[15,16,9],[2,10,17],[10,17,14],[17,14,6],[8,16,17],[16,17,12],[17,12,4]]

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
CAFE =	(184,134,11)

class Tablero(object):
    def __init__(self, numero):
        self.numero = numero
        self.grafo = net.Graph()
        self.aristas = list()
        
        if self.numero == 3:
            self.aristas = [(245,15), (505,15), (765,15),(765,275),(765,535),(505,535),(245,535),(245,275),(505,275)]
            self.grafo.add_nodes_from(nodos3,estado='V')
            self.grafo.add_edges_from(vertices3)
            self.molinos = molinos3
        elif self.numero == 5 or self.numero == 6:
            self.aristas = [(245,15), (505,15), (765,15),(765,275),(765,535),(505,535),(245,535),(245,275),(365,135),(505,135),(645,135),(645,275),(645,415),(505,415),(365,415),(365,275)]
            self.grafo.add_nodes_from(nodos56,estado='V')
            self.grafo.add_edges_from(vertices56)
            self.molinos = molinos56
        elif self.numero == 7:
            self.aristas= [(245,15), (505,15), (765,15),(765,275),(765,535),(505,535),(245,535),(245,275),(365,135),(505,135),(645,135),(645,275),(645,415),(505,415),(365,415),(365,275),(505,275)]
            self.grafo.add_nodes_from(nodos7,estado='V')
            self.grafo.add_edges_from(vertices7)
            self.molinos = molinos7
        elif self.numero == 9:
            self.aristas = [(245,15), (505,15), (765,15),(765,275),(765,535),(505,535),(245,535),(245,275),(325,95),(505,95),(685,95),(685,275),(685,455),(505,455),(325,455),(325,275),(405,175),(505,175),(605,175),(605,275),(605,375),(505,375),(405,375),(405,275)]
            self.grafo.add_nodes_from(nodos9,estado='V')
            self.grafo.add_edges_from(vertices9)
            self.molinos = molinos9


	##Función encargada de dibujar el tablero según la cantidad de fichas seleccionadas
    def dibujar_tablero(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.pantalla_tab=pygame.display.set_mode([1264,603])
        fondo = pygame.image.load("images/fondo3.jpeg").convert()       
        pygame.display.set_caption("Molino 9 - Tablero "+str(self.numero)+" piezas")
        self.pantalla_tab.blit(fondo, (0, 0))
        marcador = pygame.image.load("images/marcador.png")
        marcador = pygame.transform.scale(marcador, [300, 500])
        self.pantalla_tab.blit(marcador, (900,50))

        pygame.draw.rect(self.pantalla_tab, NEGRO, [270, 40, 520, 520], 3)
        if self.numero == 3:
            pygame.draw.line(self.pantalla_tab, NEGRO, [530, 40], [530, 560], 4)
            pygame.draw.line(self.pantalla_tab, NEGRO, [270, 300], [790, 300], 4)
        
        elif self.numero == 5 or self.numero==6 or self.numero==7:
            pygame.draw.rect(self.pantalla_tab, NEGRO, [390, 160, 280, 280], 3)
            pygame.draw.line(self.pantalla_tab, NEGRO, [530, 40], [530, 160], 4)
            pygame.draw.line(self.pantalla_tab, NEGRO, [270, 300], [390, 300], 3)
            pygame.draw.line(self.pantalla_tab, NEGRO, [790, 300], [670, 300], 3)
            pygame.draw.line(self.pantalla_tab, NEGRO, [530, 560], [530, 440], 4)
            
            if self.numero == 7:
                pygame.draw.line(self.pantalla_tab, NEGRO, [530, 40], [530, 560], 4)
                pygame.draw.line(self.pantalla_tab, NEGRO, [270, 300], [790, 300], 3)		
        
        elif self.numero == 9:
            pygame.draw.rect(self.pantalla_tab, NEGRO, [350, 120, 360, 360], 3)
            pygame.draw.rect(self.pantalla_tab, NEGRO, [430, 200, 200, 200], 3)
            pygame.draw.line(self.pantalla_tab, NEGRO, [530, 40], [530, 200], 4)
            pygame.draw.line(self.pantalla_tab, NEGRO, [270, 300], [430, 300], 3)
            pygame.draw.line(self.pantalla_tab, NEGRO, [530, 560], [530, 400], 4)
            pygame.draw.line(self.pantalla_tab, NEGRO, [790, 300], [630, 300], 3)

        for i in range(len(self.aristas)):
            pygame.draw.circle(self.pantalla_tab, NEGRO, (self.aristas[i][0]+25,self.aristas[i][1]+25),9)

        pygame.display.flip()
        
    def ver_estado(self,pos):
        return self.grafo.node[pos]['estado']

    def color_ficha(self,letra_color):
        if letra_color == 'R':
            color = pygame.image.load("images/ficha-roja.png")
        elif letra_color == 'A':
            color = pygame.image.load("images/ficha-azul.png")
        elif letra_color == 'SA':
            color = pygame.image.load("images/ficha-azulS.png")
        elif letra_color == 'SR':
            color = pygame.image.load("images/ficha-rojaS.png")
        return color

    def obtener_posicion(self,x,y):
        for idx, punto in enumerate(self.aristas):
            if(x >= punto[0] and y >=punto[1] and x <= punto[0]+50 and y <=punto[1]+50):
                return idx+1
        return -1

    def centro_posicion(self,pos):
        for idx, punto in enumerate(self.aristas):
            if pos == idx+1:
                return (punto[0],punto[1])
                
    def ver_molinos(self,pos):
        molinos = self.molinos
        molinos_nodo = []
        for m in molinos:
            for n in m:
                if pos== n:
                    molinos_nodo.append(m)
        return molinos_nodo

    def tam_tablero(self):
        return self.grafo.nodes.__len__()

    def adyacentes(self,pos):
        return [n for n in self.grafo[pos]]

