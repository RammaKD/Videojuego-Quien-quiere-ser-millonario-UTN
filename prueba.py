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
POS_INICIAL = (0,0)
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

lista_elementos_menu_principal_inicial = []
lista_elementos_menu_categorias_inicial = []
lista_textos_menu = ["JUGAR", "SALIR"]
lista_textos_categorias = ["Elija la categoria", "HISTORIA", "DEPORTE" ,"CIENCIA" , "ENTRETENIMIENTO", "GEOGRAFÍA"]
lista_pos_texto_menu = [(380, 515),(750, 515)]
lista_pos_texto_categorias = [(450, 365),
                             (250, 500),
                             (527, 500),
                             (800, 500),
                             (200, 600),
                             (750, 600)]

lista_imgs_menu_principal = [(fondo_menu, POS_INICIAL), (logo, (450,75))]
lista_imgs_menu_categorias = [(fondo_menu, POS_INICIAL), (logo, (450,0))]
lista_elementos_menu_principal_inicial += lista_imgs_menu_principal
lista_elementos_menu_categorias_inicial += lista_imgs_menu_principal

lista_renders_menu = listar_renders(lista_textos_menu, fuente, BLANCO)
lista_renders_categorias = listar_renders(lista_textos_categorias, fuente, BLANCO)

lista_rects_menu = listar_rects(lista_renders_menu, lista_pos_texto_menu)
lista_rects_categorias = listar_rects(lista_renders_categorias, lista_pos_texto_categorias)

lista_fondos_menu = listar_fondos(lista_rects_menu, VIOLETA)
lista_fondos_categorias = listar_fondos(lista_rects_categorias, VIOLETA)

lista_elementos_menu_interactivos = generar_lista_elementos(lista_renders_menu, lista_rects_menu, lista_fondos_menu)
lista_elementos_menu_categorias_interactivos = generar_lista_elementos(lista_renders_categorias, lista_rects_categorias, lista_fondos_categorias)

lista_elementos_menu = lista_elementos_menu_principal_inicial + lista_elementos_menu_interactivos
lista_elementos_menu_categorias = lista_elementos_menu_categorias_inicial + lista_elementos_menu_categorias_interactivos

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
flag_respuesta_correcta = False
contador_nivel = 1
flag_cronometro_activo = True

