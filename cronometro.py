import pygame
from generales import *
from configuraciones import *
from elementos import *

pygame.init()
# Colores
VIOLETA = (67, 0, 103)
BLANCO = (255, 255, 255)
POS_INICIAL_FONDO = (0,0)
POS_INCIAL_PRESENTADOR = (650, 250)

def crear_fondo_texto(rect_texto, color_fondo):
    fondo_surface = pygame.Surface((rect_texto.width, rect_texto.height))
    fondo_surface.fill(color_fondo)
    return fondo_surface

def crear_texto_renderizado(texto, fuente, color):
    texto_renderizado = fuente.render(texto, True, color)
    return texto_renderizado

def blitear_imagenes(ventana_principal, lista_imagenes):
    exito = True
    try:
        for imagen in lista_imagenes:
            superficie = imagen[0]
            posicion = imagen[1]
            ventana_principal.blit(superficie,posicion)
    except:
        exito = False
    
    return exito
    
def blitear_objetos_interactivos(ventana_principal, lista_botones):
    exito = True
    try:
        for elemento in lista_botones:
            superficie = elemento["superficie"]
            fondo = elemento["fondo"]
            posicion = elemento["rectangulo"].topleft
            
            ventana_principal.blit(fondo, posicion)
            ventana_principal.blit(superficie, posicion)
            
    except:
        exito = False
    return exito

def crear_diccionario_botones(lista_botones, texto, surface, rect, posicion, fondo):
    try:
        elemento = {
            "texto": texto,
            "superficie": surface,
            "rectangulo": rect,
            "posicion": posicion,
            "fondo" : fondo
        }
        lista_botones.append(elemento)
    except:
        elemento = False
    
    return elemento
        
def crear_propiedades_botones(lista_textos, fuente, color_texto, color_fondo, lista_elementos_interactivos):
    lista_botones = []
    for elemento in lista_textos:
        texto = elemento[0]
        posicion = elemento[1]
        interactivo = elemento[2]
        surface = crear_texto_renderizado(texto, fuente, color_texto)
        rect = surface.get_rect()
        rect.topleft = posicion
        fondo = crear_fondo_texto(rect, color_fondo)
        if interactivo:
            lista_elementos_interactivos.append((texto,rect))

        crear_diccionario_botones(lista_botones,texto,surface,rect,posicion,fondo)
        
    return lista_botones
        
def cargar_pantalla(pantalla, lista_textos, lista_imgs, fuente, color_texto, color_fondo, lista_elementos_interactivos):
    lista_botones = crear_propiedades_botones(lista_textos, fuente, color_texto, color_fondo, lista_elementos_interactivos)
    blitear_imagenes(pantalla, lista_imgs)
    blitear_objetos_interactivos(pantalla, lista_botones)
    
def cargar_pantalla_juego(lista_preguntas, categoria_elegida, nivel, flag_pregunta_mostrada):
    lista_posibles_preguntas = cargar_posibles_preguntas(lista_preguntas, categoria_elegida, nivel)
    pregunta_cargada = cargar_pregunta_aleatoriamente(lista_posibles_preguntas)
    lista_respuestas = crear_lista_respuestas(pregunta_cargada)
    respuesta_correcta = pregunta_cargada["Respuesta_correcta"]
    
    lista_textos_pantalla_juego = [(pregunta_cargada["Pregunta"], (25, 425), False),
                                    (lista_respuestas[0], (25, 550), True),
                                    (lista_respuestas[1], (450, 550), True),
                                    (lista_respuestas[2], (25, 650), True),
                                    (lista_respuestas[3], (450, 650), True),
                                    (f"50-50", (150,55), True),
                                    (f"Publico", (275,55), True),
                                    (f"Llamada", (440,55), True)]
    # lista_textos_pantalla_juego = [(pregunta_cargada["Pregunta"], (25, 425), False),
    #                                 (lista_respuestas[0], (25, 550), True),
    #                                 (lista_respuestas[1], (450, 550), True),
    #                                 (lista_respuestas[2], (25, 650), True),
    #                                 (lista_respuestas[3], (450, 650), True),
    #                                 (f"50-50", (150,55), True),
    #                                 (f"Publico", (275,55), True),
    #                                 (f"Llamada", (440,55), True),
    #                                 (texto_cronometro, (25, 40), False)]



    flag_pregunta_mostrada = True
    cargar_pantalla(ventana_principal, lista_textos_pantalla_juego, lista_imgs_pantalla_juego, FUENTE_PANTALLA_JUEGO, BLANCO, VIOLETA, lista_elementos_interactivos_juego)
    dibujar_niveles_premios(ventana_principal, niveles_premios)
    return flag_pregunta_mostrada, respuesta_correcta

