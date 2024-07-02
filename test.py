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
    
    flag_pregunta_mostrada = True
    cargar_pantalla(ventana_principal, lista_textos_pantalla_juego, lista_imgs_pantalla_juego, FUENTE_PANTALLA_JUEGO, BLANCO, VIOLETA, lista_elementos_interactivos_juego)
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
                
def resetear_juego(m, nivel, lista_elementos_interactivos, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo):
    m = 0
    nivel = str(niveles_premios[m][0])
    lista_elementos_interactivos.clear()
    flag_pantalla_juego = False
    flag_pantalla_principal = True
    flag_pregunta_mostrada = False
    flag_cronometro_activo = False
    return m, nivel, lista_elementos_interactivos, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo                     

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

# Variables de control
CRONOMETRO = pygame.USEREVENT 
pygame.time.set_timer(CRONOMETRO, 1000)
contador_cronometro = 5
texto_cronometro = str(contador_cronometro)

flag_run = True
flag_pantalla_principal = True
flag_pantalla_categorias = False
flag_pantalla_juego = False
flag_pregunta_mostrada = False
flag_cronometro_activo = True
flag_pantalla_game_over = False
m = 0
nivel = str(niveles_premios[m][0])

while flag_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if flag_pantalla_principal:
                for elemento in lista_elementos_interactivos_principal:
                    if elemento[1].collidepoint(mouse_pos):
                        if elemento[0] == "JUGAR":
                            flag_pantalla_principal = False
                            flag_pantalla_categorias = True
                        else:
                            flag_run = False
                        break
                    
            elif flag_pantalla_categorias:
                for elemento in lista_elementos_interactivos_categorias:
                    if elemento[1].collidepoint(mouse_pos):
                        categoria_elegida = elemento[0]
                        flag_pantalla_categorias = False
                        flag_pantalla_juego = True
                        break
                
            elif flag_pantalla_juego:
                respuesta_seleccionada = None
                for elemento in lista_elementos_interactivos_juego[:4]:
                    if elemento[1].collidepoint(mouse_pos):
                        respuesta_seleccionada = elemento[0]
                        break
        
                if respuesta_seleccionada != None:
                    if corroborar_respuesta(respuesta_seleccionada, respuesta_correcta):
                        flag_pregunta_mostrada = False
                        m += 1
                        nivel = str(niveles_premios[m][0])
                        contador_cronometro = 5
                        lista_elementos_interactivos_juego.clear()
                    else:
                        flag_pantalla_game_over = True
                        cargar_pantalla_game_over("Respuesta incorrecta", ventana_principal, lista_imgs_pantalla_game_over, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)
                     
                       
                if flag_pantalla_game_over:
                    for elemento in lista_elementos_interactivos_game_over:
                        if elemento[1].collidepoint(mouse_pos):
                            m, nivel, lista_elementos_interactivos_juego, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo = resetear_juego(m, nivel, lista_elementos_interactivos_juego, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo)


        elif event.type == CRONOMETRO and flag_cronometro_activo:
            contador_cronometro -= 1
            texto_cronometro = str(contador_cronometro).zfill(2)
            if contador_cronometro <= 0:
                flag_pantalla_game_over = True
                cargar_pantalla_game_over("Se acabó el tiempo", ventana_principal, lista_imgs_pantalla_game_over, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)
                
    if flag_pantalla_principal:
        cargar_pantalla(ventana_principal, lista_textos_pantalla_principal, lista_imgs_pantalla_principal, FUENTE_PRINCIPAL, BLANCO, VIOLETA, lista_elementos_interactivos_principal)
    elif flag_pantalla_categorias:
        cargar_pantalla(ventana_principal, lista_textos_pantalla_categorias, lista_imgs_pantalla_categorias, FUENTE_PRINCIPAL, BLANCO, VIOLETA, lista_elementos_interactivos_categorias)
    elif flag_pantalla_juego and not flag_pregunta_mostrada:
        flag_pregunta_mostrada, respuesta_correcta = cargar_pantalla_juego(lista_preguntas, categoria_elegida, nivel, flag_pregunta_mostrada)

    pygame.display.update()
        
pygame.quit()
    
                
                

                


