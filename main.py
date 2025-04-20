import pygame
from generales import *
from configuraciones import *
from elementos import *
from eventos import *
from funciones_visuales import *
from especificas import *

pygame.init()

crear_diccionario_preguntas(lista_datos_csv, lista_preguntas)
while estado_juego["flags_variables"]["run"]:

    manejar_eventos(estado_juego, elementos_pantalla)
    actualizar_pantalla(estado_juego, elementos_pantalla, ventana_principal)
    pygame.display.update()

pygame.quit()


