import pygame
from generales import *

lista_preguntas = []
lista_preguntas_superadas = []
lista_categorias = ["Historia", "Deporte", "Ciencia", "Entretenimiento", "Geografía"]
diccionario_paths = obtener_paths("archivos\\paths.json")
lista_datos_csv = leer_preguntas_csv(diccionario_paths["path_preguntas"])
crear_diccionario_preguntas(lista_datos_csv, lista_preguntas)
lista_posibles_preguntas = cargar_posibles_preguntas(lista_preguntas, lista_preguntas_superadas, "Historia", "1")
pregunta_cargada = cargar_pregunta_aleatoriamente(lista_posibles_preguntas)
lista_respuestas = crear_lista_respuestas(pregunta_cargada)

#PYGAME
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255, 255, 255)

ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
DIMENSIONES_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)
DIMENSIONES_BOTON = (280,70)

pygame.init()

ventana_principal = pygame.display.set_mode(DIMENSIONES_VENTANA)
ventana_principal.fill(BLANCO)
logo = pygame.image.load(diccionario_paths["path_logo"])
logo = pygame.transform.scale(logo, (400,350))
fondo_menu = pygame.image.load(diccionario_paths["path_fondo_menu"])
fondo_menu = pygame.transform.scale(fondo_menu, DIMENSIONES_VENTANA)
boton = pygame.image.load(diccionario_paths["path_boton"])
boton = pygame.transform.scale(boton, DIMENSIONES_BOTON)
fuente = pygame.font.SysFont("sinsum", 75)
texto_play = fuente.render("JUGAR", False, BLANCO)
texto_salir = fuente.render("SALIR", False, BLANCO)

pygame.display.set_caption("¿Quien quiere ser millonario?")
pygame.display.set_icon(logo)

lista_elementos_pantalla_menu = [(fondo_menu, (0,0)), (logo, (450,75)), (boton, (330,500)), (boton, (690,500)),
                                 (texto_play, (380,515)), (texto_salir, (750,515))]

flag_run = True
while flag_run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_run = False

    cargar_pantalla_menu(ventana_principal, lista_elementos_pantalla_menu)
    pygame.display.update()

pygame.quit()

