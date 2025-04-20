import pygame
from funciones_visuales import *
from generales import *
from funciones_archivos import *
from elementos import *
from colisiones import *
from especificas import *


def manejar_evento_quit(evento, flags_variables):
    """Si el evento es pygame.QUIT, establece flags_variables["run"] a False.
    """
    if evento.type == pygame.QUIT:
        flags_variables["run"] = False

def manejar_eventos(estado_juego, elementos_pantalla):
    """
    Maneja los eventos de Pygame en el juego.

    Este método maneja eventos como la salida del juego, clics de mouse para interacción,
    eventos de teclado para entrada de usuario y la gestión de eventos de cronómetro si está activo.
    """
    for event in pygame.event.get():
        manejar_evento_quit(event, estado_juego["flags_variables"])
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            manejar_evento_mouse(estado_juego, mouse_pos, elementos_pantalla)
            
        elif event.type == pygame.KEYDOWN:
            manejar_evento_teclado(event, estado_juego, elementos_pantalla, diccionario_paths)
        elif event.type == CRONOMETRO and estado_juego["flags_variables"]["cronometro_activo"]:
            manejar_evento_cronometro(estado_juego, elementos_pantalla)

def manejar_evento_mouse(estado_juego, mouse_pos, elementos_pantalla):
    """
    Maneja eventos de clic del mouse según el estado actual del juego y los elementos de pantalla.

    Esta función itera a través de un diccionario de eventos, donde cada clave representa un estado del juego
    y su valor es una función correspondiente para manejar eventos de clic del mouse en ese estado específico.
    """
    eventos = {
        "pantalla_principal": manejar_evento_pantalla_principal,
        "pantalla_categorias": manejar_evento_pantalla_categorias,
        "pantalla_juego": manejar_evento_pantalla_juego,
        "pantalla_game_over": manejar_evento_pantalla_game_over,
        "pantalla_checkpoint": manejar_evento_pantalla_checkpoint,
        "pantalla_victoria": manejar_evento_pantalla_victoria,
    }
    
    for estado in eventos:
        if estado_juego["flags_variables"][estado]:
            eventos[estado](estado_juego, mouse_pos, elementos_pantalla)
            
def manejar_evento_teclado(event, estado_juego, elementos_pantalla, diccionario_paths):
    """
    Maneja eventos de teclado según el estado actual del juego y elementos visuales.

    Esta funcion gestiona la interacción del teclado, como mostrar puntajes y guardar resultados,
    ajustando el estado del juego según las acciones realizadas.
    """
    flags_variables = estado_juego["flags_variables"]
    manejar_evento_mostrar_score(event, flags_variables, diccionario_paths, elementos_pantalla)
    if flags_variables["pantalla_guardar_score"] and flags_variables["botones_pantalla_guardar_score"]:
        if manejar_evento_guardar_score(event, estado_juego, elementos_pantalla):
            estado_juego["contador_nivel"] = resetear_juego(estado_juego, elementos_pantalla)

def manejar_evento_cronometro(estado_juego, elementos_pantalla):
    """
    Maneja eventos relacionados con el cronómetro del juego.

    Esta funcion actualiza el cronómetro en la pantalla principal y, si el tiempo se agota,
    activa la pantalla de game over con un mensaje de error.
    """
    actualizado = actualizar_cronometro(ventana_principal, estado_juego["dict_cronometro"])
    if not actualizado:
        msj_error = "Se le acabó el tiempo"
        elementos_pantalla["dict_general_pantallas_secundarias"] = habilitar_game_over(flags_variables, elementos_pantalla, msj_error)
        cargar_pantalla(ventana_principal, estado_juego["dict_general_pantallas_secundarias"]["game_over"])

