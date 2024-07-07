import pygame
from generales import *
from configuraciones import *
from elementos import *
from eventos import *

pygame.init()
while flags_variables["run"]:
    for event in pygame.event.get():
        manejar_evento_quit(event, flags_variables)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            if flags_variables["pantalla_principal"]:
                manejar_colision_pantalla_principal(mouse_pos, flags_variables, dict_elementos_pantalla_principal)
            
            elif flags_variables["pantalla_categorias"]:
                categoria_elegida = manejar_colision_pantalla_categorias(mouse_pos, flags_variables, 
                                                                         dict_elementos_pantalla_categorias)
            
            elif flags_variables["pantalla_juego"] and flags_variables["botones_respuestas"]:
                pregunta_elegida = manejar_colision_respuestas_pantalla_juego(mouse_pos, dict_elementos_pantalla_juego)
                comodin_elegido = manejar_colision_comodines_pantalla_juego(mouse_pos, dict_elementos_pantalla_juego)
                if comodin_elegido != None:
                    cargar_comodin_en_pantalla(ventana_principal, flags_variables, dict_elementos_pantalla_juego, 
                                               dict_pregunta_cargada, comodin_elegido)
                
                if pregunta_elegida != None:
                    dict_pregunta_cargada["pregunta_seleccionada"] = pregunta_elegida
                    contador_nivel = manejar_respuesta_seleccionada(flags_variables, contador_nivel, 
                                                                    dict_pregunta_cargada, dict_elementos_pantalla_juego)
                    corroborar = corroborar_checkpoint_y_victoria(contador_nivel,flags_variables, dict_niveles_premios, 
                                                                  dict_general_pantallas_secundarias)
                    if corroborar:
                        flags_variables["pantalla_checkpoint"] = True
                        flags_variables["botones_pantalla_checkpoint"] = True
                        cargar_pantalla(ventana_principal,dict_general_pantallas_secundarias["checkpoint"])
                    elif corroborar == False:
                        cargar_pantalla(ventana_principal,dict_general_pantallas_secundarias["victoria"])
                    dict_cronometro["contador"] = 30
                    if not contador_nivel:
                        msj_error = "Respuesta incorrecta"
                        dict_general_pantallas_secundarias = habilitar_game_over(flags_variables, 
                                                                                 dict_general_pantallas_secundarias, msj_error)
                        cargar_pantalla(ventana_principal,dict_general_pantallas_secundarias["game_over"])
            
            elif flags_variables["pantalla_game_over"] and flags_variables["boton_pantalla_game_over"]:
                if manejar_colision_pantalla_pantalla_game_over(mouse_pos,dict_general_pantallas_secundarias):
                    contador_nivel = resetear_juego(flags_variables,dict_elementos_pantalla_juego,contador_nivel)
            elif flags_variables["pantalla_checkpoint"] and flags_variables["botones_pantalla_checkpoint"]:
                manejar_colision_pantalla_checkpoint(mouse_pos, flags_variables, dict_general_pantallas_secundarias)
            elif flags_variables["pantalla_victoria"] and flags_variables["botones_pantalla_victoria"]:
                manejar_colision_pantalla_victoria(mouse_pos, flags_variables, dict_general_pantallas_secundarias)
        
        elif event.type == pygame.KEYDOWN:
            if flags_variables["pantalla_guardar_score"] and flags_variables["botones_pantalla_guardar_score"]:
                if manejar_evento_guardar_score(event, contador_nivel, dict_niveles_premios, 
                                                dict_general_pantallas_secundarias,flags_variables):
                    contador_nivel = resetear_juego(flags_variables,dict_elementos_pantalla_juego,contador_nivel)
        elif event.type == CRONOMETRO and flags_variables["cronometro_activo"]:
            actualizado = actualizar_cronometro(ventana_principal, dict_cronometro)
            if not actualizado:
                msj_error = "Se le acabó el tiempo"
                dict_general_pantallas_secundarias = habilitar_game_over(flags_variables, 
                                                                         dict_general_pantallas_secundarias, msj_error)
                cargar_pantalla(ventana_principal,dict_general_pantallas_secundarias["game_over"])
    
    if flags_variables["pantalla_principal"]:
        cargar_pantalla(ventana_principal, dict_elementos_pantalla_principal)
    elif flags_variables["pantalla_categorias"]:
        cargar_pantalla(ventana_principal, dict_elementos_pantalla_categorias)
    elif flags_variables["pantalla_juego"] and not flags_variables["pregunta_mostrada"]:
        dict_pregunta_cargada = cargar_elementos_juego(lista_preguntas, categoria_elegida,contador_nivel)
        dict_elementos_pantalla_juego = modificar_dict_pantalla_juego(dict_elementos_pantalla_juego, dict_pregunta_cargada)
        cargar_pantalla(ventana_principal, dict_elementos_pantalla_juego)
        dibujar_niveles_premios(ventana_principal, dict_niveles_premios)
        actualizar_cronometro(ventana_principal, dict_cronometro)
        flags_variables["pregunta_mostrada"] = True
        blitear_flecha(contador_nivel)
    elif flags_variables["pantalla_guardar_score"]:
        flags_variables["botones_respuestas"] = False
        flags_variables["boton_pantalla_game_over"] = False
        flags_variables["botones_pantalla_checkpoint"] = False
        flags_variables["botones_pantalla_guardar_score"] = True
        botones = cargar_pantalla(ventana_principal, dict_general_pantallas_secundarias["score"])
        surface_text = botones[2]["superficie"]
        rectangulo_text = botones[2]["rectangulo"]
        pygame.draw.rect(ventana_principal, ROJO, (rectangulo_text.x,rectangulo_text.y,450,65),3)
        rectangulo_dibujado = pygame.Rect(rectangulo_text.x, rectangulo_text.y, 450, 65)
        if colision_lado_derecho(rectangulo_dibujado, rectangulo_text):
            flags_variables["colision_rects"] = True
    pygame.display.update()
        
pygame.quit()
        
    
    
            
            

                
        
                
                        

                    

            
            
        
    




