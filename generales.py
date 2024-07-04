import random
import pygame
from funciones_visuales import *

def crear_lista_respuestas(pregunta):
    lista_respuestas = pregunta["Respuestas"].split("-")
    return lista_respuestas

def crear_diccionario_preguntas(lista_datos, lista_preguntas):
    for valores in lista_datos[1]:
        pregunta = {}
        for i in range(len(lista_datos[0])):
            pregunta[lista_datos[0][i]] = valores[i]
        lista_preguntas.append(pregunta)
    
    return lista_preguntas

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

def cargar_posibles_preguntas(lista_preguntas, categoria_elegida, nivel):
    lista_preguntas_posibles = []
    for pregunta in lista_preguntas:
        if pregunta["Categoría"] == categoria_elegida and pregunta["Nivel"] == nivel:
           lista_preguntas_posibles.append(pregunta)

    return lista_preguntas_posibles

def cargar_pregunta_aleatoriamente(lista_preguntas):
    indice_random = random.randint(0, len(lista_preguntas) - 1)
    pregunta_aleatoria = lista_preguntas[indice_random]
    return pregunta_aleatoria

def cargar_pantalla(ventana_principal, lista_elementos, fuente, color_texto, color_fondo, lista_elementos_interactivos):
    lista_botones = crear_propiedades_botones(lista_elementos, fuente, color_texto, color_fondo, lista_elementos_interactivos)
    blitear_elementos(ventana_principal, lista_botones)

def generar_porcentajes(lista_respuestas, respuesta_correcta):
    respuestas_incorrectas = []
    porcentaje_correcta = 0
    
    for respuesta in lista_respuestas:
        if respuesta == respuesta_correcta:
            porcentaje_correcta = random.randint(50, 100)
        else:
            respuestas_incorrectas.append(respuesta)
    
    porcentaje_restante = 100 - porcentaje_correcta
    porcentajes = {respuesta_correcta: porcentaje_correcta}
    total_asignado = 0
    for i in range(len(respuestas_incorrectas)):
        if i == len(respuestas_incorrectas) - 1:
            porcentajes[respuestas_incorrectas[i]] = porcentaje_restante - total_asignado
        else:
            porcentaje = random.randint(0, porcentaje_restante - total_asignado)
            porcentajes[respuestas_incorrectas[i]] = porcentaje
            total_asignado += porcentaje
    
    lista_porcentajes = []
    for respuesta in lista_respuestas:
        lista_porcentajes.append(porcentajes[respuesta])
    
    return lista_porcentajes

def aplicar_comodin_50_50(lista_textos_pantalla_juego, lista_respuestas, respuesta_correcta):
    lista_incorrectas = elegir_respuestas_incorrectas_random(lista_respuestas, respuesta_correcta)
    for i in range(1, 5):  
        for respuesta_incorrecta in lista_incorrectas:
            if lista_textos_pantalla_juego[i][0] == respuesta_incorrecta:
                lista_textos_pantalla_juego[i][0] = ""
                break
    
    return lista_textos_pantalla_juego

def elegir_respuestas_incorrectas_random(lista_respuestas, respuesta_correcta):
    lista_incorrectas = []
    contador = 0
    while contador < 2:
        indice_random = random.randint(0, len(lista_respuestas) - 1)
        respuesta_elegida = lista_respuestas[indice_random]
        
        es_correcta = respuesta_elegida == respuesta_correcta
        es_duplicada = False
        for incorrecta in lista_incorrectas:
            if incorrecta == respuesta_elegida:
                es_duplicada = True
                break
        
        if not es_correcta and not es_duplicada:
            lista_incorrectas.append(respuesta_elegida)
            contador += 1

    return lista_incorrectas

def corroborar_respuesta(respuesta_seleccionada, respuesta_correcta):
    if respuesta_seleccionada == respuesta_correcta:
        retorno = respuesta_seleccionada
    else:
        retorno = False
    
    return retorno

def cargar_elementos_juego(ventana, lista_preguntas, categoria_elegida, nivel, lista_imgs_pantalla_juego, lista_elementos_interactivos_juego):
    lista_posibles_preguntas = cargar_posibles_preguntas(lista_preguntas, categoria_elegida, nivel)
    pregunta_cargada = cargar_pregunta_aleatoriamente(lista_posibles_preguntas)
    lista_respuestas = crear_lista_respuestas(pregunta_cargada)
    respuesta_correcta = pregunta_cargada["Respuesta_correcta"]
    pista = pregunta_cargada["Pista"]
    
    lista_posiciones_respuestas = [(25, 550), (450, 550), (25, 650), (450, 650)]
    lista_textos_pantalla_juego = [(pregunta_cargada["Pregunta"], (25, 425), False),
                                   [lista_respuestas[0], lista_posiciones_respuestas[0], True],
                                   [lista_respuestas[1], lista_posiciones_respuestas[1], True],
                                   [lista_respuestas[2], lista_posiciones_respuestas[2], True],
                                   [lista_respuestas[3], lista_posiciones_respuestas[3], True],
                                   ("50-50", (150,55), True),
                                   ("Publico", (275,55), True),
                                   ("Llamada", (440,55), True)]
    
    lista_elementos_pantalla_juego = lista_imgs_pantalla_juego + lista_textos_pantalla_juego
    cargar_pantalla(ventana, lista_elementos_pantalla_juego, FUENTE_PANTALLA_JUEGO, BLANCO, VIOLETA, lista_elementos_interactivos_juego)
    
    return respuesta_correcta, pista, lista_textos_pantalla_juego, lista_respuestas, lista_posiciones_respuestas

def resetear_juego(flags_variables,m, nivel,niveles_premios,lista_elementos_interactivos):
    m = 0
    nivel = str(niveles_premios[m][0])
    lista_elementos_interactivos.clear()
    flags_variables["flag_pantalla_juego"] = False
    flags_variables["flag_pantalla_principal"] = True
    flags_variables["flag_pregunta_mostrada"] = False
    flags_variables["flag_cronometro_activo"] = False
    flags_variables["flag_pantalla_game_over"] = False
    flags_variables["flag_boton_pantalla_game_over"] = False
    flags_variables["flag_botones_respuestas"] = True
    flags_variables["flag_pantalla_checkpoint"] = False
    flags_variables["flag_botones_pantalla_checkpoint"] = False
    flags_variables["flag_comodin_pista"] = True
    flags_variables["flag_comodin_publico"] = True
    flags_variables["flag_pantalla_guardar_score"] = False
    flags_variables["flag_botones_pantalla_guardar_score"] = False
    
    return flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos





















