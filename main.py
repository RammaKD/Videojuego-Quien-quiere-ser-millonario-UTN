import pygame
from generales import *
from configuraciones import *
from elementos import *
from eventos import *
from funciones_visuales import *
from especificas import *


pygame.init()

while estado_juego["flags_variables"]["run"]:
    crear_diccionario_preguntas(lista_datos_csv, estado_juego["lista_preguntas"])
    manejar_eventos(estado_juego, elementos_pantalla)
    actualizar_pantalla(estado_juego, elementos_pantalla, ventana_principal)
    pygame.display.update()

pygame.quit()


