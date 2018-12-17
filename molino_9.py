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
dimensiones = [720, 460]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Nuevo Juego")
imagen_panel = pygame.image.load("images/panel.png")
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
    panel = pygame.transform.scale(imagen_panel, [680, 420])
    pantalla.blit(panel, [20, 20])
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
    boton_cuadro = pygame.transform.scale(imagen_boton_cuadro, [90, 90])
    boton_cuadro_pressed = pygame.transform.scale(imagen_boton_cuadro_pressed, [90, 90])
    input_text = pygame.transform.scale(imagen_text, [440, 50])

    r_boton_1_1 = imagen_boton.get_rect()
    r_boton_2_1 = boton_cuadro.get_rect()
    r_boton_2_2 = boton_cuadro.get_rect()
    r_boton_2_3 = boton_cuadro.get_rect()
    r_boton_2_4 = boton_cuadro.get_rect()
    r_boton_2_5 = boton_cuadro.get_rect()
    input_text_rect = input_text.get_rect()
    input_text_rect.topleft = [150, 360]
    campo_texto = {'imagen': input_text, 'rect': input_text_rect}

    botones = []
    r_boton_1_1.topleft = [275, 80]
    botones.append({'texto': "Comenzar Juego", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_1, 'on_click': False})
    r_boton_2_1.topleft = [80, 180]
    botones.append({'texto': "3", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_1, 'on_click': False})
    r_boton_2_2.topleft = [200, 180]
    botones.append({'texto': "5", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_2, 'on_click': False})
    r_boton_2_3.topleft = [320, 180]
    botones.append({'texto': "6", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_3, 'on_click': False})
    r_boton_2_4.topleft = [430, 180]
    botones.append({'texto': "7", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_4, 'on_click': False})
    r_boton_2_5.topleft = [550, 180]
    botones.append({'texto': "9", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_5, 'on_click': False})

    dibujar_botones_iniciales(botones)
    click = False
    mostrar_numero = 0
    numero_aleatorio = 0
    texto_entrada = ""
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
        pantalla.blit(input_text, campo_texto['rect'].topleft)
        
        if click and botones[0]['on_click']:
            if len(texto_entrada) != "":
                numero = int(texto_entrada)
                p = Partida(numero)
                p.jugar_partida()
            click = False
        if click:
            for i in range(1, 6):
                if botones[i]['on_click'] and len(texto_entrada) < 4:
                	texto_entrada = botones[i]['texto']
            click = False
        
        set_text(campo_texto, texto_entrada)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()