def corroborar_respuesta(respuesta_seleccionada, respuesta_correcta):
    if respuesta_seleccionada == respuesta_correcta:
        retorno = respuesta_seleccionada
    else:
        retorno = False
    
    return retorno 

def cargar_pantalla_game_over(texto, pantalla, lista_imgs_pantalla_game_over, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over):
    lista_textos_pantalla_game_over = [("Haz perdido!", (450, 300), False),
                                       ("Volver al menu principal", (270, 450), True),
                                       (texto, (320, 200), False)]
    cargar_pantalla(pantalla, lista_textos_pantalla_game_over, lista_imgs_pantalla_game_over, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)
                
def resetear_juego(M, nivel, lista_elementos_interactivos, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, flag_pantalla_game_over, flag_pantalla_categorias):
    M = 0  # Reiniciar el nivel a cero
    nivel = str(niveles_premios[M][0])  # Asegurar que el nivel sea el primero de la lista
    lista_elementos_interactivos.clear()  # Limpiar los elementos interactivos del juego
    flag_pantalla_principal = True  # Volver al menú principal
    flag_pantalla_categorias = False  # Asegurar que no se quede en la pantalla de categorías
    flag_pantalla_juego = False  # No mostrar la pantalla de juego al inicio
    flag_pregunta_mostrada = False  # No mostrar la pregunta al inicio
    flag_cronometro_activo = False  # No activar el cronómetro al inicio
    flag_pantalla_game_over = False  # No mostrar la pantalla de game over al inicio
    return M, nivel, lista_elementos_interactivos, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, flag_pantalla_game_over, flag_pantalla_categorias

def dibujar_niveles_premios(ventana_principal, piramide_niveles_premios):
    y = 15
    for i in range(len(piramide_niveles_premios)):
        nivel_premio = crear_texto_renderizado(piramide_niveles_premios[i][1], FUENTE_PIRAMIDE_PREMIOS,BLANCO)
        rect_nivel_premio = crear_rect_texto(nivel_premio, (1100, y))
        fondo_nivel_premio = crear_fondo_texto(rect_nivel_premio, VIOLETA)
        ventana_principal.blit(fondo_nivel_premio, (1100, y))
        ventana_principal.blit(nivel_premio, (1100, y))
        y += 45
        
# Configuración de la pantalla
ventana_principal = pygame.display.set_mode((DIMENSIONES_VENTANA))
pygame.display.set_caption("Quien quiere ser millonario?")

# Fuente
fuente = pygame.font.SysFont("sinsum", 75)

# Listas de botones y elementos interactivos
lista_elementos_interactivos_principal = []
lista_elementos_interactivos_categorias = []
lista_elementos_interactivos_juego = []
lista_elementos_interactivos_game_over = []

lista_textos_pantalla_principal = [("JUGAR", (380, 515), True), 
                                   ("SALIR", (750, 515), True)]

lista_textos_pantalla_categorias = [("Eliga una categoria", (450, 365), False),
                                    ("Historia", (250, 500), True),
                                    ("Deportes", (527, 500), True),
                                    ("Ciencia", (800, 500), True),
                                    ("Entretenimiento", (200, 600), True),
                                    ("Geografía", (750, 600), True)]

lista_imgs_pantalla_principal = [(fondo_menu, POS_INICIAL_FONDO),                    
                                 (logo, (450, 75))]

lista_imgs_pantalla_categorias = [(fondo_menu, POS_INICIAL_FONDO),                    
                                  (logo, (450, 0))]

lista_imgs_pantalla_juego = [(fondo_menu, POS_INICIAL_FONDO),                    
                             (presentador, POS_INCIAL_PRESENTADOR)]

lista_imgs_pantalla_game_over = [(fondo_menu, POS_INICIAL_FONDO)]

# Variables del juego
m = 0
nivel = str(niveles_premios[m][0])
respuesta_correcta = ""
flag_pregunta_mostrada = False
flag_respuesta_seleccionada = False
flag_pantalla_principal = True
flag_pantalla_categorias = False
flag_pantalla_juego = False
flag_pantalla_game_over = False
flag_cronometro_activo = False
respuesta_seleccionada = ""

# Cronómetro
texto_cronometro = ""
flag_cronometro_activo = False
rect_cronometro = pygame.Rect(25, 40, 60, 50)  # Ajusta este rectángulo según sea necesario
tiempo_inicial = 10
# Reloj
clock = pygame.time.Clock()
start_ticks = 0
# m = 0

