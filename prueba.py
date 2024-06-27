import pygame
from generales import *

lista_preguntas = []
lista_categorias = ["Historia", "Deporte", "Ciencia", "Entretenimiento", "Geografía"]
diccionario_paths = obtener_paths("archivos\\paths.json")
lista_datos_csv = leer_preguntas_csv(diccionario_paths["path_preguntas"])
crear_diccionario_preguntas(lista_datos_csv, lista_preguntas)

niveles_premios = [
    [1, "$100"],
    [2, "$200"],
    [3, "$300"],
    [4, "$500"],
    [5, "$1000"],
    [6, "$2000"],
    [7, "$4000"],
    [8, "$8000"],
    [9, "$16000"],
    [10, "$32000"],
    [11, "$64000"],
    [12, "$125000"],
    [13, "$250000"],
    [14, "$500000"],
    [15, "$1000000"],
]


# Inicializa Pygame
pygame.init()

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255, 255, 255)
VIOLETA = (67, 0, 103)

# Dimensiones de la ventana
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
DIMENSIONES_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)
DIMENSIONES_BOTON = (280, 70)

ventana_principal = pygame.display.set_mode(DIMENSIONES_VENTANA)
ventana_principal.fill(BLANCO)
logo = pygame.image.load(diccionario_paths["path_logo"])
logo = pygame.transform.scale(logo, (400, 350))
fondo_menu = pygame.image.load(diccionario_paths["path_fondo_menu"])
fondo_menu = pygame.transform.scale(fondo_menu, DIMENSIONES_VENTANA)
presentador = pygame.image.load(diccionario_paths["path_presentador"])
presentador = pygame.transform.scale(presentador, (375, 500))
pygame.display.set_caption("¿Quién quiere ser millonario?")
pygame.display.set_icon(logo)

# Fuentes
fuente = pygame.font.SysFont("sinsum", 70)
fuente_juego = pygame.font.SysFont("sinsum", 35)
fuente_cronometro = pygame.font.SysFont("sinsum", 75)

# Textos
texto_play = crear_texto_renderizado("JUGAR", fuente, BLANCO)
texto_salir = crear_texto_renderizado("SALIR", fuente, BLANCO)
texto_elegir_categoria = crear_texto_renderizado("Elija la categoría", fuente, BLANCO)
texto_historia = crear_texto_renderizado("HISTORIA", fuente, BLANCO)
texto_deporte = crear_texto_renderizado("DEPORTE", fuente, BLANCO)
texto_ciencia = crear_texto_renderizado("CIENCIA", fuente, BLANCO)
texto_entretenimiento = crear_texto_renderizado("ENTRETENIMIENTO", fuente, BLANCO)
texto_geografia = crear_texto_renderizado("GEOGRAFIA", fuente, BLANCO)

# Rectángulos de los textos
rect_texto_play = crear_rect_texto(texto_play, (380, 515))
rect_texto_salir = crear_rect_texto(texto_salir, (750, 515))
rect_texto_categoria = crear_rect_texto(texto_elegir_categoria, (450, 365))
rect_texto_historia = crear_rect_texto(texto_historia, (250, 500))
rect_texto_deporte = crear_rect_texto(texto_deporte, (527, 500))
rect_texto_ciencia = crear_rect_texto(texto_ciencia, (800, 500))
rect_texto_entretenimiento = crear_rect_texto(texto_entretenimiento, (200, 600))
rect_texto_geografia = crear_rect_texto(texto_geografia, (750, 600))

# Fondos de los textos
fondo_texto_play = crear_fondo_texto(rect_texto_play, VIOLETA)
fondo_texto_salir = crear_fondo_texto(rect_texto_salir, VIOLETA)
fondo_texto_categoria = crear_fondo_texto(rect_texto_categoria, VIOLETA)
fondo_texto_historia = crear_fondo_texto(rect_texto_historia, VIOLETA)
fondo_texto_deporte = crear_fondo_texto(rect_texto_deporte, VIOLETA)
fondo_texto_ciencia = crear_fondo_texto(rect_texto_ciencia, VIOLETA)
fondo_texto_entretenimiento = crear_fondo_texto(rect_texto_entretenimiento, VIOLETA)
fondo_texto_geografia = crear_fondo_texto(rect_texto_geografia, VIOLETA)

# Listas de elementos de las pantallas
lista_elementos_pantalla_menu = [
    (fondo_menu, (0, 0)),
    (logo, (450, 75)),
    (fondo_texto_play, (rect_texto_play)),
    (fondo_texto_salir, (rect_texto_salir)),
    (texto_play, rect_texto_play.topleft),
    (texto_salir, rect_texto_salir.topleft),
]

