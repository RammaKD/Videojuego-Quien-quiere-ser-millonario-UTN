import pygame
from funciones_visuales import *

pygame.init()

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255, 255, 255)
VIOLETA = (67, 0, 103)

# Dimensiones de la ventana y posiciones
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
DIMENSIONES_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)
POS_INICIAL_FONDO = (0,0)
POS_INICIAL_PRESENTADOR = (650, 250)
POS_RESP_A = (25, 550)
POS_RESP_B = (450, 550) 
POS_RESP_C = (25, 650)
POS_RESP_D = (450, 650)

# Fuentes
FUENTE_PRINCIPAL = pygame.font.SysFont("sinsum", 75)
FUENTE_PANTALLA_JUEGO =  pygame.font.SysFont("sinsum", 35)
FUENTE_CRONOMETRO =  pygame.font.SysFont("sinsum", 75)
FUENTE_COMODINES =  pygame.font.SysFont("sinsum", 60)
FUENTE_PANTALLA_GAME_OVER =  pygame.font.SysFont("sinsum", 90)
FUENTE_PIRAMIDE_PREMIOS =  pygame.font.SysFont("sinsum", 50)

#Evento propio
CRONOMETRO = pygame.USEREVENT