# Bucle principal
running = True
# Bucle principal
running = True
while running:
    tiempo_transcurrido = pygame.time.get_ticks() - start_ticks
    segundos_restantes = tiempo_inicial - int(tiempo_transcurrido / 1000)
    # ventana_principal.fill(BLANCO)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if flag_pantalla_principal:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                for elemento in lista_elementos_interactivos_principal:
                    if elemento[1].collidepoint(pos_mouse):
                        texto_boton = elemento[0]
                        if texto_boton == "JUGAR":
                            flag_pantalla_principal = False
                            flag_pantalla_categorias = True
                        elif texto_boton == "SALIR":
                            running = False

        elif flag_pantalla_categorias:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                for elemento in lista_elementos_interactivos_categorias:
                    if elemento[1].collidepoint(pos_mouse):
                        categoria_elegida = elemento[0]
                        print(categoria_elegida)
                        break
            if categoria_elegida:
                flag_pantalla_categorias = False
                flag_pantalla_juego = True

        elif flag_pantalla_juego:
            if not flag_pregunta_mostrada:  # Solo carga la pantalla de juego si no se muestra una pregunta
                flag_pregunta_mostrada, respuesta_correcta = cargar_pantalla_juego(lista_preguntas, categoria_elegida, nivel, flag_pregunta_mostrada)
                flag_cronometro_activo = True
                start_ticks = pygame.time.get_ticks()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                for elemento in lista_elementos_interactivos_juego:
                    if elemento[1].collidepoint(pos_mouse):
                        respuesta_seleccionada = elemento[0]
                        flag_respuesta_seleccionada = True
                        flag_cronometro_activo = False

        if flag_pantalla_game_over:
            flag_pantalla_game_over = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                for elemento in lista_elementos_interactivos_game_over:
                    if elemento[1].collidepoint(pos_mouse):
                        texto_boton = elemento[0]
                        if texto_boton == "Volver al menu principal":
                            m, nivel, lista_elementos_interactivos_juego, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, flag_pantalla_game_over, flag_pantalla_categorias = resetear_juego(m, nivel, lista_elementos_interactivos_juego, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, flag_pantalla_game_over, flag_pantalla_categorias)
                            
            
    # Pantallas
    if flag_pantalla_principal:
        cargar_pantalla(ventana_principal, lista_textos_pantalla_principal, lista_imgs_pantalla_principal, FUENTE_PRINCIPAL, BLANCO, VIOLETA, lista_elementos_interactivos_principal)
    elif flag_pantalla_categorias:
        cargar_pantalla(ventana_principal, lista_textos_pantalla_categorias, lista_imgs_pantalla_categorias, FUENTE_PRINCIPAL, BLANCO, VIOLETA, lista_elementos_interactivos_categorias)
    elif flag_pantalla_juego:
        if flag_respuesta_seleccionada:
            if corroborar_respuesta(respuesta_seleccionada, respuesta_correcta):
                flag_respuesta_seleccionada = False
                m += 1
                if m >= len(niveles_premios):
                    texto_game_over = "¡Felicidades! Has ganado el juego."
                    flag_pantalla_game_over = True
                    cargar_pantalla_game_over(texto_game_over, ventana_principal, lista_imgs_pantalla_game_over, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)
                else:
                    nivel = str(niveles_premios[m][0])
                    flag_pregunta_mostrada = False
                    flag_cronometro_activo = True
                    start_ticks = pygame.time.get_ticks()
            else:
                texto_game_over = f"Respuesta incorrecta"
                flag_pantalla_game_over = True
                cargar_pantalla_game_over(texto_game_over, ventana_principal, lista_imgs_pantalla_game_over, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)

        if flag_cronometro_activo:
            
            pygame.draw.rect(ventana_principal, VIOLETA, rect_cronometro)
            texto_cronometro = str(segundos_restantes).zfill(2)
            cronometro_renderizado = fuente.render(texto_cronometro, True, BLANCO)
            ventana_principal.blit(cronometro_renderizado, (25, 40))
        if segundos_restantes <= 0:
            texto_game_over = f"¡Tiempo agotado! El juego ha terminado."
            flag_pantalla_game_over = True
            cargar_pantalla_game_over(texto_game_over, ventana_principal, lista_imgs_pantalla_game_over, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)
            flag_pantalla_juego = False
            flag_cronometro_activo = False
    
    pygame.display.update()

    
    clock.tick(60)

pygame.quit()

