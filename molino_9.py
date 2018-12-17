import pygame
import random
from pygame.locals import *
from partida import Partida
import os
import sys

FONDO = (32, 30, 32)
BLANCO = (255, 255, 255)
COLOR_TEXTO = (50, 60, 80)

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
dimensiones = [1080, 690]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Nuevo Juego")
imagen_panel = pygame.image.load("images/panel.png")
imagen_molino = pygame.image.load("images/molino.png")
imagen_boton = pygame.image.load("images/button.png")
imagen_boton_pressed = pygame.image.load("images/buttonPressed.png")
imagen_boton_cuadro = pygame.image.load("images/buttonSquare.png")
imagen_boton_cuadro_pressed = pygame.image.load("images/buttonSquarePressed.png")
imagen_text = pygame.image.load("images/panelInset_brown.png")
icon = pygame.image.load("images/molino.png")
fuente = pygame.font.SysFont('Courier', 20)
fuente_numero = pygame.font.SysFont('Pacifico Regular', 30)


def dibujar_texto(texto, contenedor_imagen, contenedor_rec, fuente_render, color):
    text = fuente_render.render(texto, 1, color)
    centro = text.get_rect()
    diferencia_x = contenedor_imagen.center[0] - centro.center[0]
    diferencia_y = contenedor_imagen.center[1] - centro.center[1]
    pantalla.blit(text, [contenedor_rec.left + diferencia_x, contenedor_rec.top + diferencia_y])

def dibujar_botones_iniciales(lista_botones):
    panel = pygame.transform.scale(imagen_panel, [1020, 630])
    pantalla.blit(panel, [30, 20])
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])
        dibujar_texto(boton['texto'], boton['imagen'].get_rect(), boton['rect'], fuente, BLANCO)

def set_text(campo, texto):
    dibujar_texto(texto, campo['imagen'].get_rect(), campo['rect'], fuente_numero, COLOR_TEXTO)

def main():
    game_over = False
    clock = pygame.time.Clock()
    pygame.display.set_icon(icon)
    boton_cuadro = pygame.transform.scale(imagen_boton_cuadro, [120, 60])
    boton_cuadro_pressed = pygame.transform.scale(imagen_boton_cuadro_pressed, [120, 60])
    boton_cuadro2 = pygame.transform.scale(imagen_boton_cuadro, [190, 60])
    boton_cuadro2_pressed = pygame.transform.scale(imagen_boton_cuadro_pressed, [190, 60])
    input_text = pygame.transform.scale(imagen_text, [300, 50])
    #icono_juego = pygame.transform.scale(imagen_molino, [100, 50])

    r_boton_1_1 = imagen_boton.get_rect()
    r_boton_2_1 = boton_cuadro.get_rect()
    r_boton_2_2 = boton_cuadro.get_rect()
    r_boton_2_3 = boton_cuadro.get_rect()
    r_boton_2_4 = boton_cuadro.get_rect()
    r_boton_2_5 = boton_cuadro.get_rect()
    r_boton_3_1 = boton_cuadro.get_rect()
    r_boton_3_2 = boton_cuadro.get_rect()
    texto_1_0 = boton_cuadro.get_rect()
    input_text_rect = input_text.get_rect()
    icono_juego_rect = imagen_molino.get_rect()
    input_text_rect.topleft = [400, 540]
    icono_juego_rect.topleft = [220, 120]
    campo_texto = {'imagen': input_text, 'rect': input_text_rect}
    campo_icono = {'imagen': imagen_molino, 'rect': icono_juego_rect}

    COLOR_TITULO = (94,42,65)
    texto_inicio = "Elige tamaño de tablero y opción de juego para comenzar"
    font_texto_inicio = fuente.render(texto_inicio, True, COLOR_TITULO)

    botones = []
    r_boton_2_1.topleft = [160, 380]
    botones.append({'texto': "3", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_1, 'on_click': False})
    r_boton_2_2.topleft = [320, 380]
    botones.append({'texto': "5", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_2, 'on_click': False})
    r_boton_2_3.topleft = [480, 380]
    botones.append({'texto': "6", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_3, 'on_click': False})
    r_boton_2_4.topleft = [640, 380]
    botones.append({'texto': "7", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_4, 'on_click': False})
    r_boton_2_5.topleft = [800, 380]
    botones.append({'texto': "9", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_5, 'on_click': False})
    r_boton_3_1.topleft = [340, 460]
    botones.append({'texto': "Jug1 vs Jug2", 'imagen': boton_cuadro2, 'imagen_pressed': boton_cuadro2_pressed, 'rect': r_boton_3_1, 'on_click': False})
    r_boton_3_2.topleft = [560, 460]
    botones.append({'texto': "Jug1 vs IA ", 'imagen': boton_cuadro2, 'imagen_pressed': boton_cuadro2_pressed, 'rect': r_boton_3_2, 'on_click': False})

    dibujar_botones_iniciales(botones)
    click = False
    mostrar_numero = 0
    numero_aleatorio = 0
    texto_entrada = ""
    opcion_jugador = ""
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
                    
        pantalla.fill(FONDO)
        dibujar_botones_iniciales(botones)         
        pantalla.blit(font_texto_inicio, [220, 360])
        pantalla.blit(input_text, campo_texto['rect'].topleft)
        pantalla.blit(imagen_molino, campo_icono['rect'].topleft)
        ##botones[5] corresponde a selección jug1 vs jug2
        ##mientras que botones[6] corresponde a la selección de jug1 vs IA
        if click and botones[5]['on_click']:
            if len(texto_entrada) != "":
                numero = int(texto_entrada)
                p = Partida(numero,'j1','j2')
                p.jugar_partida()
            click = False
        elif click and botones[6]['on_click']:            
            if len(texto_entrada) != "":
                numero = int(texto_entrada)
                p = Partida(numero,'j1','IA')
                p.jugar_partida()
            click = False
        if click:
            for i in range(0, 5):
                if botones[i]['on_click'] and len(texto_entrada) < 4:
                	texto_entrada = botones[i]['texto']
            click = False
        
        set_text(campo_texto, texto_entrada)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()