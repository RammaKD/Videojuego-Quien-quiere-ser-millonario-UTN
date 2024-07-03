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

def crear_texto_renderizado(texto, fuente, color, color_fondo):
    texto_renderizado = fuente.render(texto, True, color, color_fondo)
    return texto_renderizado

def blitear_elementos(ventana_principal, lista_botones):
    exito = True
    try:
        for elemento in lista_botones:
            superficie = elemento["superficie"]
            posicion = elemento["posicion"]
            ventana_principal.blit(superficie, posicion)
    except:
        exito = False
    return exito

def crear_diccionario_botones(lista_botones, texto, surface, posicion, rect):
    try:
        elemento = {
            "texto": texto,
            "superficie": surface,
            "rectangulo": rect,
            "posicion": posicion
        }
        lista_botones.append(elemento)
    except:
        elemento = False
    
    return elemento
        
def crear_propiedades_botones(lista_textos, fuente, color_texto, color_fondo, lista_elementos_interactivos):
    lista_botones = []
    for elemento in lista_textos:
        if type(elemento[0]) == pygame.Surface: 
            surface = elemento[0]
            texto = str(surface)
        else:
            texto = elemento[0]
            surface = crear_texto_renderizado(texto, fuente, color_texto, color_fondo)
        posicion = elemento[1]
        interactivo = elemento[2]
        rect = surface.get_rect()
        rect.topleft = posicion
        if interactivo:
            lista_elementos_interactivos.append((texto, rect))
        crear_diccionario_botones(lista_botones, texto, surface, posicion, rect)

    return lista_botones
        
def cargar_pantalla(ventana_principal, lista_elementos, fuente, color_texto, color_fondo, lista_elementos_interactivos):
    lista_botones = crear_propiedades_botones(lista_elementos, fuente, color_texto, color_fondo, lista_elementos_interactivos)
    blitear_elementos(ventana_principal, lista_botones)

def cargar_elementos_juego(lista_preguntas, categoria_elegida, nivel, flag_pregunta_mostrada, lista_imgs_pantalla_juego):
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
    lista_elementos_pantalla_juego = lista_imgs_pantalla_juego + lista_textos_pantalla_juego
    flag_pregunta_mostrada = True
    cargar_pantalla(ventana_principal, lista_elementos_pantalla_juego, FUENTE_PANTALLA_JUEGO, BLANCO, VIOLETA, lista_elementos_interactivos_juego)
    
    return flag_pregunta_mostrada, respuesta_correcta, lista_textos_pantalla_juego

def corroborar_respuesta(respuesta_seleccionada, respuesta_correcta):
    if respuesta_seleccionada == respuesta_correcta:
        retorno = respuesta_seleccionada
    else:
        retorno = False
    
    return retorno 

def resetear_juego(m, nivel, lista_elementos_interactivos, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, flag_pantalla_game_over, flag_boton_pantalla_game_over, flag_botones_respuestas,  flag_pantalla_checkpoint, flag_botones_pantalla_checkpoint):
    m = 0
    nivel = str(niveles_premios[m][0])
    lista_elementos_interactivos.clear()
    flag_pantalla_juego = False
    flag_pantalla_principal = True
    flag_pregunta_mostrada = False
    flag_cronometro_activo = False
    flag_pantalla_game_over = False
    flag_boton_pantalla_game_over = False
    flag_botones_respuestas = True
    flag_pantalla_checkpoint = False
    flag_botones_pantalla_checkpoint = False
    return m, nivel, lista_elementos_interactivos, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, flag_pantalla_game_over, flag_boton_pantalla_game_over, flag_botones_respuestas, flag_pantalla_checkpoint, flag_botones_pantalla_checkpoint                     

def dibujar_niveles_premios(ventana_principal, piramide_niveles_premios):
    y = 25
    for i in range(len(piramide_niveles_premios) -1, -1, -1):
        nivel_premio = crear_texto_renderizado(piramide_niveles_premios[i][1], FUENTE_PIRAMIDE_PREMIOS, BLANCO, VIOLETA)
        ventana_principal.blit(nivel_premio, (1100, y))
        y += 40
        
def actualizar_cronometro(ventana_principal, contador_cronometro, texto_cronometro, fuente, color_texto, color_fondo):
    texto_cronometro = str(contador_cronometro).zfill(2)
    superficie_cronometro = crear_texto_renderizado(texto_cronometro, fuente, color_texto, color_fondo)
    ventana_principal.blit(superficie_cronometro, (25, 40)) 
      
# Configuración de la pantalla
ventana_principal = pygame.display.set_mode(DIMENSIONES_VENTANA)
pygame.display.set_caption("Quien quiere ser millonario?")

