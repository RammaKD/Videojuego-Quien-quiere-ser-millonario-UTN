import random
import pygame
from funciones_visuales import *

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
        if pregunta["Categoría"] == categoria_elegida and pregunta["Nivel"] == contador_nivel+1 :
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

def cargar_pantalla(ventana_principal, dict_elementos):
    """
    Carga y muestra elementos interactivos en una ventana principal, usando una fuente y colores específicos.
    """
    lista_botones = crear_propiedades_botones(dict_elementos)
    blitear_elementos(ventana_principal, lista_botones)

    return lista_botones

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

def aplicar_comodin_50_50(lista_textos_pantalla_juego,  lista_respuestas, respuesta_correcta):
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

def cargar_elementos_juego(lista_preguntas, categoria_elegida, contador_nivel):
    """
    Carga y muestra los elementos del juego en la pantalla. Filtra las preguntas según 
    la categoría y nivel, selecciona una pregunta aleatoria y prepara las respuestas 
    y pistas para mostrar. Combina las imágenes y textos para la pantalla de juego y 
    los carga en la ventana.

    Retorna la respuesta correcta, pista, lista de textos en pantalla, lista de respuestas y 
    sus posiciones.
    """
    dict_pregunta_tocada = {}
    lista_posibles_preguntas = cargar_posibles_preguntas(lista_preguntas, categoria_elegida, contador_nivel)
    pregunta_cargada = cargar_pregunta_aleatoriamente(lista_posibles_preguntas)
    dict_pregunta_tocada["pregunta"] = pregunta_cargada["Pregunta"]
    dict_pregunta_tocada["respuestas"] = crear_lista_respuestas(pregunta_cargada)
    dict_pregunta_tocada["respuesta_correcta"] = pregunta_cargada["Respuesta_correcta"]
    dict_pregunta_tocada["pista"] = pregunta_cargada["Pista"]

    return dict_pregunta_tocada

def modificar_dict_pantalla_juego(dict_elementos, dict_pregunta):
    dict_elementos["textos"][0][0] = dict_pregunta["pregunta"]
    dict_elementos["textos"][1][0] = dict_pregunta["respuestas"][0]
    dict_elementos["textos"][2][0] = dict_pregunta["respuestas"][1]
    dict_elementos["textos"][3][0] = dict_pregunta["respuestas"][2]
    dict_elementos["textos"][4][0] = dict_pregunta["respuestas"][3]

    return dict_elementos
   
def resetear_juego(flags_variables, dict_elementos, contador_nivel):
    """
    Restaura el estado inicial del juego, reseteando el contador, nivel, 
    lista de elementos interactivos y todas las banderas del juego a sus 
    valores iniciales.
    """
    contador_nivel = 0
    
    dict_elementos["interactivos"].clear()
    flags_variables["pantalla_juego"] = False
    flags_variables["pantalla_principal"] = True
    flags_variables["pregunta_mostrada"] = False
    flags_variables["cronometro_activo"] = False
    flags_variables["pantalla_game_over"] = False
    flags_variables["boton_pantalla_game_over"] = False
    flags_variables["botones_respuestas"] = True
    flags_variables["pantalla_checkpoint"] = False
    flags_variables["botones_pantalla_checkpoint"] = False
    flags_variables["comodin_pista"] = True
    flags_variables["comodin_publico"] = True
    flags_variables["pantalla_guardar_score"] = False
    flags_variables["botones_pantalla_guardar_score"] = False
    flags_variables["comodin_50_50"] = True

    return contador_nivel

def desactivar_pantalla_juego(flags_variables):
    flags_variables["pantalla_juego"] = False
    flags_variables["cronometro_activo"] = False
    flags_variables["botones_respuestas"] = False
    flags_variables["comodin_pista"] = False
    flags_variables["comodin_publico"] = False
    flags_variables["comodin_50_50"] = False

    return flags_variables
    
def habilitar_game_over(flags_variables, dict_general_pantallas_secundarias, msj_error):
    flags_variables["pantalla_game_over"] = True
    flags_variables["boton_pantalla_game_over"] = True
    desactivar_pantalla_juego(flags_variables)
    dict_general_pantallas_secundarias["game_over"]["textos"][2][0] = msj_error
    
    return dict_general_pantallas_secundarias
    
def colision_lado_derecho(rect1, rect2):
    # Verificar si el borde derecho de rect2 colisiona con el borde derecho de rect1
    return rect2.right >= rect1.right and rect1.top < rect2.bottom and rect1.bottom > rect2.top















