import pygame
from configuraciones import *

def cargar_imagen(path, dimensiones):
    imagen = pygame.image.load(path)
    imagen = pygame.transform.scale(imagen, dimensiones)
    return imagen

def crear_fuente(fuente, tamaño):
    fuente = pygame.font.SysFont(fuente, tamaño)
    return fuente

def crear_texto_renderizado(texto, fuente, color):
    texto_renderizado = fuente.render(texto, True, color)
    return texto_renderizado

def crear_fondo_texto(rect_texto, color_fondo):
    fondo_surface = pygame.Surface((rect_texto.width, rect_texto.height))
    fondo_surface.fill(color_fondo)
    return fondo_surface

def crear_rect_texto(texto_renderizado, posicion):
    rect_texto = texto_renderizado.get_rect()
    rect_texto.topleft = posicion
    return rect_texto

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

def crear_fondo_texto(rect_texto, color_fondo):
    fondo_surface = pygame.Surface((rect_texto.width, rect_texto.height))
    fondo_surface.fill(color_fondo)
    return fondo_surface

def crear_texto_renderizado(texto, fuente, color):
    texto_renderizado = fuente.render(texto, True, color)
    return texto_renderizado

def dibujar_niveles_premios(ventana_principal, piramide_niveles_premios, fuente, color_texto, color_fondo):
    y = 15
    for i in range(len(piramide_niveles_premios)):
        nivel_premio = crear_texto_renderizado(piramide_niveles_premios[i][1], fuente, color_texto)
        rect_nivel_premio = crear_rect_texto(nivel_premio, (1100, y))
        fondo_nivel_premio = crear_fondo_texto(rect_nivel_premio, color_fondo)
        ventana_principal.blit(fondo_nivel_premio, (1100, y))
        ventana_principal.blit(nivel_premio, (1100, y))
        y += 45
        
def actualizar_cronometro(ventana_principal, contador_cronometro, texto_cronometro, fuente, color_texto, color_fondo, pos_cronometro, flag_pantalla_game_over, flag_boton_pantalla_game_over):
    if contador_cronometro > 0:
        texto_cronometro_render = crear_texto_renderizado(texto_cronometro, fuente, color_texto)
        rect_cronometro = crear_rect_texto(texto_cronometro_render, (25, 40))
        fondo_cronometro = crear_fondo_texto(rect_cronometro, color_fondo)
        ventana_principal.blit(fondo_cronometro, pos_cronometro)
        ventana_principal.blit(texto_cronometro_render, pos_cronometro)
    else:
        flag_pantalla_game_over = True
        flag_boton_pantalla_game_over = True
    
    return flag_pantalla_game_over, flag_boton_pantalla_game_over









