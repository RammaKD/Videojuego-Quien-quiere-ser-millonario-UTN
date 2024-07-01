import pygame
from elementos import *




pygame.init()
# Colores
VIOLETA = (67, 0, 103)
BLANCO = (255, 255, 255)
POS_INICIAL_FONDO = (0,0)

def crear_fondo_texto(rect_texto, color_fondo):
    fondo_surface = pygame.Surface((rect_texto.width, rect_texto.height))
    fondo_surface.fill(color_fondo)
    return fondo_surface

def crear_texto_renderizado(texto, fuente, color):
    texto_renderizado = fuente.render(texto, True, color)
    return texto_renderizado

def blitear_imagenes(ventana_principal, lista_imagenes):
    exito = True
    try:
        for imagen in lista_imagenes:
            superficie = imagen[0]
            posicion = imagen[1]
            ventana_principal.blit(superficie,posicion)
    except:
        exito = False
    
    return exito
    
    

def blitear_objetos_interactivos(ventana_principal, lista_botones):
    exito = True
    try:
        for elemento in lista_botones:
            superficie = elemento["superficie"]
            fondo = elemento["fondo"]
            posicion = elemento["rectangulo"].topleft
            
            ventana_principal.blit(fondo, posicion)
            ventana_principal.blit(superficie, posicion)
            
    except:
        exito = False
    return exito

            

def crear_diccionario_botones(lista_botones, texto, surface, rect, posicion, fondo):
    """
    Crea un nuevo diccionario con los datos de un botón.
    Devuelve el diccionario creado si se pudieron convertir los datos correctamente, False en caso contrario.
    """
    try:
        
        elemento = {
            "texto": texto,
            "superficie": surface,
            "rectangulo": rect,
            "posicion": posicion,
            "fondo" : fondo
        }
        lista_botones.append(elemento)
    except Exception as e:
        print(f"Error al crear diccionario: {e}")
        elemento = False
    
    return elemento

def crear_propiedades_botones(ventana_principal,lista_textos, lista_botones, fuente, color_texto, color_fondo,lista_elementos_interactivos):
    for elemento in lista_textos:
        texto = elemento[0]
        posicion = elemento[1]
        interactivo = elemento[2]
        surface = crear_texto_renderizado(texto, fuente, color_texto)
        rect = surface.get_rect()
        rect.topleft = posicion
        fondo = crear_fondo_texto(rect, color_fondo)
        if interactivo:
            lista_elementos_interactivos.append((texto,rect))

        crear_diccionario_botones(lista_botones,texto,surface,rect,posicion,fondo)
        
    return lista_botones
        

# Configuración de la pantalla
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Botones con bordes redondeados")

# Definición de la fuente
fuente = pygame.font.SysFont(None, 36)

# Lista de botones
lista_elementos_interactivos_principal = []
lista_elementos_interactivos_categorias = []
lista_botones = []
lista_imagenes = []
lista_textos_menu_principal = [("JUGAR", (380, 515),True), ("SALIR", (750, 515),True)]
lista_textos_categorias = [              
                    ("Eliga una categoria",(450, 365),False),
                    ("HISTORIA", (250, 500),True),
                    ("DEPORTE", (527, 500),True),
                    ("CIENCIA", (800, 500),True),
                    ("ENTRETENIMIENTO", (200, 600),True),
                    ("GEOGRAFÍA", (750, 600),True)
                       ]
lista_imgs_menu_principal = [(fondo_menu, POS_INICIAL_FONDO),                    
                         (logo, (450,75))]


crear_propiedades_botones(screen,lista_textos_categorias,lista_botones,fuente,BLANCO,VIOLETA, lista_elementos_interactivos_categorias)

flag_pantalla_categorias = False
flag_run = True
flag_pantalla_principal = True
flag_pantalla_juego = False
flag_boton_play = True
flag_boton_salir = True
flag_pregunta_mostrada = False
flag_respuesta_seleccionada = False
flag_respuesta_correcta = False
flag_pantalla_retirarse = False
flag_cronometro_activo = True
flag_comodin_50_50_usado = False
flag_comodin_publico_usado = False

while flag_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_run = False
        elif event.type == pygame.MOUSEBUTTONDOWN :
            mouse_pos = event.pos
            # if flag_pantalla_principal:
            #     crear_propiedades_botones(screen,lista_textos_menu_principal,lista_botones, fuente, BLANCO,VIOLETA,lista_elementos_interactivos_principal)
            
            
            if flag_pantalla_categorias:
                for elemento in lista_elementos_interactivos_categorias:
                    if elemento[1].collidepoint(mouse_pos):
                        categoria_elegida = elemento[0]
                        print(categoria_elegida)
                        break
        elif flag_pantalla_principal:
            blitear_imagenes(screen, lista_imgs_menu_principal)
            crear_propiedades_botones(screen,lista_textos_menu_principal,lista_botones, fuente, BLANCO,VIOLETA,lista_elementos_interactivos_principal)    
            blitear_objetos_interactivos(screen, lista_botones)
            
            
            
      
    screen.fill((0, 0, 0))

    # Dibujar los botones



    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()
