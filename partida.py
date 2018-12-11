from tablero import Tablero
from jugador import Jugador
import pygame
from pygame.locals import *
from functools import partial

class Partida(object):

    def __init__(self,num_piezas):
        self.turno = 1
        self.piezas_por_jugador = num_piezas
        self.jugador1 = Jugador(num_piezas,'A')
        self.jugador2 = Jugador(num_piezas,'R')
        self.tablero = Tablero(num_piezas)

    #cambiar a turno entre el jugador 1 y 2
    def cambio_turno(self):
        if self.turno == 1:
            self.turno = 2
        elif self.turno == 2:
            self.turno = 1
            
    def quien_juega(self):
        if self.turno == 1:
            return self.jugador1
        elif self.turno == 2:
            return self.jugador2

    def quien_es(self,color):
        if color == 'A':
            return self.jugador1
        elif color == 'R':
            return self.jugador2

    def vacios(self):
        vacios = []
        tam = self.tablero.tam_tablero() + 1
        for i in range(1,tam):
            if self.tablero.ver_estado(i) == 'V':
                vacios.append(i)
        return vacios

    # lista con las piezas en juego del jugador
    def en_juego(self,color):
        piezas = []
        tam = self.tablero.tam_tablero() + 1
        for i in range(1,tam):
            if self.tablero.ver_estado(i) == color:
                piezas.append(i)
        return piezas

    # lista con las piezas que el jugador puede mover
    def movibles(self,color):
        piezas_jugador = self.en_juego(color)
        movibles = []
        for pieza in piezas_jugador:
            adyacentes = self.tablero.adyacentes(pieza)
            count = 0
            for nodo in adyacentes:
                if self.tablero.ver_estado(nodo) == 'V':
                    count += 1
            if count > 0:
                movibles.append(pieza)                
        return movibles
    
    # lista con los lugares disponibles a los que se puede mover una pieza
    def movimientos_posibles(self,pieza):
        vacias = []
        adyacentes = self.tablero.adyacentes(pieza)
        for nodo in adyacentes:
            if self.tablero.ver_estado(nodo) == 'V':
                vacias.append(nodo)
        return vacias

    # mueve una pieza de un lugar a otro
    def mover_pieza(self,origen,destino,color):
        self.tablero.cambiar_estado(origen,'V')
        self.tablero.cambiar_estado(destino,color)

    # ver si pieza pertenece a un molino
    def en_molino(self,pieza,color):
        print('en molino')
        molinos = self.tablero.ver_molinos(pieza)
        for molino in molinos:
            contador = 0
            for nodo in molino:
                if self.tablero.ver_estado(nodo) == color:
                    contador += 1
            if contador == 3:
                print('true')
                return True
        print('false')    
        return False

    # obtener el jugador oponente
    def rival(self,color_jugador):
        if color_jugador == 'A':
            return self.jugador2
        elif color_jugador == 'R':
            return self.jugador1

    # lista de piezas que pueden ser eliminadas
    def eliminables(self,color): 
        en_juego = self.en_juego(color)
        no_molinos = []
        for pieza in en_juego:
            if self.en_molino(pieza,color) == False:
                no_molinos.append(pieza)
        if no_molinos.__len__() == 0:
            return en_juego
        else:
            return no_molinos

    def perder_pieza(self,color):
        self.quien_es(color).sumar_perdidas()

    def eliminar_pieza(self,color):
        color_rival = self.rival(color).ver_color()
        eliminables = self.eliminables(color_rival)        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if pygame.mouse.get_pressed()[0]:
                    x,y = pygame.mouse.get_pos()
                    pos = self.tablero.obtener_posicion(x,y)
                    if pos in eliminables:
                        self.tablero.cambiar_estado(pos,'V')
                        self.perder_pieza(color_rival)
                        return        

    def restar_pieza(self):
        self.quien_juega().restar_piezas()

    # fase de colocar piezas en el tablero
    def fase1(self,color):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if pygame.mouse.get_pressed()[0]:
                    x,y = pygame.mouse.get_pos()
                    pos = self.tablero.obtener_posicion(x,y)
                    pos = self.tablero.cambiar_estado(pos,color)
                    if pos:
                        self.restar_pieza()
                        return pos

    def fase2(self,color):
        movibles = self.movibles(color)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if pygame.mouse.get_pressed()[0]:
                    x,y = pygame.mouse.get_pos()
                    pos = self.tablero.obtener_posicion(x,y)
                    if pos:
                        if pos in movibles:
                            posibles = self.movimientos_posibles(pos)  
                            self.tablero.cambiar_estado(pos,'V')
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit(0)
                                    if pygame.mouse.get_pressed()[0]:
                                        x,y = pygame.mouse.get_pos()
                                        pos2 = self.tablero.obtener_posicion(x,y)
                                        if pos2 in posibles:
                                            self.tablero.cambiar_estado(pos2,self.quien_juega().ver_color())
                                            return pos2

    def fase3(self,color):
        movibles = self.en_juego(color)
        vacios = self.vacios()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if pygame.mouse.get_pressed()[0]:
                    x,y = pygame.mouse.get_pos()
                    pos = self.tablero.obtener_posicion(x,y)
                    if pos:
                        if pos in movibles:
                            posibles = self.movimientos_posibles(pos)  
                            self.tablero.cambiar_estado(pos,'V')
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit(0)
                                    if pygame.mouse.get_pressed()[0]:
                                        x,y = pygame.mouse.get_pos()
                                        pos2 = self.tablero.obtener_posicion(x,y)
                                        if pos2 in vacios:
                                            self.tablero.cambiar_estado(pos2,self.quien_juega().ver_color())
                                            return pos2

    def gane_o_no(self,color):
        rival = self.rival(color)

        color_rival = rival.ver_color()
        movibles_rival = self.movibles(color_rival)
        no_jugadas_rival = rival.no_jugadas()
        if movibles_rival.__len__() == 0 and no_jugadas_rival == 0:
            print(color, 'GANA')
            return 1

        restantes_rival = self.piezas_por_jugador - rival.ver_perdidas()
        if restantes_rival < 3:
            print(color, 'GANA')
            return 1

    def jugar_turno(self):
        #self.ver_juego()
        # jugar dependiendo en la fase de juego que se encuentra el jugador
        # self.quien_juega determina el jugador que le toca
        jugador = self.quien_juega()
        color = jugador.ver_color()
        piezas_sin_jugar = jugador.no_jugadas()
        piezas_restantes = self.piezas_por_jugador - jugador.ver_perdidas()

        if piezas_sin_jugar > 0:
            pieza_jugada = self.fase1(color)
        else:
            if piezas_restantes > 3:
                pieza_jugada = self.fase2(color)
            else:
                pieza_jugada = self.fase3(color)
        
        # despues de jugar revisar si se hizo un molino
        
        if self.en_molino(pieza_jugada,color):
            self.eliminar_pieza(color)
        
        if self.gane_o_no(color) == 1:
            return 1
        
        self.cambio_turno()   

    def jugar_partida(self):
        self.tablero.dibujar_tablero()   
        while True:
            if self.jugar_turno() == 1:
                pantalla = pygame.display.set_mode([720, 460])
                pygame.display.update()
                break
            else:
                continue
