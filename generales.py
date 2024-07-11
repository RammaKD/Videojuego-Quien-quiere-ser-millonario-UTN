import random
import pygame
from funciones_visuales import *
from colisiones import *
from elementos import *


blitear_flecha = lambda contador_nivel: ventana_principal.blit(flecha, (995, ALTO_VENTANA - 60 - (contador_nivel + 1) * 40))
#Funciones preguntas
def crear_lista_respuestas(pregunta):
    """
    Crea y retorna una lista de respuestas a partir de una cadena de respuestas separadas por "-".
    """
    lista_respuestas = pregunta["Respuestas"].split("-")
    return lista_respuestas

def crear_diccionario_preguntas(lista_datos, lista_preguntas):
    """
    Crea diccionarios de preguntas desde una lista de datos y los añade a una lista.

    Retorna la lista de preguntas actualizada.
    """
    for valores in lista_datos[1]:
        pregunta = {}
        for i in range(len(lista_datos[0])):
            if lista_datos[0][i] == "Nivel":
                pregunta[lista_datos[0][i]] = int(valores[i])
            else:
                pregunta[lista_datos[0][i]] = valores[i]

        lista_preguntas.append(pregunta)
    
    return lista_preguntas

def cargar_posibles_preguntas(lista_preguntas, categoria_elegida, contador_nivel):
    """
    Filtra y retorna una lista de preguntas posibles según la categoría y nivel especificados.
    """
    lista_preguntas_posibles = []
    for pregunta in lista_preguntas:
        if pregunta["Categoría"] == categoria_elegida and pregunta["Nivel"] == contador_nivel + 1:
           lista_preguntas_posibles.append(pregunta)

    return lista_preguntas_posibles

def cargar_pregunta_aleatoriamente(lista_preguntas):
    """
    Carga aleatoriamente una pregunta de una lista dada de preguntas.
    Retorna la pregunta seleccionada aleatoriamente.
    """
    indice_random = random.randint(0, len(lista_preguntas) - 1)
    pregunta_aleatoria = lista_preguntas[indice_random]
    return pregunta_aleatoria


#Funciones botones y comodines
def crear_propiedades_botones(dict_elementos):
    """
    Crea propiedades para botones usando texto renderizado o superficies.
    Añade botones interactivos a una lista dada.

    Retorna una lista de diccionarios con propiedades de botones.
    """
    lista_botones = []
    for clave,valor in dict_elementos.items():
        if clave != "interactivos" and clave != "fuente":
            for elemento in valor:
                if type(elemento[0]) == pygame.Surface: 
                    surface = elemento[0]
                    texto = str(surface)
                else:
                    texto = elemento[0]
                    surface = crear_texto_renderizado(texto, dict_elementos["fuente"][0], dict_elementos["fuente"][1], dict_elementos["fuente"][2])
                posicion = elemento[1]
                interactivo = elemento[2]
                rect = surface.get_rect()
                rect.topleft = posicion
                if interactivo:
                    
                    dict_elementos["interactivos"].append((texto, rect))
                crear_diccionario_botones(lista_botones, texto, surface, posicion, rect)

    return lista_botones

def crear_diccionario_botones(lista_botones, texto, surface, posicion, rect):
    """
    Crea y añade un diccionario con propiedades de botón a una lista.

    Retorna el diccionario creado con las propiedades del botón.
    """
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

def generar_porcentajes(lista_respuestas, respuesta_correcta):
    """
    Genera porcentajes aleatorios de popularidad para cada respuesta, asegurando que 
    la respuesta correcta tenga un porcentaje entre 50 y 100. Retorna una lista con 
    los porcentajes correspondientes a cada respuesta.
    """
    lista_porcentajes = [0] * len(lista_respuestas)
    porcentaje_correcta = random.randint(50, 100)
    porcentaje_restante = 100 - porcentaje_correcta
    
    indice_correcta = lista_respuestas.index(respuesta_correcta)
    lista_porcentajes[indice_correcta] = porcentaje_correcta
    
    respuestas_incorrectas = len(lista_respuestas) - 1
    total_asignado = 0
    for i in range(len(lista_respuestas)):
        if i != indice_correcta:
            if respuestas_incorrectas == 1:
                lista_porcentajes[i] = porcentaje_restante - total_asignado
            else:
                porcentaje = random.randint(0, porcentaje_restante - total_asignado)
                lista_porcentajes[i] = porcentaje
                total_asignado += porcentaje
            respuestas_incorrectas -= 1
    
    return lista_porcentajes

def aplicar_comodin_50_50(lista_textos_pantalla_juego, lista_respuestas, respuesta_correcta):
    """
    Aplica el comodín 50:50 eliminando dos respuestas incorrectas de la pantalla de juego.
    Retorna la lista actualizada de elementos de texto en pantalla.
    """
    
    lista_incorrectas = elegir_respuestas_incorrectas_random(lista_respuestas, respuesta_correcta)
    for i in range(1, 5):  
        for respuesta_incorrecta in lista_incorrectas:
            if lista_textos_pantalla_juego[i][0] == respuesta_incorrecta:
                lista_textos_pantalla_juego[i][0] = ""
                break
    
    return lista_textos_pantalla_juego

def elegir_respuestas_incorrectas_random(lista_respuestas, respuesta_correcta):
    """
    Selecciona aleatoriamente dos respuestas incorrectas de la lista de respuestas,
    asegurando que no sean la correcta ni duplicadas.
    
    Parámetros:
    lista_respuestas (list): Lista de todas las respuestas posibles.
    respuesta_correcta (str): La respuesta correcta que debe excluirse.
    
    Retorna:
    list: Lista con dos respuestas incorrectas seleccionadas aleatoriamente.
    """
    lista_incorrectas = []
    contador = 0
    while contador < 2:
        indice_random = random.randint(0, len(lista_respuestas) - 1)
        respuesta_elegida = lista_respuestas[indice_random]
        
        es_duplicada = False
        for incorrecta in lista_incorrectas:
            if incorrecta == respuesta_elegida:
                es_duplicada = True
                break
        
        if respuesta_elegida != respuesta_correcta and not es_duplicada:
            lista_incorrectas.append(respuesta_elegida)
            contador += 1

    return lista_incorrectas







