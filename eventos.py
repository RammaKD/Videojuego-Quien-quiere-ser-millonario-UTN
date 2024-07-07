import pygame
from funciones_visuales import *
from generales import *
from funciones_archivos import *
from elementos import *


blitear_flecha = lambda contador_nivel: ventana_principal.blit(flecha, (995, ALTO_VENTANA - 60 - (contador_nivel + 1) * 40))

def manejar_evento_quit(evento, flags_variables):
    if evento.type == pygame.QUIT:
        flags_variables["run"] = False

def manejar_colision_pantalla_principal(mouse_pos, flags_variables, dict_elementos: dict):
    for elemento in dict_elementos["interactivos"]:
        if elemento[1].collidepoint(mouse_pos):
            if elemento[0] == "JUGAR":
                flags_variables["pantalla_principal"] = False
                flags_variables["pantalla_categorias"] = True
            else:
                flags_variables["run"] = False
            break

def manejar_colision_pantalla_categorias(mouse_pos, flags_variables, dict_elementos):
    categoria_elegida = None
    for elemento in dict_elementos["interactivos"]:
        if elemento[1].collidepoint(mouse_pos):
            categoria_elegida = elemento[0]
            flags_variables["pantalla_categorias"] = False
            flags_variables["pantalla_juego"] = True
            flags_variables["cronometro_activo"] = True
            break
    
    return categoria_elegida

def manejar_colision_respuestas_pantalla_juego(mouse_pos, dict_elementos):
    respuesta_seleccionada = None
    for elemento in dict_elementos["interactivos"][:4]:
        if elemento[1].collidepoint(mouse_pos):
            respuesta_seleccionada = elemento[0]

    return respuesta_seleccionada

def manejar_colision_comodines_pantalla_juego(mouse_pos, dict_elementos):
    comodin_elegido = None
    for elemento in dict_elementos["interactivos"][4:7]:
        if elemento[1].collidepoint(mouse_pos):
            comodin_elegido = elemento[0]

    return comodin_elegido
            
def cargar_comodin_en_pantalla(ventana_principal, flags_variables, dict_elementos, dict_pregunta, comodin):
    fuente =  dict_elementos["fuente"][0]
    color_texto = dict_elementos["fuente"][1]
    color_fondo = dict_elementos["fuente"][2]
    
    if comodin == "Llamada" and flags_variables["comodin_pista"]:
        flags_variables["comodin_pista"] = False
        mostrar_pista(ventana_principal, dict_pregunta["pista"], fuente, color_texto , color_fondo)
    
    elif comodin == "Publico" and flags_variables["comodin_publico"]:
        flags_variables["comodin_publico"] = False
        lista_porcentajes = generar_porcentajes(dict_pregunta["respuestas"], dict_pregunta["respuesta_correcta"])
        blitear_porcentajes(ventana_principal, lista_porcentajes, dict_pregunta["respuestas"], fuente, color_texto, color_fondo)    
    
    elif comodin == "50-50" and flags_variables["comodin_50_50"]:
        flags_variables["comodin_50_50"] = False
        dict_elementos["interactivos"].clear()
        dict_elementos["textos"] = aplicar_comodin_50_50(dict_elementos["textos"], dict_pregunta["respuestas"], dict_pregunta["respuesta_correcta"])
        cargar_pantalla(ventana_principal, dict_elementos)
        dibujar_niveles_premios(ventana_principal, dict_niveles_premios)
        blitear_flecha(contador_nivel)
    
def manejar_respuesta_seleccionada(flags_variables, contador_nivel,  dict_pregunta_cargada, dict_elementos_pantalla_juego):
    retorno = False
    if dict_pregunta_cargada["respuesta_correcta"] == dict_pregunta_cargada["pregunta_seleccionada"]:
        contador_nivel += 1
        flags_variables["pregunta_mostrada"] = False
        dict_elementos_pantalla_juego["interactivos"].clear()
        retorno = contador_nivel
        
        
    return retorno
        
def corroborar_checkpoint_y_victoria(contador_nivel, flags_variables, dict_niveles_premios,  dict_general_pantallas_secundarias):
    retorno = None
    nivel = contador_nivel + 1

    if nivel == 6 or nivel == 11:
        desactivar_pantalla_juego(flags_variables)
        dinero_a_retirar = dict_niveles_premios["piramide"][contador_nivel - 1][1]
        dict_general_pantallas_secundarias["checkpoint"]["textos"][3][0] = f"O retirarse con: {dinero_a_retirar}"
        retorno = True
    elif nivel == 16:
        desactivar_pantalla_juego(flags_variables)
        flags_variables["pantalla_victoria"] = True
        flags_variables["botones_pantalla_victoria"] = True
        retorno = False
        
       
    return retorno
       
