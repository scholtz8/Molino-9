import pygame
from pygame.locals import *
class Jugador(object):

    def __init__(self,num_piezas,color):
        # color del jugador
        self.color = color
        # numero de piezas no jugadas
        self.piezas = num_piezas
        # numero de piezas perdidas
        self.perdidas = 0
        self.posiciones = list()
        if color == 'rojo':
            self.ficha_color = pygame.image.load("images/ficha-roja.png")
        elif color == 'azul':
            self.ficha_color = pygame.image.load("images/ficha-azul.png")
        elif color == 'verde':
            self.ficha_color = pygame.image.load("images/ficha-verde.png")
        elif color == 'amarilla':
            self.ficha_color = pygame.image.load("images/ficha-amarilla.png")
        else:
            self.ficha_color = pygame.image.load("images/ficha-blanca.png")

    def no_jugadas(self):
        return self.piezas

    def ver_perdidas(self):
        return self.perdidas

    def ver_color(self):
        return self.color

    def restar_piezas(self):
        self.piezas -= 1

    def sumar_perdidas(self):
        self.perdidas += 1
