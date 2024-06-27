import pygame
from generales import *

lista_preguntas = []
lista_categorias = ["Historia", "Deporte", "Ciencia", "Entretenimiento", "Geografía"]
diccionario_paths = obtener_paths("archivos\\paths.json")
lista_datos_csv = leer_preguntas_csv(diccionario_paths["path_preguntas"])
crear_diccionario_preguntas(lista_datos_csv, lista_preguntas)

#PYGAME
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255, 255, 255)
VIOLETA = (67, 0, 103)

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
presentador = pygame.image.load(diccionario_paths["path_presentador"])
presentador = pygame.transform.scale(presentador, (375,500))
pygame.display.set_caption("¿Quien quiere ser millonario?")
pygame.display.set_icon(logo)

#FUENTES 
fuente = pygame.font.SysFont("sinsum", 70)
fuente_juego = pygame.font.SysFont("sinsum", 35)

#TEXTOS
texto_play = crear_texto_renderizado("JUGAR", fuente, BLANCO)
texto_salir = crear_texto_renderizado("SALIR", fuente, BLANCO)
texto_elegir_categoria = crear_texto_renderizado("Elija la categoría", fuente, BLANCO)
texto_historia = crear_texto_renderizado("HISTORIA", fuente, BLANCO)
texto_deporte = crear_texto_renderizado("DEPORTE", fuente, BLANCO)
texto_ciencia = crear_texto_renderizado("CIENCIA", fuente, BLANCO)
texto_entretenimiento = crear_texto_renderizado("ENTRETENIMIENTO", fuente, BLANCO)
texto_geografia = crear_texto_renderizado("GEOGRAFIA", fuente, BLANCO)

#RECTÁGUNLOS DE LOS TEXTOS
rect_texto_play = crear_rect_texto(texto_play, (380,515))
rect_texto_salir = crear_rect_texto(texto_salir, (750,515))
rect_texto_categoria = crear_rect_texto(texto_elegir_categoria, (450,365))
rect_texto_historia = crear_rect_texto(texto_historia, (250,500))
rect_texto_deporte = crear_rect_texto(texto_deporte, (527,500))
rect_texto_ciencia = crear_rect_texto(texto_ciencia, (800,500))
rect_texto_entretenimiento = crear_rect_texto(texto_entretenimiento, (200,600))
rect_texto_geografia = crear_rect_texto(texto_geografia, (750,600))

#FONDOS DE LOS TEXTOS
fondo_texto_play = crear_fondo_texto(rect_texto_play, VIOLETA)
fondo_texto_salir = crear_fondo_texto(rect_texto_salir, VIOLETA)
fondo_texto_categoria = crear_fondo_texto(rect_texto_categoria, VIOLETA)
fondo_texto_historia = crear_fondo_texto(rect_texto_historia, VIOLETA)
fondo_texto_deporte = crear_fondo_texto(rect_texto_deporte, VIOLETA)
fondo_texto_ciencia = crear_fondo_texto(rect_texto_ciencia, VIOLETA)
fondo_texto_entretenimiento = crear_fondo_texto(rect_texto_entretenimiento, VIOLETA)
fondo_texto_geografia = crear_fondo_texto(rect_texto_geografia, VIOLETA)

#LISTAS DE ELEMENTOS DE LAS PANTALLAS
lista_elementos_pantalla_menu = [
    (fondo_menu, (0, 0)),
    (logo, (450, 75)),
    (fondo_texto_play, (rect_texto_play)),
    (fondo_texto_salir, (rect_texto_salir)),
    (texto_play, rect_texto_play.topleft),
    (texto_salir, rect_texto_salir.topleft),
]

lista_elementos_pantalla_categorias = [
    (fondo_menu, (0,0)),
    (logo, (450, 0)),
    (fondo_texto_categoria, (rect_texto_categoria)),
    (fondo_texto_historia, (rect_texto_historia)),
    (fondo_texto_deporte, (rect_texto_deporte)),
    (fondo_texto_ciencia, (rect_texto_ciencia)),
    (fondo_texto_entretenimiento, (rect_texto_entretenimiento)),
    (fondo_texto_geografia, (rect_texto_geografia)),
    (texto_elegir_categoria, rect_texto_categoria.topleft),
    (texto_historia, rect_texto_historia.topleft),
    (texto_deporte, rect_texto_deporte.topleft),
    (texto_ciencia, rect_texto_ciencia.topleft),
    (texto_entretenimiento, rect_texto_entretenimiento.topleft),
    (texto_geografia, rect_texto_geografia.topleft)
]


#BUCLE PRINCIPAL
flag_run = True
flag_pantalla_principal = True
flag_pantalla_categorias = False
flag_pantalla_juego = False
flag_boton_salir = True
flag_boton_play = True
flag_pregunta_mostrada = False
flag_respuesta_seleccionada = False