lista_elementos_pantalla_categorias = [
    (fondo_menu, (0, 0)),
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


contador_cronometro = 10
CRONOMETRO = pygame.USEREVENT + 1  
pygame.time.set_timer(CRONOMETRO, 0)  

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
                if flag_pantalla_juego:
                    flag_pantalla_categorias = False
                    flag_pregunta_mostrada = False
                    flag_respuesta_seleccionada = False
                    contador_cronometro = 10
                    texto_cronometro = str(contador_cronometro).zfill(2)
                    pygame.time.set_timer(CRONOMETRO, 1000)
            elif flag_pantalla_juego:
                if rect_respuesta_a.collidepoint(evento.pos):
                    print("Respuesta A seleccionada")
                    flag_respuesta_seleccionada = True
                elif rect_respuesta_b.collidepoint(evento.pos):
                    print("Respuesta B seleccionada")
                    flag_respuesta_seleccionada = True
                elif rect_respuesta_c.collidepoint(evento.pos):
                    print("Respuesta C seleccionada")
                    flag_respuesta_seleccionada = True
                elif rect_respuesta_d.collidepoint(evento.pos):
                    print("Respuesta D seleccionada")
                    flag_respuesta_seleccionada = True

        elif evento.type == CRONOMETRO:
            contador_cronometro -= 1
            texto_cronometro = str(contador_cronometro).zfill(2)
            if contador_cronometro <= 0:
                print("Se le acabó el tiempo")
                flag_respuesta_seleccionada = True

    if flag_pantalla_principal:
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_menu)
    
    if flag_pantalla_juego and not flag_pregunta_mostrada:
        
        pregunta_cargada = cargar_pregunta_aleatoriamente(lista_posibles_preguntas)
        texto_pregunta = crear_texto_renderizado(pregunta_cargada["Pregunta"], fuente_juego, BLANCO)
        rect_texto_pregunta = crear_rect_texto(texto_pregunta, (25, 450))
        fondo_texto_pregunta = crear_fondo_texto(rect_texto_pregunta, VIOLETA)

        lista_respuestas = crear_lista_respuestas(pregunta_cargada)
        respuesta_correcta = pregunta_cargada["Respuesta_correcta"]

        respuesta_a = lista_respuestas[0]
        respuesta_b = lista_respuestas[1]
        respuesta_c = lista_respuestas[2]
        respuesta_d = lista_respuestas[3]

        # Texto respuestas
        texto_respuesta_a = crear_texto_renderizado(respuesta_a, fuente_juego, BLANCO)
        texto_respuesta_b = crear_texto_renderizado(respuesta_b, fuente_juego, BLANCO)
        texto_respuesta_c = crear_texto_renderizado(respuesta_c, fuente_juego, BLANCO)
        texto_respuesta_d = crear_texto_renderizado(respuesta_d, fuente_juego, BLANCO)

        # Rectángulos respuestas
        rect_respuesta_a = crear_rect_texto(texto_respuesta_a, (25, 550))
        rect_respuesta_b = crear_rect_texto(texto_respuesta_b, (450, 550))
        rect_respuesta_c = crear_rect_texto(texto_respuesta_c, (25, 650))
        rect_respuesta_d = crear_rect_texto(texto_respuesta_d, (450, 650))

        # Fondos respuestas
        fondo_texto_respuesta_a = crear_fondo_texto(rect_respuesta_a, VIOLETA)
        fondo_texto_respuesta_b = crear_fondo_texto(rect_respuesta_b, VIOLETA)
        fondo_texto_respuesta_c = crear_fondo_texto(rect_respuesta_c, VIOLETA)
        fondo_texto_respuesta_d = crear_fondo_texto(rect_respuesta_d, VIOLETA)

        # Cronómetro
        texto_cronometro_render = crear_texto_renderizado(texto_cronometro, fuente_cronometro, BLANCO)
        rect_texto_cronometro = crear_rect_texto(texto_cronometro_render, (25, 50))
        fondo_texto_cronometro = crear_fondo_texto(rect_texto_cronometro, VIOLETA)

        lista_elementos_pantalla_jugando = [
            (fondo_menu, (0, 0)),
            (presentador, (600, 250)),
            (fondo_texto_pregunta, (rect_texto_pregunta)),
            (fondo_texto_respuesta_a, (rect_respuesta_a)),
            (fondo_texto_respuesta_b, (rect_respuesta_b)),
            (fondo_texto_respuesta_c, (rect_respuesta_c)),
            (fondo_texto_respuesta_d, (rect_respuesta_d)),
            (texto_pregunta, rect_texto_pregunta.topleft),
            (texto_respuesta_a, rect_respuesta_a.topleft),
            (texto_respuesta_b, rect_respuesta_b.topleft),
            (texto_respuesta_c, rect_respuesta_c.topleft),
            (texto_respuesta_d, rect_respuesta_d.topleft),
            (fondo_texto_cronometro, rect_texto_cronometro.topleft),
            (texto_cronometro_render, rect_texto_cronometro.topleft)
        ]

        flag_pregunta_mostrada = True
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_jugando)
        dibujar_piramide_premios(ventana_principal, niveles_premios, ANCHO_VENTANA, BLANCO, VIOLETA)

    if flag_pantalla_juego and flag_respuesta_seleccionada:
        flag_pantalla_juego = False
        flag_pregunta_mostrada = False
        flag_respuesta_seleccionada = False
        flag_pantalla_principal = True
        contador_cronometro = 10
        texto_cronometro = str(contador_cronometro).zfill(2)
        pygame.time.set_timer(CRONOMETRO, 0)  

    if flag_pantalla_juego:
        texto_cronometro_render = crear_texto_renderizado(texto_cronometro, fuente_cronometro, BLANCO)
        rect_texto_cronometro = crear_rect_texto(texto_cronometro_render, (25, 50))
        fondo_texto_cronometro = crear_fondo_texto(rect_texto_cronometro, VIOLETA)
        ventana_principal.blit(fondo_texto_cronometro, rect_texto_cronometro.topleft)
        ventana_principal.blit(texto_cronometro_render, rect_texto_cronometro.topleft)

    pygame.display.update()

pygame.quit()