def manejar_evento_guardar_score(event, estado_juego, elementos_pantalla):
    """
    Maneja eventos relacionados con la introducción y guardado de puntajes.

    Esta funcion permite al jugador ingresar su nombre para guardar su puntuación.
    Se controlan teclas específicas como retroceso para eliminar caracteres y enter
    para confirmar y guardar el puntaje en caso de que se cumplan ciertas condiciones.

    """
    dict_score = elementos_pantalla["dict_general_pantallas_secundarias"]["score"]
    dict_niveles_premios = estado_juego["dict_niveles_premios"]
    contador_nivel = estado_juego["contador_nivel"]
    retorno = False
    max_caracteres = 15
    
    if event.key == pygame.K_BACKSPACE:
        dict_score["textos"][1][0] = dict_score["textos"][1][0][:-1]
    elif event.key == pygame.K_ESCAPE:
        dict_score["textos"][1][0] = ""
    else:
        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
            if len(dict_general_pantallas_secundarias["score"]["textos"][1][0]) > 0:
                nombre = dict_general_pantallas_secundarias["score"]["textos"][1][0]
                if contador_nivel == 15:
                    contador_nivel -= 1
                score = dict_niveles_premios["piramide"][contador_nivel][1]
                nueva_puntuacion = f"{nombre}: {score}"
                actualizar_billetera_json(diccionario_paths["path_billetera"], nueva_puntuacion)
                dict_general_pantallas_secundarias["score"]["textos"][1][0] = ""
                retorno = True
        else:    
            if len(dict_score["textos"][1][0]) < max_caracteres:
                dict_score["textos"][1][0] += event.unicode
            
    return retorno

def manejar_evento_mostrar_score(event, flags_variables, diccionario_paths, elementos_pantalla):
    """
    Maneja eventos relacionados con la visualización de puntajes en la pantalla principal.

    Esta funcion carga y muestra los puntajes guardados al presionar la tecla TAB. Permite 
    alternar entre la visualización de puntajes y la pantalla principal según el estado actual.

    """
    dict_elementos_pantalla_principal = elementos_pantalla["dict_elementos_pantalla_principal"]
    
    if event.key == pygame.K_TAB:
        if not flags_variables["scores_mostrados"]:
            scores = cargar_billetera_json(diccionario_paths["path_billetera"])
            puntajes = scores["billetera"]
            if len(puntajes) > 0:
                y = 50
                for puntaje in puntajes:
                    texto_score = puntaje
                    posicion = (25, y)
                    interactivo = False
                    elemento_comp = (texto_score, posicion, interactivo)
                    dict_elementos_pantalla_principal["textos"].append(elemento_comp)
                    y += 50
            flags_variables["scores_mostrados"] = True
        else:
            flags_variables["flag_pantalla_principal"] = True
            flags_variables["scores_mostrados"] = False
            dict_elementos_pantalla_principal["textos"] = [
                ("JUGAR", (380, 515), True), 
                ("SALIR", (750, 515), True),
                ("Pantalla puntajes[tab]", (370, 600), False)
            ]
    
    return flags_variables


def manejar_evento_pantalla_principal(estado_juego, mouse_pos, elementos_pantalla):
    """
    Maneja la selección de botones en la pantalla principal y actualiza el estado del juego.
    
    Parámetros:
    - estado_juego: Diccionario con el estado actual del juego.
    - mouse_pos: Tupla con la posición actual del ratón.
    - elementos_pantalla: Diccionario con los elementos de la pantalla principal.
    """
    dict_elementos_pantalla_principal = elementos_pantalla["dict_elementos_pantalla_principal"]
    boton_seleccionado = manejar_colision_pantalla_principal(mouse_pos, dict_elementos_pantalla_principal)
    if boton_seleccionado != None:
        manejar_boton_pantalla_principal(boton_seleccionado, estado_juego["flags_variables"])

