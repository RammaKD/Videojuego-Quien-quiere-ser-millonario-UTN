import pygame
from funciones_visuales import *
from generales import *
from funciones_archivos import *
from elementos import *



def manejar_evento_quit(evento, flags_variables):
    if evento.type == pygame.QUIT:
        flags_variables["flag_run"] = False

def manejar_colision_pantalla_principal(mouse_pos, flags_variables, lista_elementos_interactivos_principal):
    for elemento in lista_elementos_interactivos_principal:
        if elemento[1].collidepoint(mouse_pos):
            if elemento[0] == "JUGAR":
                flags_variables["flag_pantalla_principal"] = False
                flags_variables["flag_pantalla_categorias"] = True
            else:
                flags_variables["flag_run"] = False
            break

def manejar_colision_pantalla_categorias(mouse_pos, flags_variables, lista_elementos_interactivos_categorias):
    categoria_elegida = None
    for elemento in lista_elementos_interactivos_categorias:
        if elemento[1].collidepoint(mouse_pos):
            categoria_elegida = elemento[0]
            flags_variables["flag_pantalla_categorias"] = False
            flags_variables["flag_pantalla_juego"] = True
            flags_variables["flag_cronometro_activo"] = True
            break
    
    return categoria_elegida

def manejar_colision_respuestas_pantalla_juego(mouse_pos, lista_elementos_interactivos_juego):
    respuesta_seleccionada = None
    for elemento in lista_elementos_interactivos_juego[:4]:
        if elemento[1].collidepoint(mouse_pos):
            respuesta_seleccionada = elemento[0]
    
    return respuesta_seleccionada

def manejar_colision_comodines_pantalla_juego(mouse_pos, flags_variables, ventana_principal, lista_textos_pantalla_juego, lista_elementos_interactivos_juego, lista_imgs_pantalla_juego, lista_respuestas, respuesta_correcta, pista, fuente, color_texto, color_fondo):
    for elemento in lista_elementos_interactivos_juego[4:7]:
        if elemento[1].collidepoint(mouse_pos):
            if elemento[0] == "Llamada" and flags_variables["flag_comodin_pista"]:
                flags_variables["flag_comodin_pista"] = False
                mostrar_pista(ventana_principal, pista, FUENTE_PANTALLA_JUEGO, BLANCO, VIOLETA)
            elif elemento[0] == "Publico" and flags_variables["flag_comodin_publico"]:
                flags_variables["flag_comodin_publico"] = False
                lista_porcentajes = generar_porcentajes(lista_respuestas, respuesta_correcta)
                blitear_porcentajes(ventana_principal, lista_porcentajes, lista_respuestas, fuente, color_texto, color_fondo)    
            elif elemento[0] == "50-50" and flags_variables["flag_comodin_50_50"]:
                lista_elementos_interactivos_juego.clear()
                lista_textos_pantalla_juego = aplicar_comodin_50_50(lista_textos_pantalla_juego, lista_respuestas, respuesta_correcta)
                lista_elementos_pantalla_juego = lista_imgs_pantalla_juego + lista_textos_pantalla_juego 
                cargar_pantalla(ventana_principal, lista_elementos_pantalla_juego, FUENTE_PANTALLA_JUEGO, BLANCO, VIOLETA, lista_elementos_interactivos_juego)
                
                flags_variables["flag_comodin_50_50"] = False

