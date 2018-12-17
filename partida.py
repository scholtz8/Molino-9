from tablero import Tablero
from jugador import Jugador
import pygame
from pygame.locals import *
import os
import sys
import heuristicas as ht

img_panel = pygame.image.load("images/panelInset_beigeLight.png")
Color_titulo = (51,25,0)
AZUL = (0,0,102)
ROJO = (102,0,0)

class Partida(object):

    def __init__(self,num_piezas,nombre1,nombre2):
        self.turno = 1
        self.piezas_por_jugador = num_piezas
        self.jugador1 = Jugador(num_piezas,'A',nombre1)
        self.jugador2 = Jugador(num_piezas,'R',nombre2)
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
        self.cambiar_estado(origen,'V')
        self.cambiar_estado(destino,color)

    # ver si pieza pertenece a un molino
    def en_molino(self,pieza,color):
        molinos = self.tablero.ver_molinos(pieza)
        for molino in molinos:
            contador = 0
            for nodo in molino:
                if self.tablero.ver_estado(nodo) == color:
                    contador += 1
            if contador == 3:
                return True
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
        if self.quien_juega().nombre == 'IA':
            pos = ht.eliminar(self,color)
            pygame.time.delay(1000)
            self.tablero.cambiar_estado(pos,'V')
            self.perder_pieza(self.rival(color).ver_color())                    
        else:
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
        if self.quien_juega().nombre == 'IA':
            pos = ht.posicionar(self,color)
            pygame.time.delay(1000)
            pos = self.tablero.cambiar_estado(pos,color)
            self.restar_pieza()
            return pos
        else:
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
        if self.quien_juega().nombre == 'IA':
            pos,pos2 = ht.mover(self,2,color)
            pygame.time.delay(1000)
            self.tablero.cambiar_estado(pos,'S'+color)
            pygame.time.delay(1000)
            self.tablero.cambiar_estado(pos,'V')
            self.tablero.cambiar_estado(pos2,color)
            return pos2
        else:
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
                                self.tablero.cambiar_estado(pos,'S'+color)
                                pygame.time.delay(250)   
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            sys.exit(0)
                                        if pygame.mouse.get_pressed()[0]:
                                            x,y = pygame.mouse.get_pos()
                                            pos2 = self.tablero.obtener_posicion(x,y)
                                            if pos2 in posibles:
                                                self.tablero.cambiar_estado(pos,'V')
                                                self.tablero.cambiar_estado(pos2,color)
                                                pygame.time.delay(250)
                                                return pos2

    def fase3(self,color):
        if self.quien_juega().nombre == 'IA':
            (pos,pos2) = ht.mover(self,3,color)
            pygame.time.delay(1000)
            self.tablero.cambiar_estado(pos,'S'+color)
            pygame.time.delay(1000)
            self.tablero.cambiar_estado(pos,'V')
            pos2 = self.tablero.cambiar_estado(pos2,color)
            return pos2
        else:
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
                                self.tablero.cambiar_estado(pos,'S'+color)
                                pygame.time.delay(250)  
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            sys.exit(0)
                                        if pygame.mouse.get_pressed()[0]:
                                            x,y = pygame.mouse.get_pos()
                                            pos2 = self.tablero.obtener_posicion(x,y)
                                            if pos2 in vacios:
                                                self.tablero.cambiar_estado(pos,'V')
                                                self.tablero.cambiar_estado(pos2,color)
                                                pygame.time.delay(250)
                                                return pos2                                            

    def gane_o_no(self,color):
        rival = self.rival(color)

        color_rival = rival.ver_color()
        movibles_rival = self.movibles(color_rival)
        no_jugadas_rival = rival.no_jugadas()
        restantes_rival = self.piezas_por_jugador - rival.ver_perdidas()

        if movibles_rival.__len__() == 0 and no_jugadas_rival == 0:
            if color=='A':
                ganador = pygame.image.load("images/ganador_azul.png")
                ganador = pygame.transform.scale(ganador, [1000, 600])
                self.tablero.pantalla_tab.blit(ganador, (30,20))
            else:
                ganador = pygame.image.load("images/ganador_rojo.png")
                ganador = pygame.transform.scale(ganador, [1000, 600])
                self.tablero.pantalla_tab.blit(ganador, (30,20))
            pygame.display.update()    
            return 1
       
        elif restantes_rival < 3:
            if color=='A':
                ganador = pygame.image.load("images/ganador_azul.png")
                ganador = pygame.transform.scale(ganador, [1000, 600])
                self.tablero.pantalla_tab.blit(ganador, (30,20))
            else:
                ganador = pygame.image.load("images/ganador_rojo.png")
                ganador = pygame.transform.scale(ganador, [1000, 600])
                self.tablero.pantalla_tab.blit(ganador, (30,20))
            pygame.display.update()        
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
        self.informacion()
        # despues de jugar revisar si se hizo un molino        
        if self.en_molino(pieza_jugada,color):
            jugador.molino = True
            jugador.molino = jugador.molino+1            
            self.informacion()
            self.eliminar_pieza(color)
        jugador.molino = False
        self.informacion()

        if self.gane_o_no(color)==1:
            pygame.time.delay(10000)
            return 1
        
        self.cambio_turno() 

    #Completa el panel de información
    def informacion(self):
        marcador = pygame.image.load("images/marcador.png")
        marcador = pygame.transform.scale(marcador, [300, 500])
        self.tablero.pantalla_tab.blit(marcador, (900,50))
        fuente = pygame.font.Font(None, 30)
        texto_inicial = "Información de Juego"
        texto_jugador1 = "Jugador Azul"
        texto_jugadas1 = "Fichas jugadas = "+str(self.piezas_por_jugador - self.jugador1.piezas)
        texto_perdidas1 = "Fichas perdidas= "+str(self.jugador1.perdidas)
        texto_molinos1 = "N° molinos= "+str(self.jugador1.num_molino)
        texto_jugador2 = "Jugador Rojo"
        texto_jugadas2 = "Fichas jugadas = "+str(self.piezas_por_jugador - self.jugador2.piezas)
        texto_perdidas2 = "Fichas perdidas= "+str(self.jugador2.perdidas)
        texto_molinos2 = "N° molinos= "+str(self.jugador1.num_molino)
        texto = fuente.render(texto_inicial, True, Color_titulo)
        linea11 = fuente.render(texto_jugador1, True, AZUL)
        linea12 = fuente.render(texto_jugadas1, True, AZUL)
        linea13 = fuente.render(texto_perdidas1, True, AZUL)
        linea14 = fuente.render(texto_molinos1, True, AZUL)
        linea21 = fuente.render(texto_jugador2, True, ROJO)
        linea22 = fuente.render(texto_jugadas2, True, ROJO)
        linea23 = fuente.render(texto_perdidas2, True, ROJO)
        linea24 = fuente.render(texto_molinos2, True, ROJO)
        self.tablero.pantalla_tab.blit(texto, [930, 80])
        self.tablero.pantalla_tab.blit(linea11, [915, 105])
        self.tablero.pantalla_tab.blit(linea12, [915, 125])
        self.tablero.pantalla_tab.blit(linea13, [915, 145])
        self.tablero.pantalla_tab.blit(linea14, [915, 165])

        self.tablero.pantalla_tab.blit(linea21, [915, 205])
        self.tablero.pantalla_tab.blit(linea22, [915, 225])
        self.tablero.pantalla_tab.blit(linea23, [915, 245])
        self.tablero.pantalla_tab.blit(linea24, [915, 265])
        if self.turno == 1:
            texto_jugador = "Es turno del Jugador Rojo"
            linea = fuente.render(texto_jugador, True, ROJO)
            self.tablero.pantalla_tab.blit(linea, [915, 300])    
        elif self.turno == 2:
            texto_jugador = "Es turno del Jugador Azul"
            linea = fuente.render(texto_jugador, True, AZUL)
            self.tablero.pantalla_tab.blit(linea, [915, 300])  
        
        texto_jugador = "Molino formado"
        texto_eliminar = "Seleccione una pieza del"
        texto_eliminar2="contrincante"
        if self.jugador1.molino:           
            linea_molino = fuente.render(texto_jugador, True, AZUL) 
            self.tablero.pantalla_tab.blit(linea_molino, [915, 320])
            linea_eliminar = fuente.render(texto_eliminar, True, AZUL) 
            self.tablero.pantalla_tab.blit(linea_eliminar, [915, 340])
            linea_eliminar2 = fuente.render(texto_eliminar2, True, AZUL) 
            self.tablero.pantalla_tab.blit(linea_eliminar2, [915, 360])
        elif self.jugador2.molino:
            linea_molino = fuente.render(texto_jugador, True, ROJO)
            self.tablero.pantalla_tab.blit(linea_molino, [915, 320])
            linea_eliminar = fuente.render(texto_eliminar, True, ROJO) 
            self.tablero.pantalla_tab.blit(linea_eliminar, [915, 340])      
            linea_eliminar2 = fuente.render(texto_eliminar2, True, ROJO) 
            self.tablero.pantalla_tab.blit(linea_eliminar2, [915, 360])
        pygame.display.update()

    def jugar_partida(self):
        panel = pygame.transform.scale(img_panel, [1020, 630])
        self.tablero.dibujar_tablero()
        while True:
            if self.jugar_turno() == 1:
                pantalla = pygame.display.set_mode([1080, 690])
                pygame.display.update()
                break
            else:
                continue
'''

'''
