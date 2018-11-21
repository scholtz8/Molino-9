import pygame
from pygame.locals import *

class Posicion(object):

	def __init__(self,posicion):
		self.posicion = posicion
		self.status = False

	def arista_posicion(self, x, y,numero_aristas):
		for idx, punto_inicial in enumerate(area_posible):
			if(x >= punto_inicial[0] and y >=punto_inicial[1] and x <= punto_inicial[0]+50 and y <=punto_inicial[1]+50):
				return idx
		return -1

	def posicionar(self, x, y, numero_aristas)
		for idx, punto_inicial in enumerate(area_posible):
			if(x >= punto_inicial[0] and y >=punto_inicial[1] and x <= punto_inicial[0]+50 and y <=punto_inicial[1]+50):
				centro_arista = (punto_inicial[0]+25, punto_inicial[1]+25)
				return centro_arista
		return -1

