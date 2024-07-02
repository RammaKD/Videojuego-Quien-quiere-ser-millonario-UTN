# import pygame
# from generales import *
# from configuraciones import *
# from elementos import *

# pygame.init()

# ventana_principal = pygame.display.set_mode(DIMENSIONES_VENTANA)
# pygame.display.set_caption("¿Quién quiere ser millonario?")
# pygame.display.set_icon(logo)

# CRONOMETRO = pygame.USEREVENT + 1  
# pygame.time.set_timer(CRONOMETRO, 0)  
# m = 0
# contador_nivel = niveles_premios[m][0]

# while flag_run:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             flag_run = False
#         elif evento.type == pygame.MOUSEBUTTONDOWN:
#             if flag_pantalla_principal:
#                 if lista_rects_menu[0].collidepoint(evento.pos) and flag_boton_play:
#                     flag_pantalla_principal = False
#                     flag_boton_salir = False
#                     flag_pantalla_categorias = True
#                     cargar_pantalla(ventana_principal, lista_elementos_menu_categorias)
#                 elif lista_rects_menu[1].collidepoint(evento.pos) and flag_boton_salir:
#                     flag_run = False
#             elif flag_pantalla_categorias:
#                 if lista_rects_categorias[1].collidepoint(evento.pos):
#                     flag_pantalla_juego = True
#                     categoria_elegida = "Historia"
#                 elif lista_rects_categorias[2].collidepoint(evento.pos):
#                     flag_pantalla_juego = True
#                     categoria_elegida = "Deportes"
#                 elif lista_rects_categorias[3].collidepoint(evento.pos):
#                     flag_pantalla_juego = True
#                     categoria_elegida = "Ciencia"
#                 elif lista_rects_categorias[4].collidepoint(evento.pos):
#                     flag_pantalla_juego = True
#                     categoria_elegida = "Entretenimiento"
#                 elif lista_rects_categorias[5].collidepoint(evento.pos):
#                     flag_pantalla_juego = True
#                     categoria_elegida = "Geografía"
#                 flag_cronometro_activo = True

#                 if flag_pantalla_juego:
#                     flag_pantalla_categorias = False
#                     flag_pregunta_mostrada = False
#                     flag_respuesta_seleccionada = False
#                     contador_cronometro = 10
#                     texto_cronometro = str(contador_cronometro).zfill(2)
#                     pygame.time.set_timer(CRONOMETRO, 1000)
            
#             elif flag_pantalla_juego:
#                 respuesta_seleccionada = None
#                 for i in range(2, len(lista_rects_jugando)):  
#                     if lista_rects_jugando[i].collidepoint(evento.pos):
#                         respuesta_seleccionada = lista_respuestas[i - 2]

#                 if respuesta_seleccionada != None:
#                     if corroborar_respuesta(respuesta_seleccionada, respuesta_correcta):
#                         flag_respuesta_correcta = True
#                         print("Respuesta correcta")
#                     else:
#                         flag_respuesta_correcta = False
#                         print("Respuesta incorrecta")
#                     flag_respuesta_seleccionada = True
                    
#         elif evento.type == CRONOMETRO and flag_cronometro_activo:
#             contador_cronometro -= 1
#             texto_cronometro = str(contador_cronometro).zfill(2)
#             if contador_cronometro <= 0:
#                 print("Se le acabó el tiempo\n1")
#                 flag_respuesta_seleccionada = True
#                 flag_respuesta_correcta = False

#     if flag_pantalla_principal:
#         cargar_pantalla(ventana_principal, lista_elementos_menu)
    
#     elif flag_pantalla_juego and not flag_pregunta_mostrada:
#         nivel = str(contador_nivel)
#         lista_elementos_pantalla_jugando, lista_rects_jugando, lista_respuestas, respuesta_correcta = cargar_elementos_pantalla_jugando(categoria_elegida, nivel)
#         flag_pregunta_mostrada = True
#         cargar_pantalla(ventana_principal, lista_elementos_pantalla_jugando)

#     elif flag_pantalla_juego and flag_respuesta_seleccionada:
#         if flag_respuesta_correcta:
#             (m, contador_nivel, flag_pregunta_mostrada, flag_respuesta_seleccionada, 
#             contador_cronometro, texto_cronometro) = manejar_respuesta_correcta(m, contador_nivel, niveles_premios, CRONOMETRO)
#             if contador_nivel == 2:  
#                 flag_pantalla_retirarse = True
#         else:
#             (flag_pantalla_juego, flag_pregunta_mostrada, flag_respuesta_seleccionada, 
#             flag_pantalla_principal, flag_cronometro_activo, flag_comodin_50_50_usado, 
#             flag_boton_salir, m, contador_nivel) = manejar_respuesta_incorrecta(niveles_premios)
    
#     elif flag_pantalla_juego:
#         actualizar_cronometro_pantalla_juego(ventana_principal, lista_elementos_pantalla_jugando, 
#                                   niveles_premios, ANCHO_VENTANA, texto_cronometro, 
#                                   FUENTE_CRONOMETRO, BLANCO, VIOLETA)
    
#     # Nueva pantalla de retirada
#     if flag_pantalla_retirarse:
#         rect_continuar, rect_retirarse = cargar_elementos_pantalla_retirarse(ventana_principal)
#         for evento in pygame.event.get():
#             if evento.type == pygame.MOUSEBUTTONDOWN:
#                 if rect_continuar.collidepoint(evento.pos):
#                     flag_pantalla_retirarse = False
#                     flag_pantalla_juego = True
#                 elif rect_retirarse.collidepoint(evento.pos):
#                     flag_pantalla_retirarse = False
#                     flag_pantalla_principal = True
#                     flag_pantalla_juego = False
#                     flag_pantalla_categorias = False
#                     flag_boton_salir = True
#                     flag_pregunta_mostrada = False
#                     flag_respuesta_seleccionada = False
#                     m = 1
#                     pygame.time.set_timer(CRONOMETRO, 0)  # Detener el cronómetro
#                     cargar_pantalla(ventana_principal, lista_elementos_menu)
    
#     pygame.display.update()

# pygame.quit()