import pygame
from pygame.locals import *
from tkinter import *
from functools import partial
from jugador import Jugador
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
		pygame.init()
		screen=pygame.display.set_mode([1064,603])
		fondo = pygame.image.load("images/fondo3.jpeg").convert()		
		pygame.display.set_caption("Molino 9")
		screen.blit(fondo, (0, 0))
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
		
		pygame.draw.circle(pantalla, NEGRO, (270,40),9)
		pygame.draw.circle(pantalla, NEGRO, (270,560),9)
		pygame.draw.circle(pantalla, NEGRO, (790,40),9)
		pygame.draw.circle(pantalla, NEGRO, (790,560),9)

		pygame.draw.circle(pantalla, NEGRO, (530,40),9)
		pygame.draw.circle(pantalla, NEGRO, (530,560),9)
		pygame.draw.circle(pantalla, NEGRO, (270,300),9)
		pygame.draw.circle(pantalla, NEGRO, (790,300),9)
		if self.numero == 3:
			pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 560], 4)
			pygame.draw.line(pantalla, NEGRO, [270, 300], [790, 300], 4)
			pygame.draw.circle(pantalla, NEGRO, (530,300),9)

		elif self.numero == 5 or self.numero==6 or self.numero==7:
			pygame.draw.rect(pantalla, NEGRO, [390, 160, 280, 280], 3)

			pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 160], 4)
			pygame.draw.line(pantalla, NEGRO, [270, 300], [390, 300], 3)
			pygame.draw.line(pantalla, NEGRO, [790, 300], [670, 300], 3)
			pygame.draw.line(pantalla, NEGRO, [530, 560], [530, 440], 4)

			pygame.draw.circle(pantalla, NEGRO, (390,160),9)
			pygame.draw.circle(pantalla, NEGRO, (390,440),9)
			pygame.draw.circle(pantalla, NEGRO, (670,160),9)
			pygame.draw.circle(pantalla, NEGRO, (670,440),9)

			pygame.draw.circle(pantalla, NEGRO, (530, 160),9)
			pygame.draw.circle(pantalla, NEGRO, (390, 300),9)
			pygame.draw.circle(pantalla, NEGRO, (670, 300),9)
			pygame.draw.circle(pantalla, NEGRO, (530, 440),9)

			if self.numero == 7:
				pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 560], 4)
				pygame.draw.line(pantalla, NEGRO, [270, 300], [790, 300], 3)
				pygame.draw.circle(pantalla, NEGRO, (530,300),9)

		elif self.numero == 9:
			pygame.draw.rect(pantalla, NEGRO, [350, 120, 360, 360], 3)
			pygame.draw.circle(pantalla, NEGRO, (350,120),9)
			pygame.draw.circle(pantalla, NEGRO, (350,480),9)
			pygame.draw.circle(pantalla, NEGRO, (710,120),9)
			pygame.draw.circle(pantalla, NEGRO, (710,480),9)
			pygame.draw.circle(pantalla, NEGRO, (530,120),9)
			pygame.draw.circle(pantalla, NEGRO, (530,480),9)
			pygame.draw.circle(pantalla, NEGRO, (350,300),9)
			pygame.draw.circle(pantalla, NEGRO, (710,300),9)

			pygame.draw.rect(pantalla, NEGRO, [430, 200, 200, 200], 3)
			pygame.draw.circle(pantalla, NEGRO, (430,200),9)
			pygame.draw.circle(pantalla, NEGRO, (430,400),9)
			pygame.draw.circle(pantalla, NEGRO, (630,200),9)
			pygame.draw.circle(pantalla, NEGRO, (630,400),9)
			pygame.draw.circle(pantalla, NEGRO, (530,200),9)
			pygame.draw.circle(pantalla, NEGRO, (530,400),9)
			pygame.draw.circle(pantalla, NEGRO, (430,300),9)
			pygame.draw.circle(pantalla, NEGRO, (630,300),9)
			pygame.draw.line(pantalla, NEGRO, [530, 40], [530, 200], 4)
			pygame.draw.line(pantalla, NEGRO, [270, 300], [430, 300], 3)
			pygame.draw.line(pantalla, NEGRO, [530, 560], [530, 400], 4)
			pygame.draw.line(pantalla, NEGRO, [790, 300], [630, 300], 3)

	def posicionar_ficha(self, pantalla):
		jug1 = pygame.transform.scale(self.jugador1.ficha_color, [50, 50])
		jug2 = pygame.transform.scale(self.jugador2.ficha_color, [50, 50])
		if self.jugadas > 0:
			if self.turno == 0 or self.turno == 2:
				x,y = pygame.mouse.get_pos()
				pos = (x-25,y-25)
				pantalla.blit(jug1,pos)				
				self.jugador1.posiciones.append(pos)
				self.turno=1
				print(self.jugador1.posiciones)
			elif self.turno == 1:
				x,y = pygame.mouse.get_pos()
				pos = (x-25,y-25)
				pantalla.blit(jug2,pos)
				self.jugador2.posiciones.append(pos)
				self.turno=2
				print(self.jugador2.posiciones)
			self.jugadas = self.jugadas-1
		pygame.display.update()