import pygame
from generales import *
from configuraciones import *
from elementos import *

pygame.init()
ventana_principal = pygame.display.set_mode(DIMENSIONES_VENTANA)
pygame.display.set_caption("Quien quiere ser millonario?")
pygame.display.set_icon(logo)
pygame.time.set_timer(CRONOMETRO, 1000)

while flags_variables["flag_run"]:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flags_variables["flag_run"] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if flags_variables["flag_pantalla_principal"]:
                for elemento in lista_elementos_interactivos_principal:
                    if elemento[1].collidepoint(mouse_pos):
                        if elemento[0] == "JUGAR":
                            flags_variables["flag_pantalla_principal"] = False
                            flags_variables["flag_pantalla_categorias"] = True
                        else:
                            flags_variables["flag_run"] = False
                        break
                    
            elif flags_variables["flag_pantalla_categorias"]:
                for elemento in lista_elementos_interactivos_categorias:
                    if elemento[1].collidepoint(mouse_pos):
                        categoria_elegida = elemento[0]
                        flags_variables["flag_pantalla_categorias"] = False
                        flags_variables["flag_pantalla_juego"] = True
                        flags_variables["flag_cronometro_activo"] = True
                        break
                
            elif flags_variables["flag_pantalla_juego"] and flags_variables["flag_botones_respuestas"]:
                respuesta_seleccionada = None
                for elemento in lista_elementos_interactivos_juego[:4]:
                    if elemento[1].collidepoint(mouse_pos):
                        respuesta_seleccionada = elemento[0]
                        break
        
                if respuesta_seleccionada != None:
                    if corroborar_respuesta(respuesta_seleccionada, respuesta_correcta):
                        flags_variables["flag_pregunta_mostrada"] = False
                        m += 1
                        nivel = str(niveles_premios[m][0])
                        contador_cronometro = 10
                        lista_elementos_interactivos_juego.clear()
                        if nivel == "6" or nivel == "11":
                            flags_variables["flag_pantalla_juego"] = False
                            flags_variables["flag_cronometro_activo"] = False
                            flags_variables["flag_botones_respuestas"] = False
                            flags_variables["flag_pantalla_checkpoint"] = True
                            flags_variables["flag_botones_pantalla_checkpoint"] = True
                            dinero_a_retirar = niveles_premios[m - 1][1]
                            mensaje_dinero_a_retirar = (f"O retirarse con: {dinero_a_retirar}", (450, 350), False)
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
                            
                    else:
                        contador_cronometro = 10
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
            
            
            elif flags_variables["flag_pantalla_game_over"] and flags_variables["flag_boton_pantalla_game_over"]:
                for elemento in lista_elementos_interactivos_game_over:
                    if elemento[1].collidepoint(mouse_pos):
                        flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos_juego = resetear_juego(flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos_juego)
            
            elif flags_variables["flag_pantalla_checkpoint"] and flags_variables["flag_botones_pantalla_checkpoint"]:
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
            
            elif flags_variables["flag_pantalla_victoria"] and flags_variables["flag_botones_pantalla_victoria"]:
                for elemento in lista_elementos_interactivos_victoria:
                    if elemento[1].collidepoint(mouse_pos):
                        if elemento[0] == "Retirar premio":
                            flags_variables["flag_pantalla_guardar_score"] = True
                            flags_variables["flag_pregunta_mostrada"] = False
            
                            
            for elemento in lista_elementos_interactivos_juego[4:7]:
                if elemento[1].collidepoint(mouse_pos):
                    if elemento[0] == "Llamada" and flags_variables["flag_comodin_pista"]:
                        flags_variables["flag_comodin_pista"] = False
                        mostrar_pista(ventana_principal, pista, FUENTE_PANTALLA_JUEGO, BLANCO, VIOLETA)
                        break
                    elif elemento[0] == "Publico" and flags_variables["flag_comodin_publico"]:
                        flags_variables["flag_comodin_publico"] = False
                        lista_porcentajes = generar_porcentajes(lista_respuestas, respuesta_correcta)
                        blitear_porcentajes(ventana_principal, lista_porcentajes, lista_respuestas)    
                    elif elemento[0] == "50-50" and flags_variables["flag_comodin_50_50"]:
                        lista_elementos_interactivos_juego.clear()
                        lista_textos_pantalla_juego = aplicar_comodin_50_50(lista_textos_pantalla_juego, lista_respuestas, respuesta_correcta)
                        lista_elementos_pantalla_juego = lista_imgs_pantalla_juego + lista_textos_pantalla_juego
                        cargar_pantalla(ventana_principal, lista_elementos_pantalla_juego, FUENTE_PANTALLA_JUEGO, BLANCO, VIOLETA, lista_elementos_interactivos_juego)
                        flags_variables["flag_comodin_50_50"] = False

        elif event.type == pygame.KEYDOWN:
            if flags_variables["flag_pantalla_guardar_score"] and flags_variables["flag_botones_pantalla_guardar_score"]:
                if event.key == pygame.K_BACKSPACE:
                    texto_input_box = texto_input_box[:-1]
                
                
                elif event.key == pygame.K_ESCAPE:
                    texto_input_box = ""
                else:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if len(texto_input_box) > 0:
                            nombre = texto_input_box
                            score = niveles_premios[m][1]
                            nueva_puntuacion = f"{nombre} :{score}"
                            actualizar_billetera_json(diccionario_paths["path_billetera"], nueva_puntuacion)
                            texto_input_box = ""
                            flags_variables, m, nivel,niveles_premios, lista_elementos_interactivos_juego = resetear_juego(flags_variables, m, nivel,niveles_premios, lista_elementos_interactivos_juego)
                    else:    
                        texto_temp = texto_input_box + event.unicode
                        texto_surface_temp = FUENTE_PANTALLA_GAME_OVER.render(texto_temp, True, BLANCO)
                        rect_temp = texto_surface_temp.get_rect()
                        if rect_temp.width <= input_box_premio.width:
                            texto_input_box += event.unicode

        
        elif event.type == CRONOMETRO and flags_variables["flag_cronometro_activo"]:
            actualizar_cronometro(ventana_principal, contador_cronometro, texto_cronometro, FUENTE_CRONOMETRO, BLANCO, VIOLETA)
            dibujar_niveles_premios(ventana_principal, niveles_premios, FUENTE_PIRAMIDE_PREMIOS, BLANCO, VIOLETA)
            contador_cronometro -= 1
            if contador_cronometro < 0:
                contador_cronometro = 10
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
    
    if flags_variables["flag_pantalla_principal"]:
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_principal, FUENTE_PRINCIPAL, BLANCO, VIOLETA, lista_elementos_interactivos_principal)
    elif flags_variables["flag_pantalla_categorias"]:
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_categorias, FUENTE_PRINCIPAL, BLANCO, VIOLETA, lista_elementos_interactivos_categorias)
    elif flags_variables["flag_pantalla_juego"] and not flags_variables["flag_pregunta_mostrada"]:
        respuesta_correcta, pista, lista_textos_pantalla_juego, lista_respuestas, lista_posiciones_respuestas = cargar_elementos_juego(ventana_principal, lista_preguntas, categoria_elegida, nivel, lista_imgs_pantalla_juego, lista_elementos_interactivos_juego)
        flags_variables["flag_pregunta_mostrada"] = True
        actualizar_cronometro(ventana_principal, contador_cronometro, texto_cronometro, FUENTE_CRONOMETRO, BLANCO, VIOLETA)
        dibujar_niveles_premios(ventana_principal, niveles_premios, FUENTE_PIRAMIDE_PREMIOS, BLANCO, VIOLETA)
    elif flags_variables["flag_pantalla_guardar_score"]:
        flags_variables["flag_botones_respuestas"] = False
        flags_variables["flag_boton_pantalla_game_over"] = False
        flags_variables["flag_botones_pantalla_checkpoint"] = False
        flags_variables["flag_botones_pantalla_guardar_score"] = True
        lista_elementos_pantalla_score = lista_imgs_pantalla_game_over + lista_textos_pantalla_score
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_score, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_score)
        input_box_premio = pygame.Rect(250, 450, 750, 65)
        texto_surface = crear_texto_renderizado(texto_input_box, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA)
        ventana_principal.blit(texto_surface, (input_box_premio.x, input_box_premio.y))
        pygame.draw.rect(ventana_principal, BLANCO, input_box_premio, 2)
    
    pygame.display.update()
        
pygame.quit()