# Listas de botones y elementos interactivos
lista_elementos_interactivos_principal = []
lista_elementos_interactivos_categorias = []
lista_elementos_interactivos_juego = []
lista_elementos_interactivos_game_over = []
lista_elementos_interactivos_checkpoint = []
lista_elementos_interactivos_score = []

lista_textos_pantalla_principal = [("JUGAR", (380, 515), True), 
                                   ("SALIR", (750, 515), True)]

lista_textos_pantalla_categorias = [("Eliga una categoria", (450, 365), False),
                                    ("Historia", (275, 500), True),
                                    ("Deportes", (515, 500), True),
                                    ("Ciencia", (800, 500), True),
                                    ("Entretenimiento", (275, 600), True),
                                    ("Geografía", (715, 600), True)]

lista_textos_pantalla_checkpoint = [("Quiere seguir jugando?", (450, 300), False),
                                    ("Seguir jugando", (100, 450), True),
                                    ("Retirarse", (400, 450), True)]

lista_textos_pantalla_game_over_incorrecta = [("Has perdido!", (450, 300), False),
                                              ("Volver al menu principal", (270, 450), True)]

lista_textos_pantalla_game_over_tiempo_finalizado = [("Has perdido!", (450, 300), False),
                                                     ("Volver al menu principal", (270, 450), True)]

lista_textos_pantalla_score = [("Introduzca su nombre", (300, 300), False)]

lista_imgs_pantalla_principal = [(fondo_menu, POS_INICIAL_FONDO, False),                    
                                 (logo, (450, 75), False)]

lista_imgs_pantalla_categorias = [(fondo_menu, POS_INICIAL_FONDO, False),                    
                                  (logo, (450, 0), False)]

lista_imgs_pantalla_juego = [(fondo_menu, POS_INICIAL_FONDO, False),                    
                             (presentador, POS_INCIAL_PRESENTADOR, False)]

lista_imgs_pantalla_game_over = [(fondo_menu, POS_INICIAL_FONDO, False)]

lista_elementos_pantalla_principal = lista_imgs_pantalla_principal + lista_textos_pantalla_principal
lista_elementos_pantalla_categorias = lista_imgs_pantalla_categorias + lista_textos_pantalla_categorias

# Variables de control
CRONOMETRO = pygame.USEREVENT + 1
pygame.time.set_timer(CRONOMETRO, 1000)
contador_cronometro = 10
texto_cronometro = str(contador_cronometro)

