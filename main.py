import pygame
from generales import *
from configuraciones import *
from elementos import *
from eventos import *

pygame.init()
ventana_principal = pygame.display.set_mode(DIMENSIONES_VENTANA)
pygame.display.set_caption("Quien quiere ser millonario?")
pygame.display.set_icon(logo)
pygame.time.set_timer(CRONOMETRO, 1000)

blitear_flecha = lambda nivel: ventana_principal.blit(flecha, (995, ALTO_VENTANA - 60 - (contador_nivel+1) * 40))


while flags_variables["flag_run"]:
    for event in pygame.event.get():
        manejar_evento_quit(event, flags_variables)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if flags_variables["flag_pantalla_principal"]:
                manejar_colision_pantalla_principal(mouse_pos, flags_variables, dict_elementos_pantalla_principal)
            elif flags_variables["flag_pantalla_categorias"]:
                categoria_elegida = manejar_colision_pantalla_categorias(mouse_pos, flags_variables, dict_elementos_pantalla_categorias)
            elif flags_variables["flag_pantalla_juego"] and flags_variables["flag_botones_respuestas"]:
                dict_pregunta_cargada["pregunta_seleccionada"] = manejar_colision_respuestas_pantalla_juego(mouse_pos, dict_elementos_pantalla_juego)
                print(dict_pregunta_cargada["pregunta_seleccionada"])
                manejar_colision_comodines_pantalla_juego(mouse_pos, flags_variables, ventana_principal, dict_elementos_pantalla_juego, dict_pregunta_cargada)
                
                # blitear_flecha(nivel)
                nivel, m, contador_cronometro = manejar_respuesta_seleccionada(flags_variables, m, nivel, contador_cronometro,dict_pregunta_cargada, niveles_premios, ventana_principal, dict_elementos_pantalla_juego, dict_general_pantallas_secundarias)
            elif flags_variables["flag_pantalla_game_over"] and flags_variables["flag_boton_pantalla_game_over"]:
                flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos_juego = manejar_colision_pantalla_pantalla_game_over(mouse_pos, lista_elementos_interactivos_game_over, flags_variables, m, nivel, niveles_premios, lista_elementos_interactivos_juego)
            elif flags_variables["flag_pantalla_checkpoint"] and flags_variables["flag_botones_pantalla_checkpoint"]:
                manejar_colision_pantalla_checkpoint(mouse_pos, flags_variables, lista_elementos_interactivos_checkpoint)
            elif flags_variables["flag_pantalla_victoria"] and flags_variables["flag_botones_pantalla_victoria"]:
                manejar_colision_pantalla_victoria(mouse_pos, flags_variables, lista_elementos_interactivos_victoria)
        
        elif event.type == pygame.KEYDOWN:
            if flags_variables["flag_pantalla_guardar_score"] and flags_variables["flag_botones_pantalla_guardar_score"]:
                texto_input_box, texto_surface, input_box_premio, m, nivel = manejar_evento_guardar_score(event, flags_variables, texto_input_box, input_box_premio,  m, nivel,niveles_premios, lista_elementos_interactivos_juego)
            flags_variables,lista_elementos_pantalla_principal,lista_imgs_pantalla_principal,lista_textos_pantalla_principal = manejar_evento_mostrar_score(event,flags_variables, diccionario_paths, ventana_principal, lista_elementos_pantalla_principal, lista_imgs_pantalla_principal, FUENTE_PRINCIPAL, BLANCO, VIOLETA, lista_textos_pantalla_principal)
            
            flags_variables, lista_elementos_pantalla_principal, lista_imgs_pantalla_principal,lista_textos_pantalla_principal = manejar_evento_borrar_score_pantalla(event,flags_variables,lista_textos_pantalla_principal,ventana_principal, lista_elementos_pantalla_principal, FUENTE_PRINCIPAL, BLANCO, VIOLETA, lista_elementos_interactivos_principal)
        
        elif event.type == CRONOMETRO and flags_variables["flag_cronometro_activo"]:
            contador_cronometro = manejar_evento_cronometro(ventana_principal, flags_variables, contador_cronometro, dict_niveles_premios, dict_cronometro)
    
    if flags_variables["flag_pantalla_principal"]:
        cargar_pantalla(ventana_principal, dict_elementos_pantalla_principal)
    
    elif flags_variables["flag_pantalla_categorias"]:
        cargar_pantalla(ventana_principal, dict_elementos_pantalla_categorias)
    
    elif flags_variables["flag_pantalla_juego"] and not flags_variables["flag_pregunta_mostrada"]:
        dict_pregunta_cargada = cargar_elementos_juego(lista_preguntas, categoria_elegida,contador_nivel)
        dict_elementos_pantalla_juego = modificar_dict_pantalla_juego(dict_elementos_pantalla_juego, dict_pregunta_cargada)
        cargar_pantalla(ventana_principal, dict_elementos_pantalla_juego)
        flags_variables["flag_pregunta_mostrada"] = True
        blitear_flecha(contador_nivel)
        actualizar_cronometro(ventana_principal, dict_cronometro)
        dibujar_niveles_premios(ventana_principal, dict_niveles_premios, FUENTE_PIRAMIDE_PREMIOS, BLANCO, VIOLETA)
    elif flags_variables["flag_pantalla_guardar_score"]:
        flags_variables["flag_botones_respuestas"] = False
        flags_variables["flag_boton_pantalla_game_over"] = False
        flags_variables["flag_botones_pantalla_checkpoint"] = False
        flags_variables["flag_botones_pantalla_guardar_score"] = True
        cargar_pantalla(ventana_principal, lista_elementos_pantalla_score, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_score)
        blitear_texto_nombre(texto_input_box, texto_surface, input_box_premio, ventana_principal)
    
    pygame.display.update()
        
pygame.quit()




