import pygame
from generales import *

lista_preguntas = []
lista_preguntas_tocadas = []
path_preguntas = cargar_paths("paths.json")[0]
path_dinero = cargar_paths("paths.json")[1]
path_fondo_menu = cargar_paths("paths.json")[2]
path_logo = cargar_paths("paths.json")[3]

#PYGAME#######################################################################################
NEGRO  = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)
BLANCO = (255,255,255)

ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
DIMENSIONES_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

pygame.init()

ventana_principal = pygame.display.set_mode(DIMENSIONES_VENTANA)
pygame.display.set_caption("Quien quiere ser millonario?")
ventana_principal.fill(AZUL_CLARO)

fondo_menu = pygame.image.load(path_fondo_menu)
fondo_menu = pygame.transform.scale(fondo_menu, DIMENSIONES_VENTANA)
logo = pygame.image.load(path_logo)
logo = pygame.transform.scale(logo, (370,320))

fuente = pygame.font.SysFont("sinsum", 75)
texto_play = fuente.render("JUGAR", False, BLANCO, AZUL_CLARO)
texto_exit = fuente.render("SALIR", False, BLANCO, AZUL_CLARO) 

texto_play_rect = pygame.Rect(380,480,180,53)

flag_run = True
while flag_run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if texto_play_rect.collidepoint(evento.pos):
                print("Paso algo")
    
    
    ventana_principal.blit(fondo_menu, (0,0))
    ventana_principal.blit(logo, (480, 75))
    ventana_principal.blit(texto_play, (380, 480))
    ventana_principal.blit(texto_exit, (750, 480))
    pygame.display.update()


pygame.quit()


# piramide_premios =  [
#     ["Muy fácil", 100],
#     ["Muy fácil", 200],
#     ["Fácil", 300],
#     ["Fácil", 500],
#     ["Fácil", 1000],
#     ["Medio", 2000],
#     ["Medio", 4000],
#     ["Medio", 8000],
#     ["Medio", 16000],
#     ["Medio", 32000],
#     ["Dificil", 64000],
#     ["Dificil", 125000],
#     ["Dificil", 250000],
#     ["Muy dificil", 500000],
#     ["Muy dificil", 1000000]
#]

# seguir = True
# while seguir:
#     print("1. JUGAR")
#     print("2. SALIR")
#     opcion = seleccionar_opcion_menu("Elija una opción: ")

#     match opcion:
#         case 1:
#             seguir_eligiendo = True
#             while seguir_eligiendo:
#                 print("1. Historia")
#                 print("2. Deporte")
#                 print("3. Entretinimiento")
#                 print("4. Ciencia")
#                 print("5. Geografía")
#                 print("6. Salir")
#                 lista_categorias = ["Historia", "Deporte", "Entretenimiento", "Ciencia", "Geografía"]
#                 opcion_categoria = seleccionar_opcion_menu("Elija una opción: ")
#                 lista_preguntas.clear()
#                 if opcion_categoria != 6:
#                     categoria_elegida = lista_categorias[opcion_categoria - 1]
#                     leer_preguntas_desde_csv(lista_preguntas, categoria_elegida, path_preguntas)
#                     billetera = cargar_puntuaciones_json(path_dinero)
#                     print(f"Billetera: ${billetera}")
                
#                 match opcion_categoria:
#                     case 1:
#                         ejecutar_juego(lista_preguntas, lista_preguntas_tocadas, piramide_premios, billetera, path_dinero)
#                         break
#                     case 2: 
#                         ejecutar_juego(lista_preguntas, lista_preguntas_tocadas, piramide_premios, billetera, path_dinero)
#                         break
#                     case 3:
#                         ejecutar_juego(lista_preguntas, lista_preguntas_tocadas, piramide_premios, billetera, path_dinero)
#                         break
#                     case 4:
#                         ejecutar_juego(lista_preguntas, lista_preguntas_tocadas, piramide_premios, billetera, path_dinero)
#                         break
#                     case 5:
#                         ejecutar_juego(lista_preguntas, lista_preguntas_tocadas, piramide_premios, billetera, path_dinero)
#                         break
                        
#                     case 6:
#                         if desea_continuar("Desea dejar de elegir? SI/NO: ", "Error. Ingrese SI/NO: "):
#                             seguir_eligiendo = False
#                     case _:
#                         print("Error. Ingrese una opción del Menú.")
                        
#         case 2:
#             if desea_continuar("Desea salir? SI/NO: ", "Error. Ingrese SI/NO: "):
#                 seguir = False
#                 break
#         case _:
#             print("Error. Ingrese una opción del Menú.")


