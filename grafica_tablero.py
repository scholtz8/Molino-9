import pygame
from pygame.locals import *
from tkinter import *
from functools import partial
from jugador import Jugador
from partida import Partida
import os
import sys

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

def insert_grilla(pantalla):
	for desplazar_y in range(0, 1300, 10):
		pygame.draw.line(pantalla,BLANCO, [0 + desplazar_y, 0], [0 + desplazar_y, 600], 1)
		pygame.draw.line(pantalla,BLANCO, [0, 0 + desplazar_y], [1300, 0 + desplazar_y], 1)


class Tablero(object):

	def __init__(self, numero, turno):
		self.numero = numero
		self.turno = 0
		self.jugadas = 2*numero
		self.jugador1 = Jugador(numero,'rojo')
		self.jugador2 = Jugador(numero,'azul')
		self.aristas = list()
		pygame.init()
		screen=pygame.display.set_mode([1064,603])
		fondo = pygame.image.load("images/fondo3.jpeg").convert()		
		pygame.display.set_caption("Molino 9")
		screen.blit(fondo, (0, 0))
		#insert_grilla(screen)
		self.dibujar_tablero(screen)
		pygame.display.flip()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				if pygame.mouse.get_pressed()[0]:
					self.posicionar_ficha(screen)

	def dibujar_tablero(self, pantalla):
		pygame.draw.rect(pantalla, NEGRO, [270, 40, 520, 520], 3)	

		pygame.draw.circle(pantalla, NEGRO, (270,40),9)##1
		pygame.draw.circle(pantalla, NEGRO, (530,40),9)##2
		pygame.draw.circle(pantalla, NEGRO, (790,40),9)##3
		pygame.draw.circle(pantalla, NEGRO, (790,300),9)##4
		pygame.draw.circle(pantalla, NEGRO, (790,560),9)##5
		pygame.draw.circle(pantalla, NEGRO, (530,560),9)##6
		pygame.draw.circle(pantalla, NEGRO, (270,560),9)##7
		pygame.draw.circle(pantalla, NEGRO, (270,300),9)##8

		self.aristas = [(245,15), (505,15), (765,15),(765,275),(765,535),(505,535),(245,535),(245,275)]

		if self.numero == 3:
			pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 560], 4)
			pygame.draw.line(pantalla, NEGRO, [270, 300], [790, 300], 4)
			
			pygame.draw.circle(pantalla, NEGRO, (530,300),9)
			self.aristas.append((505,275))

		elif self.numero == 5 or self.numero==6 or self.numero==7:
			pygame.draw.rect(pantalla, NEGRO, [390, 160, 280, 280], 3)

			pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 160], 4)
			pygame.draw.line(pantalla, NEGRO, [270, 300], [390, 300], 3)
			pygame.draw.line(pantalla, NEGRO, [790, 300], [670, 300], 3)
			pygame.draw.line(pantalla, NEGRO, [530, 560], [530, 440], 4)

			pygame.draw.circle(pantalla, NEGRO, (390,160),9)##9
			pygame.draw.circle(pantalla, NEGRO, (530,160),9)##10
			pygame.draw.circle(pantalla, NEGRO, (670,160),9)##11
			pygame.draw.circle(pantalla, NEGRO, (670,300),9)##12
			pygame.draw.circle(pantalla, NEGRO, (670,440),9)##13
			pygame.draw.circle(pantalla, NEGRO, (530,440),9)##14
			pygame.draw.circle(pantalla, NEGRO, (390,440),9)##15
			pygame.draw.circle(pantalla, NEGRO, (390,300),9)##16
			
			self.aristas = [(245,15), (505,15), (765,15),(765,275),(765,535),(505,535),(245,535),(245,275),(365,135),(505,135),(645,135),(645,275),(645,415),(505,415),(365,415),(365,275)]
				
			if self.numero == 7:
				pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 560], 4)
				pygame.draw.line(pantalla, NEGRO, [270, 300], [790, 300], 3)
				pygame.draw.circle(pantalla, NEGRO, (530,300),9)
				self.aristas.append((505,275))##17

		elif self.numero == 9:
			pygame.draw.rect(pantalla, NEGRO, [350, 120, 360, 360], 3)
			pygame.draw.rect(pantalla, NEGRO, [430, 200, 200, 200], 3)

			pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 200], 4)
			pygame.draw.line(pantalla, NEGRO, [270, 300], [430, 300], 3)
			pygame.draw.line(pantalla, NEGRO, [530, 560], [530, 400], 4)
			pygame.draw.line(pantalla, NEGRO, [790, 300], [630, 300], 3)

			pygame.draw.circle(pantalla, NEGRO, (350,120),9)##9
			pygame.draw.circle(pantalla, NEGRO, (530,120),9)##10
			pygame.draw.circle(pantalla, NEGRO, (710,120),9)##11
			pygame.draw.circle(pantalla, NEGRO, (710,300),9)##12
			pygame.draw.circle(pantalla, NEGRO, (710,480),9)##13
			pygame.draw.circle(pantalla, NEGRO, (530,480),9)##14
			pygame.draw.circle(pantalla, NEGRO, (350,480),9)##15
			pygame.draw.circle(pantalla, NEGRO, (350,300),9)##16
			pygame.draw.circle(pantalla, NEGRO, (430,200),9)##17
			pygame.draw.circle(pantalla, NEGRO, (530,200),9)##18
			pygame.draw.circle(pantalla, NEGRO, (630,200),9)##19
			pygame.draw.circle(pantalla, NEGRO, (630,300),9)##20
			pygame.draw.circle(pantalla, NEGRO, (630,400),9)##21
			pygame.draw.circle(pantalla, NEGRO, (530,400),9)##22
			pygame.draw.circle(pantalla, NEGRO, (430,400),9)##23
			pygame.draw.circle(pantalla, NEGRO, (430,300),9)##24
			
			self.aristas = [(245,15), (505,15), (765,15),(765,275),(765,535),(505,535),(245,535),(245,275),(325,95),(505,95),(685,95),(685,275),(685,455),(505,455),(325,455),(325,275),(405,175),(505,175),(605,175),(605,275),(605,375),(505,375),(405,375),(405,275)]

		for i in range(len(self.aristas)):
			pygame.draw.rect(pantalla, VERDE, [self.aristas[i][0], self.aristas[i][1], 50, 50], 3)
			pygame.draw.line(pantalla, VIOLETA, [self.aristas[i][0], self.aristas[i][1]], [1000, 1000], 3)
			print(i+1, self.aristas[i][0], self.aristas[i][1])
		
	def posicionar_ficha(self, pantalla):
		jug1 = pygame.transform.scale(self.jugador1.ficha_color, [50, 50])
		jug2 = pygame.transform.scale(self.jugador2.ficha_color, [50, 50])
		if self.jugadas > 0:
			print(self.aristas)
			if self.turno == 0 or self.turno == 2:
				x,y = pygame.mouse.get_pos()
				pos = (x-25,y-25)
				if f.movimiento_posible(x,y, self.aristas):
					pantalla.blit(jug1,pos)
					self.jugador1.posiciones.append(pos)
					self.turno=1
			elif self.turno == 1:
				x,y = pygame.mouse.get_pos()
				pos = (x-25,y-25)
				if f.movimiento_posible(x,y, self.aristas):
					pantalla.blit(jug2,pos)
					self.jugador2.posiciones.append(pos)
					self.turno=2
			self.jugadas = self.jugadas-1
		pygame.display.update()