while flag_run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if flag_pantalla_principal:
                if lista_rects_menu[0].collidepoint(evento.pos) and flag_boton_play:
                    flag_pantalla_principal = False
                    flag_boton_salir = False
                    flag_pantalla_categorias = True
                    cargar_pantalla(ventana_principal, lista_elementos_menu_categorias)
                elif lista_rects_menu[1].collidepoint(evento.pos) and flag_boton_salir:
                    flag_run = False
            elif flag_pantalla_categorias:
                if lista_rects_categorias[1].collidepoint(evento.pos):
                    flag_pantalla_juego = True
                    categoria_elegida = "Historia"
                elif lista_rects_categorias[2].collidepoint(evento.pos):
                    flag_pantalla_juego = True
                    categoria_elegida = "Deportes"
                elif lista_rects_categorias[3].collidepoint(evento.pos):
                    flag_pantalla_juego = True
                    categoria_elegida = "Ciencia"
                elif lista_rects_categorias[4].collidepoint(evento.pos):
                    flag_pantalla_juego = True
                    categoria_elegida = "Entretenimiento"
                elif lista_rects_categorias[5].collidepoint(evento.pos):
                    flag_pantalla_juego = True
                    categoria_elegida = "Geografía"
                flag_cronometro_activo = True

                if flag_pantalla_juego:
                    flag_pantalla_categorias = False
                    flag_pregunta_mostrada = False
                    flag_respuesta_seleccionada = False
                    contador_cronometro = 10
                    texto_cronometro = str(contador_cronometro).zfill(2)
                    pygame.time.set_timer(CRONOMETRO, 1000)
            
            elif flag_pantalla_juego:
                respuesta_seleccionada = None

                if lista_rects_jugando[2].collidepoint(evento.pos):
                    respuesta_seleccionada = lista_respuestas[0]
                elif lista_rects_jugando[3].collidepoint(evento.pos):
                    respuesta_seleccionada = lista_respuestas[1]
                elif lista_rects_jugando[4].collidepoint(evento.pos):
                    respuesta_seleccionada = lista_respuestas[2]
                elif lista_rects_jugando[5].collidepoint(evento.pos):
                    respuesta_seleccionada = lista_respuestas[3]

                if respuesta_seleccionada is not None:
                    if respuesta_seleccionada == respuesta_correcta:
                        print("Respuesta correcta")
                        flag_respuesta_correcta = True
                    else:
                        print("Respuesta incorrecta")
                        flag_respuesta_correcta = False
                    flag_respuesta_seleccionada = True

            
        elif evento.type == CRONOMETRO and flag_cronometro_activo:
            contador_cronometro -= 1
            texto_cronometro = str(contador_cronometro).zfill(2)
            if contador_cronometro <= 0:
                print("Se le acabó el tiempo\n1")
                flag_respuesta_seleccionada = True
                flag_respuesta_correcta = False

    if flag_pantalla_principal:
        cargar_pantalla(ventana_principal, lista_elementos_menu)
    
    elif flag_pantalla_juego and not flag_pregunta_mostrada:
        nivel = str(contador_nivel)
        lista_posibles_preguntas = cargar_posibles_preguntas(lista_preguntas, categoria_elegida, nivel)
        pregunta_cargada = cargar_pregunta_aleatoriamente(lista_posibles_preguntas)
        pregunta = dividir_pregunta(pregunta_cargada["Pregunta"])
        lista_respuestas = crear_lista_respuestas(pregunta_cargada)
        respuesta_correcta = pregunta_cargada["Respuesta_correcta"]
        
        if len(pregunta) == 1:
            texto_pregunta_corte_1 = pregunta[0]
            texto_pregunta_corte_2 = ""
        else:
            texto_pregunta_corte_1 = pregunta[0]
            texto_pregunta_corte_2 = pregunta[1]
        
        respuesta_a = f"A: {lista_respuestas[0]}"
        respuesta_b = f"B: {lista_respuestas[1]}"
        respuesta_c = f"C: {lista_respuestas[2]}"
        respuesta_d = f"D: {lista_respuestas[3]}"

        lista_elementos_pantalla_jugando_inicial = []
        lista_imgs_jugando = [(fondo_menu, POS_INICIAL), (presentador, (650,250))]
        lista_textos_pantalla_jugando = [texto_pregunta_corte_1, texto_pregunta_corte_2, respuesta_a, respuesta_b, respuesta_c, respuesta_d, texto_cronometro]
        lista_pos_elementos_pantalla_jugando = [(25, 425), (25, 475), (25, 550), (450, 550), (25, 650), (450, 650), (25, 50)]
        lista_elementos_pantalla_jugando_inicial += lista_imgs_jugando

        lista_renders_jugando = listar_renders(lista_textos_pantalla_jugando, fuente_juego, BLANCO)
        lista_rects_jugando = listar_rects(lista_renders_jugando, lista_pos_elementos_pantalla_jugando)
        lista_fondos_jugando = listar_fondos(lista_rects_jugando, VIOLETA)

        lista_elementos_jugando_interactivos = generar_lista_elementos(lista_renders_jugando, lista_rects_jugando, lista_fondos_jugando)
        lista_elementos_pantalla_jugando = lista_elementos_pantalla_jugando_inicial + lista_elementos_jugando_interactivos

        flag_pregunta_mostrada = True
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_jugando)

    if flag_pantalla_juego and flag_respuesta_seleccionada:
        
        if flag_respuesta_correcta:
            contador_nivel += 1
            flag_pregunta_mostrada = False
            flag_respuesta_seleccionada = False
            contador_cronometro = 10
            texto_cronometro = str(contador_cronometro).zfill(2)
            pygame.time.set_timer(CRONOMETRO, 1000)
        elif not flag_respuesta_correcta:
            flag_pantalla_juego = False
            flag_pregunta_mostrada = False
            flag_respuesta_seleccionada = False
            flag_pantalla_principal = True
            contador_nivel = 1
            flag_cronometro_activo = False
    
    if flag_pantalla_juego:
        ventana_principal.fill(BLANCO)
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_jugando)
        dibujar_piramide_premios(ventana_principal, niveles_premios, ANCHO_VENTANA, BLANCO, VIOLETA)
        texto_cronometro_render = crear_texto_renderizado(texto_cronometro, fuente_cronometro, BLANCO)
        rect_texto_cronometro = crear_rect_texto(texto_cronometro_render, (25, 50))
        fondo_texto_cronometro = crear_fondo_texto(rect_texto_cronometro, VIOLETA)
        ventana_principal.blit(fondo_texto_cronometro, rect_texto_cronometro.topleft)
        ventana_principal.blit(texto_cronometro_render, rect_texto_cronometro.topleft)
        
    pygame.display.update()

pygame.quit()