def manejar_colision_pantalla_pantalla_game_over(mouse_pos, dict_general_pantallas_secundarias):
    retorno = False
    for elemento in dict_general_pantallas_secundarias["game_over"]["interactivos"]:
        if elemento[1].collidepoint(mouse_pos):
            retorno = True

    return retorno
            
def manejar_colision_pantalla_checkpoint(mouse_pos, flags_variables, dict_general_pantallas_secundarias):
    for elemento in dict_general_pantallas_secundarias["checkpoint"]["interactivos"]:
        if elemento[1].collidepoint(mouse_pos):
            if elemento[0] == "Retirarse":
                flags_variables["pantalla_guardar_score"] = True
                flags_variables["pregunta_mostrada"] = False
            else:
                flags_variables["pantalla_juego"] = True
                flags_variables["botones_respuestas"] = True
                flags_variables["cronometro_activo"] = True
                flags_variables["pregunta_mostrada"] = False
                flags_variables["botones_pantalla_checkpoint"] = False

def manejar_colision_pantalla_victoria(mouse_pos, flags_variables, dict_general_pantallas_secundarias):
    for elemento in dict_general_pantallas_secundarias["victoria"]["interactivos"]:
        if elemento[1].collidepoint(mouse_pos):
            if elemento[0] == "Retirar premio":
                flags_variables["pantalla_guardar_score"] = True
                flags_variables["botones_pantalla_guardar_score"] = True
                flags_variables["pregunta_mostrada"] = False
            
def manejar_evento_guardar_score(event, contador_nivel, dict_niveles_premios, dict_general_pantallas_secundarias, flags_variables):
    retorno = False
    if event.key == pygame.K_BACKSPACE or flags_variables["colision_rects"]:
        flags_variables["colision_rects"] = False
        dict_general_pantallas_secundarias["score"]["textos"][1][0] = dict_general_pantallas_secundarias["score"]["textos"][1][0][:-1]
    elif event.key == pygame.K_ESCAPE:
        dict_general_pantallas_secundarias["score"]["textos"][1][0] = ""
    else:
        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
            if len(dict_general_pantallas_secundarias["score"]["textos"][1][0]) > 0:
                nombre = dict_general_pantallas_secundarias["score"]["textos"][1][0]
                if contador_nivel == 15:
                    contador_nivel -=1
                score = dict_niveles_premios["piramide"][contador_nivel][1]
                nueva_puntuacion = f"{nombre}: {score}"
                actualizar_billetera_json(diccionario_paths["path_billetera"], nueva_puntuacion)
                dict_general_pantallas_secundarias["score"]["textos"][1][0] = ""
                retorno = True
                
        else:    
            if len(dict_general_pantallas_secundarias["score"]["textos"][1][0]) < 12:
                dict_general_pantallas_secundarias["score"]["textos"][1][0] += event.unicode
            
    return retorno

def manejar_evento_mostrar_score(event, flags_variables, diccionario_paths, dict_elementos_pantalla_principal):
    if event.key == pygame.K_TAB or event.key == pygame.K_DELETE:
        if not flags_variables["scores_mostrados"]:
            scores = cargar_billetera_json(diccionario_paths["path_billetera"])
            puntajes = scores["billetera"]
            if len(puntajes) > 0:
                y = 50
                for puntaje in puntajes:
                    texto_score = puntaje
                    posicion = (25,y)
                    inter_actividad = False
                    elemento_comp = (texto_score,posicion,inter_actividad)
                    dict_elementos_pantalla_principal["textos"].append(elemento_comp)
                    y +=50
                    flags_variables["scores_mostrados"] = True
                
        else:
            flags_variables["flag_pantalla_principal"] = True
            flags_variables["flag_scores_mostrados"] = False
            lista_textos_pantalla_principal = [("JUGAR", (380, 515), True), 
                                               ("SALIR", (750, 515), True),
                                               ("Pantalla puntajes[tab]", (370, 600), False)]
    
    return flags_variables
                          