def manejar_respuesta_seleccionada(flags_variables, m, nivel, contador_cronometro, respuesta_seleccionada, respuesta_correcta, niveles_premios, ventana_principal, lista_elementos_interactivos_juego, lista_textos_pantalla_checkpoint, lista_imgs_pantalla_game_over, lista_elementos_interactivos_checkpoint, lista_elementos_pantalla_victoria, lista_elementos_interactivos_victoria, lista_textos_pantalla_game_over_incorrecta, lista_elementos_interactivos_game_over):
    if respuesta_seleccionada != None:
        if corroborar_respuesta(respuesta_seleccionada, respuesta_correcta):
            m += 1
            nivel = str(niveles_premios[m][0])
            
            flags_variables["flag_pregunta_mostrada"] = False
            contador_cronometro = 30
            lista_elementos_interactivos_juego.clear()
            corroborar_checkpoint(m, nivel, flags_variables, niveles_premios, ventana_principal, lista_textos_pantalla_checkpoint, lista_imgs_pantalla_game_over, lista_elementos_interactivos_checkpoint, lista_elementos_pantalla_victoria, lista_elementos_interactivos_victoria)
        else:
            contador_cronometro = 30
            flags_variables["flag_cronometro_activo"] = False
            flags_variables["flag_pantalla_game_over"] = True
            flags_variables["flag_boton_pantalla_game_over"] = True
            flags_variables["flag_botones_respuestas"] = False
            flags_variables["flag_comodin_pista"] = False
            flags_variables["flag_comodin_publico"] = False
            flags_variables["flag_comodin_50_50"] = False
            mensaje_error = "Respuesta incorrecta"
            lista_textos_pantalla_game_over_incorrecta.append((mensaje_error, (320, 200), False))
            lista_elementos_pantalla_game_over_incorrecta = lista_imgs_pantalla_game_over + lista_textos_pantalla_game_over_incorrecta
            cargar_pantalla(ventana_principal, lista_elementos_pantalla_game_over_incorrecta, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)
    
    return nivel, m, contador_cronometro

def corroborar_checkpoint(m, nivel, flags_variables, niveles_premios, ventana_principal, lista_textos_pantalla_checkpoint, lista_imgs_pantalla_game_over, lista_elementos_interactivos_checkpoint, lista_elementos_pantalla_victoria, lista_elementos_interactivos_victoria):
    if nivel == "6" or nivel == "11":
        flags_variables["flag_pantalla_juego"] = False
        flags_variables["flag_cronometro_activo"] = False
        flags_variables["flag_botones_respuestas"] = False
        flags_variables["flag_pantalla_checkpoint"] = True
        flags_variables["flag_botones_pantalla_checkpoint"] = True
        dinero_a_retirar = niveles_premios[m - 1][1]
        mensaje_dinero_a_retirar = (f"O retirarse con: {dinero_a_retirar}", (250, 300), False)
        lista_textos_pantalla_checkpoint.append(mensaje_dinero_a_retirar)
        lista_elementos_pantalla_checkpoint = lista_imgs_pantalla_game_over + lista_textos_pantalla_checkpoint
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_checkpoint, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_checkpoint)
    elif nivel == "16":
        flags_variables["flag_pantalla_juego"] = False
        flags_variables["flag_cronometro_activo"] = False
        flags_variables["flag_botones_respuestas"] = False
        flags_variables["flag_pantalla_categorias"]
        flags_variables["flag_pantalla_victoria"] = True
        flags_variables["flag_botones_pantalla_victoria"] = True
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_victoria, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_victoria)
        
def manejar_colision_pantalla_pantalla_game_over(mouse_pos, lista_elementos_interactivos_game_over, flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos_juego):
    for elemento in lista_elementos_interactivos_game_over:
        if elemento[1].collidepoint(mouse_pos):
            flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos_juego = resetear_juego(flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos_juego)
            
    return flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos_juego

def manejar_colision_pantalla_checkpoint(mouse_pos, flags_variables, lista_elementos_interactivos_checkpoint):
    for elemento in lista_elementos_interactivos_checkpoint:
        if elemento[1].collidepoint(mouse_pos):
            if elemento[0] == "Retirarse":
                flags_variables["flag_pantalla_guardar_score"] = True
                flags_variables["flag_pregunta_mostrada"] = False
            else:
                flags_variables["flag_pantalla_juego"] = True
                flags_variables["flag_botones_respuestas"] = True
                flags_variables["flag_cronometro_activo"] = True
                flags_variables["flag_pregunta_mostrada"] = False
                flags_variables["flag_botones_pantalla_checkpoint"] = False

def manejar_colision_pantalla_victoria(mouse_pos, flags_variables, lista_elementos_interactivos_victoria):
    for elemento in lista_elementos_interactivos_victoria:
        if elemento[1].collidepoint(mouse_pos):
            if elemento[0] == "Retirar premio":
                flags_variables["flag_pantalla_guardar_score"] = True
                flags_variables["flag_pregunta_mostrada"] = False
            
