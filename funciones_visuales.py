import pygame
from configuraciones import *

def cargar_imagen(path, dimensiones):
    imagen = pygame.image.load(path)
    imagen = pygame.transform.scale(imagen, dimensiones)
    return imagen

def crear_texto_renderizado(texto, fuente, color, color_fondo):
    texto_renderizado = fuente.render(texto, True, color, color_fondo)
    return texto_renderizado

def blitear_porcentajes(ventana, porcentajes, lista_respuestas, fuente, color_texto, color_fondo):
    y = 125
    for i in range(len(lista_respuestas)):
        respuesta = lista_respuestas[i]
        porcentaje = porcentajes[i]
        texto = f"{respuesta}: {porcentaje}%"
        superficie_texto = crear_texto_renderizado(texto, fuente, color_texto, color_fondo)
        ventana.blit(superficie_texto, (25, y))
        y += 50

def mostrar_pista(ventana_principal, pista, fuente, color_texto, color_fondo):
    superficie_pista = crear_texto_renderizado(pista, fuente, color_texto, color_fondo)
    ventana_principal.blit(superficie_pista, (25, 325))

def actualizar_cronometro(ventana_principal, contador_cronometro, texto_cronometro, fuente, color_texto, color_fondo):
    texto_cronometro = str(contador_cronometro).zfill(2)
    superficie_cronometro = crear_texto_renderizado(texto_cronometro, fuente, color_texto, color_fondo)
    ventana_principal.blit(superficie_cronometro, (25, 40))  

def dibujar_niveles_premios(ventana_principal, piramide_niveles_premios, fuente, color_texto, color_fondo):
    y = 25
    for i in range(len(piramide_niveles_premios) -1, -1, -1):
        nivel_premio = crear_texto_renderizado(piramide_niveles_premios[i][1], fuente, color_texto, color_fondo)
        ventana_principal.blit(nivel_premio, (1100, y))
        y += 40

def blitear_elementos(ventana_principal, lista_botones):
    exito = True
    try:
        for elemento in lista_botones:
            superficie = elemento["superficie"]
            posicion = elemento["posicion"]
            ventana_principal.blit(superficie, posicion)
    except:
        exito = False
    return exito