def manejar_evento_pantalla_categorias(estado_juego, mouse_pos, elementos_pantalla):
    """
    Maneja la selección de categorías y habilita la pantalla del juego si se elige una categoría.
    
    Parámetros:
    - estado_juego: Diccionario con el estado actual del juego.
    - mouse_pos: Tupla con la posición actual del ratón.
    - elementos_pantalla: Diccionario con los elementos de la pantalla de categorías.
    """
  
    
    dict_elementos_pantalla_categorias = elementos_pantalla["dict_elementos_pantalla_categorias"]
    estado_juego["categoria_elegida"] = manejar_colision_pantalla_categorias(mouse_pos, dict_elementos_pantalla_categorias)
    if estado_juego["categoria_elegida"] != None:
        habilitar_pantalla_juego(estado_juego["flags_variables"])                    

def manejar_evento_pantalla_juego(estado_juego, mouse_pos, elementos_pantalla):
    """
    Administra los eventos en la pantalla del juego si los botones de respuesta están habilitados.
    
    Parámetros:
    - estado_juego: Diccionario con el estado actual del juego.
    - mouse_pos: Tupla con la posición actual del ratón.
    - elementos_pantalla: Diccionario con los elementos de la pantalla del juego.
    """
    if estado_juego["flags_variables"]["botones_respuestas"]:
        
        estado_juego = administrar_pantalla_juego(mouse_pos, estado_juego, elementos_pantalla, ventana_principal, flags_variables)

def manejar_evento_pantalla_game_over(estado_juego, mouse_pos, elementos_pantalla):
    """
    Resetea el juego y el contador de nivel si se presiona el botón de 'game over'.
    
    Parámetros:
    - estado_juego: Diccionario con el estado actual del juego.
    - mouse_pos: Tupla con la posición actual del ratón.
    - elementos_pantalla: Diccionario con los elementos de la pantalla de 'game over'.
    """
    dict_general_pantallas_secundarias = elementos_pantalla["dict_general_pantallas_secundarias"]
    if estado_juego["flags_variables"]["boton_pantalla_game_over"]:
        if manejar_colision_pantalla_game_over(mouse_pos, dict_general_pantallas_secundarias):
            estado_juego["contador_nivel"] = resetear_juego(estado_juego, elementos_pantalla)
            
        
def manejar_evento_pantalla_checkpoint(estado_juego, mouse_pos, elementos_pantalla):
    """
    Maneja la selección de botones en la pantalla de checkpoint y actualiza el estado del juego.
    
    Parámetros:
    - estado_juego: Diccionario con el estado actual del juego.
    - mouse_pos: Tupla con la posición actual del ratón.
    - elementos_pantalla: Diccionario con los elementos de la pantalla de checkpoint.
    """
    dict_general_pantallas_secundarias = elementos_pantalla["dict_general_pantallas_secundarias"]
    if estado_juego["flags_variables"]["botones_pantalla_checkpoint"]:
        boton_seleccionado = manejar_colision_pantalla_checkpoint(mouse_pos, dict_general_pantallas_secundarias)
        if boton_seleccionado != None:
            manejar_boton_pantalla_checkpoint(boton_seleccionado, estado_juego["flags_variables"])
        
def manejar_evento_pantalla_victoria(estado_juego, mouse_pos, elementos_pantalla):
    """
    Maneja la selección de botones en la pantalla de victoria y actualiza el estado del juego.
    
    Parámetros:
    - estado_juego: Diccionario con el estado actual del juego.
    - mouse_pos: Tupla con la posición actual del ratón.
    - elementos_pantalla: Diccionario con los elementos de la pantalla de victoria.
    """
    dict_general_pantallas_secundarias = elementos_pantalla["dict_general_pantallas_secundarias"]
    if estado_juego["flags_variables"]["botones_pantalla_victoria"]:
        boton_seleccionado = manejar_colision_pantalla_victoria(mouse_pos, dict_general_pantallas_secundarias)
        if boton_seleccionado != None:
            manejar_boton_pantalla_victoria(boton_seleccionado, estado_juego["flags_variables"])

        