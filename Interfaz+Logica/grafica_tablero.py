import pygame
from pygame.locals import *
from functools import partial
from jugador import Jugador
from cuadrante import Cuadrante
import os
import sys

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
CAFE =	(184,134,11)

def insert_grilla(pantalla):
	for desplazar_y in range(0, 1300, 10):
		pygame.draw.line(pantalla,BLANCO, [0 + desplazar_y, 0], [0 + desplazar_y, 600], 1)
		pygame.draw.line(pantalla,BLANCO, [0, 0 + desplazar_y], [1300, 0 + desplazar_y], 1)


class Tablero(object):

	def __init__(self, numero, turno):
		#self.numero = numero de fichas por jugador
		#self.turno = 0
		#self.jugadas = total de jugadas entre jugador 1 y 2
		#self.jugador1 = Jugador(numero,'rojo')
		#self.jugador2 = Jugador(numero,'azul')
		#self.aristas = esquina superior izquierda del cuadrante donde se ubica el punto
		#self.arista_estados = estado de la arista enumerada (lista de aristas correspondientes)
		self.numero = numero
		self.turno = 0
		self.jugadas = 2*numero
		self.jugador1 = Jugador(numero,'rojo')
		self.jugador2 = Jugador(numero,'azul')
		self.aristas = list()
		self.arista_estados = list()

	##Función encargada de dibujar el tablero según la cantidad de fichas seleccionadas
	def dibujar_tablero(self, pantalla):
		pygame.draw.rect(pantalla, NEGRO, [270, 40, 520, 520], 3)	
		self.aristas = [(245,15), (505,15), (765,15),(765,275),(765,535),(505,535),(245,535),(245,275)]

		if self.numero == 3:
			pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 560], 4)
			pygame.draw.line(pantalla, NEGRO, [270, 300], [790, 300], 4)
			self.aristas.append((505,275))

		elif self.numero == 5 or self.numero==6 or self.numero==7:
			pygame.draw.rect(pantalla, NEGRO, [390, 160, 280, 280], 3)
			pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 160], 4)
			pygame.draw.line(pantalla, NEGRO, [270, 300], [390, 300], 3)
			pygame.draw.line(pantalla, NEGRO, [790, 300], [670, 300], 3)
			pygame.draw.line(pantalla, NEGRO, [530, 560], [530, 440], 4)
			self.aristas = [(245,15), (505,15), (765,15),(765,275),(765,535),(505,535),(245,535),(245,275),(365,135),(505,135),(645,135),(645,275),(645,415),(505,415),(365,415),(365,275)]
				
			if self.numero == 7:
				pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 560], 4)
				pygame.draw.line(pantalla, NEGRO, [270, 300], [790, 300], 3)
				self.aristas.append((505,275))##17

		elif self.numero == 9:
			pygame.draw.rect(pantalla, NEGRO, [350, 120, 360, 360], 3)
			pygame.draw.rect(pantalla, NEGRO, [430, 200, 200, 200], 3)
			pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 200], 4)
			pygame.draw.line(pantalla, NEGRO, [270, 300], [430, 300], 3)
			pygame.draw.line(pantalla, NEGRO, [530, 560], [530, 400], 4)
			pygame.draw.line(pantalla, NEGRO, [790, 300], [630, 300], 3)
			self.aristas = [(245,15), (505,15), (765,15),(765,275),(765,535),(505,535),(245,535),(245,275),(325,95),(505,95),(685,95),(685,275),(685,455),(505,455),(325,455),(325,275),(405,175),(505,175),(605,175),(605,275),(605,375),(505,375),(405,375),(405,275)]

		for i in range(len(self.aristas)):
			pygame.draw.rect(pantalla, CAFE, [self.aristas[i][0], self.aristas[i][1], 50, 50], 2)
			#pygame.draw.line(pantalla, VIOLETA, [self.aristas[i][0], self.aristas[i][1]], [1000, 1000], 3)
			pygame.draw.circle(pantalla, NEGRO, (self.aristas[i][0]+25,self.aristas[i][1]+25),9)
			print(i+1, self.aristas[i][0], self.aristas[i][1])
			self.arista_estados.append(Cuadrante(i+1))

		for i in range(len(self.arista_estados)):
			print(self.arista_estados[i].posicion, self.arista_estados[i].status)

	##Función que permite posicionar fichas SÓLO en las posiciones correspondientes a las aristas
	def posicion_admitida(self, x, y, area_posible):
		print("punto a adjuntar", x, y)
		for idx, punto_inicial in enumerate(area_posible):
			if(x >= punto_inicial[0] and y >=punto_inicial[1] and x <= punto_inicial[0]+50 and y <=punto_inicial[1]+50):
				print("posicion ", idx+1)
				return True
		return False
	
	#Función encargada de encontrar la arista (enumeradas) más cercana a la zona clickeada.
	def arista_posicion(self, x, y, area_posible):
		for idx, punto_inicial in enumerate(area_posible):
			if(x >= punto_inicial[0] and y >=punto_inicial[1] and x <= punto_inicial[0]+50 and y <=punto_inicial[1]+50):
				return idx
		return -1

	##Función encargada de encontrar el centro de la arista más cercana  a la posición clickeada.
	def posicionar(self, x, y, area_posible):
		for punto_inicial in area_posible:
			if(x >= punto_inicial[0] and y >=punto_inicial[1] and x <= punto_inicial[0]+50 and y <=punto_inicial[1]+50):
				centro_arista = (punto_inicial[0], punto_inicial[1])
				return centro_arista
		return -1


	##Función encargada de colocar la ficha en la posición clickeada correspondiente.	
	def posicionar_ficha(self, pantalla):
		jug1 = pygame.transform.scale(self.jugador1.ficha_color, [50, 50])
		jug2 = pygame.transform.scale(self.jugador2.ficha_color, [50, 50])
		if self.jugadas > 0:
			if self.turno == 0 or self.turno == 2:
				x,y = pygame.mouse.get_pos()
				pos = (x-25,y-25)
				if self.posicion_admitida(x,y, self.aristas):
					posicion_cuadrante = self.arista_posicion(x,y, self.aristas)
					if self.arista_estados[posicion_cuadrante].status == False:
						pantalla.blit(jug1, self.posicionar(x,y,self.aristas))
						self.jugador1.posiciones.append(pos)
						self.turno=1
						self.arista_estados[posicion_cuadrante].status = True
						self.jugadas = self.jugadas-1
					else:
						print("Posición ocupada, intente otra posición")
			elif self.turno == 1:
				x,y = pygame.mouse.get_pos()
				pos = (x-25,y-25)
				if self.posicion_admitida(x,y, self.aristas):
					posicion_cuadrante = self.arista_posicion(x,y, self.aristas)
					if self.arista_estados[posicion_cuadrante].status == False:
						pantalla.blit(jug2, self.posicionar(x,y,self.aristas))
						self.jugador2.posiciones.append(pos)
						self.turno=2
						self.arista_estados[posicion_cuadrante].status = True
						self.jugadas = self.jugadas-1
					else:
						print("Posición ocupada, intente otra posición")
		pygame.display.update()