texto_input_box = ""
flag_run = True
flag_pantalla_principal = True
flag_pantalla_categorias = False
flag_pantalla_juego = False
flag_pregunta_mostrada = False
flag_cronometro_activo = False
flag_pantalla_game_over = False
flag_pantalla_checkpoint = False
flag_boton_pantalla_game_over = False
flag_botones_pantalla_checkpoint = False
flag_botones_respuestas = True
flag_pantalla_guardar_score = False
flag_botones_pantalla_guardar_score = False
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
                        flag_cronometro_activo = True
                        break
                
            elif flag_pantalla_juego and flag_botones_respuestas:
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
                        contador_cronometro = 10
                        lista_elementos_interactivos_juego.clear()
                        if nivel == "3" or nivel == "11":
                            flag_pantalla_juego = False
                            flag_cronometro_activo = False
                            flag_botones_respuestas = False
                            flag_pantalla_checkpoint = True
                            flag_botones_pantalla_checkpoint = True
                            dinero_a_retirar = niveles_premios[m - 1][1]
                            mensaje_dinero_a_retirar = (f"O retirarse con: {dinero_a_retirar}", (450, 350), False)
                            lista_textos_pantalla_checkpoint.append(mensaje_dinero_a_retirar)
                            lista_elementos_pantalla_checkpoint = lista_imgs_pantalla_game_over + lista_textos_pantalla_checkpoint
                            cargar_pantalla(ventana_principal, lista_elementos_pantalla_checkpoint, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_checkpoint)
                    else:
                        contador_cronometro = 10
                        flag_cronometro_activo = False
                        flag_pantalla_game_over = True
                        flag_boton_pantalla_game_over = True
                        flag_botones_respuestas = False
                        mensaje_error = "Respuesta incorrecta"
                        lista_textos_pantalla_game_over_incorrecta.append((mensaje_error, (320, 200), False))
                        lista_elementos_pantalla_game_over_incorrecta = lista_imgs_pantalla_game_over + lista_textos_pantalla_game_over_incorrecta
                        cargar_pantalla(ventana_principal, lista_elementos_pantalla_game_over_incorrecta, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)
            
            
            elif flag_pantalla_game_over and flag_boton_pantalla_game_over:
                for elemento in lista_elementos_interactivos_game_over:
                    if elemento[1].collidepoint(mouse_pos):
                        m, nivel, lista_elementos_interactivos_juego, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, flag_pantalla_game_over, flag_boton_pantalla_game_over, flag_botones_respuestas, flag_pantalla_checkpoint, flag_botones_pantalla_checkpoint = resetear_juego(m, nivel, lista_elementos_interactivos_juego, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, flag_pantalla_game_over, flag_boton_pantalla_game_over, flag_botones_respuestas, flag_pantalla_checkpoint, flag_botones_pantalla_checkpoint)
            
            elif flag_pantalla_checkpoint and flag_botones_pantalla_checkpoint:
                for elemento in lista_elementos_interactivos_checkpoint:
                    if elemento[1].collidepoint(mouse_pos):
                        if elemento[0] == "Retirarse":
                            flag_pantalla_guardar_score = True
                            flag_pregunta_mostrada = False
                        else:
                            flag_pantalla_juego = True
                            flag_botones_respuestas = True
                            flag_cronometro_activo = True
                            flag_pregunta_mostrada = False
                            flag_botones_pantalla_checkpoint = False
            
            
        elif event.type == pygame.KEYDOWN:
            if flag_pantalla_guardar_score and flag_botones_pantalla_guardar_score:
                if event.key == pygame.K_BACKSPACE:
                    texto_input_box = texto_input_box[:-1]
                elif event.key == pygame.K_ESCAPE:
                    texto_input_box = ""
                else:
                    texto_temp = texto_input_box + event.unicode
                    texto_surface_temp = FUENTE_PANTALLA_GAME_OVER.render(texto_temp, True, BLANCO)
                    rect_temp = texto_surface_temp.get_rect()
                    if rect_temp.width <= input_box_premio.width:
                        texto_input_box += event.unicode

                    
                    

    


        #m, nivel, lista_elementos_interactivos_juego, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, flag_pantalla_game_over, flag_boton_pantalla_game_over, flag_botones_respuestas, flag_pantalla_checkpoint, flag_botones_pantalla_checkpoint = resetear_juego(m, nivel, lista_elementos_interactivos_juego, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, flag_pantalla_game_over, flag_boton_pantalla_game_over, flag_botones_respuestas, flag_pantalla_checkpoint, flag_botones_pantalla_checkpoint)
        
        
        elif event.type == CRONOMETRO and flag_cronometro_activo:
            actualizar_cronometro(ventana_principal, contador_cronometro, texto_cronometro, FUENTE_CRONOMETRO, BLANCO, VIOLETA)
            dibujar_niveles_premios(ventana_principal, niveles_premios)
            contador_cronometro -= 1
            if contador_cronometro < 0:
                contador_cronometro = 10
                flag_cronometro_activo = False
                flag_pantalla_game_over = True
                flag_boton_pantalla_game_over = True
                flag_botones_respuestas = False
                mensaje_error = "Se le acabó el tiempo"
                lista_textos_pantalla_game_over_tiempo_finalizado.append((mensaje_error, (320, 200), False))
                lista_elementos_pantalla_game_over_tiempo_finalizado = lista_imgs_pantalla_game_over + lista_textos_pantalla_game_over_tiempo_finalizado
                cargar_pantalla(ventana_principal, lista_elementos_pantalla_game_over_tiempo_finalizado, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)
    
    if flag_pantalla_principal:
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_principal, FUENTE_PRINCIPAL, BLANCO, VIOLETA, lista_elementos_interactivos_principal)
    elif flag_pantalla_categorias:
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_categorias, FUENTE_PRINCIPAL, BLANCO, VIOLETA, lista_elementos_interactivos_categorias)
    elif flag_pantalla_juego and not flag_pregunta_mostrada:
        flag_pregunta_mostrada, respuesta_correcta, lista_textos_pantalla_juego = cargar_elementos_juego(lista_preguntas, categoria_elegida, nivel, flag_pregunta_mostrada, lista_imgs_pantalla_juego)
        actualizar_cronometro(ventana_principal, contador_cronometro, texto_cronometro, FUENTE_CRONOMETRO, BLANCO, VIOLETA)
        dibujar_niveles_premios(ventana_principal, niveles_premios)
    elif flag_pantalla_guardar_score:
        flag_botones_respuestas = False
        flag_boton_pantalla_game_over = False
        flag_botones_pantalla_checkpoint = False
        flag_botones_pantalla_guardar_score = True
        lista_elementos_pantalla_score = lista_imgs_pantalla_game_over + lista_textos_pantalla_score
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_score, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_score)
        input_box_premio = pygame.Rect(250, 450, 750, 65)
        texto_surface = crear_texto_renderizado(texto_input_box, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA)
        ventana_principal.blit(texto_surface, (input_box_premio.x, input_box_premio.y))
        pygame.draw.rect(ventana_principal, BLANCO, input_box_premio, 2)
    
    pygame.display.update()
        
pygame.quit()
           
               