def manejar_evento_guardar_score(event, flags_variables, texto_input_box, input_box_premio, m, nivel,niveles_premios, lista_elementos_interactivos_juego):
    if event.key == pygame.K_BACKSPACE:
            texto_input_box = texto_input_box[:-1]
    elif event.key == pygame.K_ESCAPE:
        texto_input_box = ""
    else:
        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
            if len(texto_input_box) > 0:
                nombre = texto_input_box
                if m == 15:
                    m -=1
                score = niveles_premios[m][1]
                nueva_puntuacion = f"{nombre}: {score}"
                actualizar_billetera_json(diccionario_paths["path_billetera"], nueva_puntuacion)
                texto_input_box = ""
                flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos_juego = resetear_juego(flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos_juego)
        else:    
            texto_input_box += event.unicode
            
    return texto_input_box, texto_surface, input_box_premio, m, nivel  



def manejar_evento_cronometro(ventana_principal, flags_variables, contador_cronometro, texto_cronometro, niveles_premios, color_texto, color_fondo, fuente):
    if contador_cronometro < 11:
        color_texto = ROJO
    actualizar_cronometro(ventana_principal, contador_cronometro, texto_cronometro, fuente, color_texto, color_fondo)
    dibujar_niveles_premios(ventana_principal, niveles_premios, FUENTE_PIRAMIDE_PREMIOS, BLANCO, VIOLETA)
    contador_cronometro -= 1
    if contador_cronometro < 0:
        contador_cronometro = 30
        flags_variables["flag_cronometro_activo"] = False
        flags_variables["flag_pantalla_game_over"] = True
        flags_variables["flag_boton_pantalla_game_over"] = True
        flags_variables["flag_botones_respuestas"] = False
        flags_variables["flag_comodin_pista"] = False
        flags_variables["flag_comodin_publico"] = False
        flags_variables["flag_comodin_50_50"] = False
        mensaje_error = "Se le acabó el tiempo"
        lista_textos_pantalla_game_over_tiempo_finalizado.append((mensaje_error, (320, 200), False))
        lista_elementos_pantalla_game_over_tiempo_finalizado = lista_imgs_pantalla_game_over + lista_textos_pantalla_game_over_tiempo_finalizado
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_game_over_tiempo_finalizado, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)
    
    return contador_cronometro

def manejar_evento_mostrar_score(event, flags_variables,diccionario_paths,ventana_principal,lista_elementos_pantalla_principal,lista_imgs_pantalla_principal,fuente, color_texto, color_fondo, lista_textos_pantalla_principal):
    if event.key == pygame.K_TAB and flags_variables["flag_pantalla_principal"]:
                if flags_variables["flag_scores_mostrados"]:
                    flags_variables["flag_scores_mostrados"] = False
                    scores = cargar_billetera_json(diccionario_paths["path_billetera"])
                    puntajes = scores["billetera"]
                    if len(puntajes) > 0:
                        y = 50
                        for puntaje in puntajes:
                            texto_score = puntaje
                            posicion = (25,y)
                            inter_actividad = False
                            elemento_comp = (texto_score,posicion,inter_actividad)
                            lista_textos_pantalla_principal.append(elemento_comp)
                            y +=50
                        lista_elementos_pantalla_principal = lista_imgs_pantalla_principal + lista_textos_pantalla_principal
                        cargar_pantalla(ventana_principal,lista_elementos_pantalla_principal,fuente, color_texto , color_fondo ,lista_elementos_interactivos_principal)
                else:
                    flags_variables["flag_scores_mostrados"] = True
    
    return flags_variables,lista_elementos_pantalla_principal,lista_imgs_pantalla_principal,lista_textos_pantalla_principal

def manejar_evento_borrar_score_pantalla(event,flags_variables,lista_textos_pantalla_principal, ventana_principal,lista_elementos_pantalla_principal,fuente, color_texto, color_fondo,lista_elementos_interactivos_principal):
    if event.key == pygame.K_DELETE: 
                flags_variables["flag_pantalla_principal"] = True
                flags_variables["flag_scores_mostrados"] = False
                lista_textos_pantalla_principal = [
                    ("JUGAR", (380, 515), True), 
                    ("SALIR", (750, 515), True),
                    ("Pantalla puntajes[tab]", (370, 600), False)
                ]
                lista_elementos_pantalla_principal = lista_imgs_pantalla_principal + lista_textos_pantalla_principal
                
                cargar_pantalla(ventana_principal, lista_elementos_pantalla_principal, fuente, color_texto, color_fondo, lista_elementos_interactivos_principal)       
                    

    return flags_variables, lista_elementos_pantalla_principal, lista_imgs_pantalla_principal,lista_textos_pantalla_principal