while flag_run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if flag_pantalla_principal:
                if rect_texto_play.collidepoint(evento.pos) and flag_boton_play:
                    flag_pantalla_principal = False
                    flag_boton_salir = False
                    flag_pantalla_categorias = True
                    cargar_pantalla(ventana_principal, lista_elementos_pantalla_categorias)
                elif rect_texto_salir.collidepoint(evento.pos) and flag_boton_salir:
                    flag_run = False
            elif flag_pantalla_categorias:
                if rect_texto_historia.collidepoint(evento.pos):
                    flag_pantalla_juego = True
                    lista_posibles_preguntas = cargar_posibles_preguntas(lista_preguntas, "Historia", "1")
                elif rect_texto_deporte.collidepoint(evento.pos):
                    flag_pantalla_juego = True
                    print("Usted ha elegido Deporte.")
                elif rect_texto_ciencia.collidepoint(evento.pos):
                    flag_pantalla_juego = True
                    print("Usted ha elegido Ciencia.")
                elif rect_texto_entretenimiento.collidepoint(evento.pos):
                    flag_pantalla_juego = True
                    print("Usted ha elegido Entretenimiento.")
                elif rect_texto_geografia.collidepoint(evento.pos):
                    flag_pantalla_juego = True
                    print("Usted ha elegido Geografía.")
        elif flag_pantalla_juego:
            if not flag_pregunta_mostrada:
                pregunta_cargada = cargar_pregunta_aleatoriamente(lista_posibles_preguntas)
                texto_pregunta = crear_texto_renderizado(pregunta_cargada["Pregunta"], fuente_juego, BLANCO)
                rect_texto_pregunta = crear_rect_texto(texto_pregunta, (25,450))
                fondo_texto_pregunta = crear_fondo_texto(rect_texto_pregunta, VIOLETA)
                
                lista_respuestas = crear_lista_respuestas(pregunta_cargada)
                respuesta_correcta = pregunta_cargada["Respuesta_correcta"]

                respuesta_a = lista_respuestas[0]
                respuesta_b = lista_respuestas[1]
                respuesta_c = lista_respuestas[2]
                respuesta_d = lista_respuestas[3]
                
                #region Texto respuestas
                texto_respuesta_a = crear_texto_renderizado(respuesta_a, fuente_juego, BLANCO)
                texto_respuesta_b = crear_texto_renderizado(respuesta_b, fuente_juego, BLANCO)
                texto_respuesta_c = crear_texto_renderizado(respuesta_c, fuente_juego, BLANCO)
                texto_respuesta_d = crear_texto_renderizado(respuesta_d, fuente_juego, BLANCO)
                #endregion
                
                #region Rectángulos respuestas
                rect_respuesta_a = crear_rect_texto(texto_respuesta_a, (25,550))
                rect_respuesta_b = crear_rect_texto(texto_respuesta_b, (450,550))
                rect_respuesta_c = crear_rect_texto(texto_respuesta_c, (25,650))
                rect_respuesta_d = crear_rect_texto(texto_respuesta_d, (450,650))
                #endregion
                
                #region Fondos respuestas
                fondo_texto_respuesta_a = crear_fondo_texto(rect_respuesta_a, VIOLETA)
                fondo_texto_respuesta_b = crear_fondo_texto(rect_respuesta_b, VIOLETA)
                fondo_texto_respuesta_c = crear_fondo_texto(rect_respuesta_c, VIOLETA)
                fondo_texto_respuesta_d = crear_fondo_texto(rect_respuesta_d, VIOLETA)
                #endregion
                
                lista_elementos_pantalla_jugando = [
                    (fondo_menu, (0, 0)),
                    (presentador, (600,250)),
                    (fondo_texto_pregunta, (rect_texto_pregunta)),
                    (fondo_texto_respuesta_a, (rect_respuesta_a)),
                    (fondo_texto_respuesta_b, (rect_respuesta_b)),
                    (fondo_texto_respuesta_c, (rect_respuesta_c)),
                    (fondo_texto_respuesta_d, (rect_respuesta_d)),
                    (texto_pregunta, rect_texto_pregunta.topleft),
                    (texto_respuesta_a, rect_respuesta_a.topleft),
                    (texto_respuesta_b, rect_respuesta_b.topleft),
                    (texto_respuesta_c, rect_respuesta_c.topleft),
                    (texto_respuesta_d, rect_respuesta_d.topleft)
                ]
                
                flag_pantalla_categorias = False
                cargar_pantalla(ventana_principal, lista_elementos_pantalla_jugando)
                flag_pregunta_mostrada = True
            

    if flag_pantalla_principal:
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_menu)
    pygame.display.update()

pygame.quit()

