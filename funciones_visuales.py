import pygame
from configuraciones import *

def cargar_imagen(path, dimensiones):
    """
    Carga una imagen desde el path especificado y la escala a las dimensiones dadas.
    Retorna la imagen cargada y escalada.
    """
    imagen = pygame.image.load(path)
    imagen = pygame.transform.scale(imagen, dimensiones)
    return imagen

def crear_texto_renderizado(texto, fuente, color, color_fondo):
    """
    Crea y retorna texto renderizado con la fuente, color de texto y color de fondo especificados.
    """
    texto_renderizado = fuente.render(texto, True, color, color_fondo)
    return texto_renderizado

def blitear_porcentajes(ventana, porcentajes, lista_respuestas, fuente, color_texto, color_fondo):
    """
    Muestra porcentajes de respuestas en la ventana dada.

    Parámetros:
    ventana (pygame.Surface): Ventana donde se muestran los porcentajes.
    porcentajes (list): Lista de porcentajes por respuesta.
    lista_respuestas (list): Lista de respuestas correspondientes.
    fuente (pygame.font.Font): Fuente para el texto.
    color_texto (tuple): Color del texto (RGB).
    color_fondo (tuple): Color de fondo (RGB).
    """
    y = 125
    for i in range(len(lista_respuestas)):
        respuesta = lista_respuestas[i]
        porcentaje = porcentajes[i]
        texto = f"{respuesta}: {porcentaje}%"
        superficie_texto = crear_texto_renderizado(texto, fuente, color_texto, color_fondo)
        ventana.blit(superficie_texto, (25, y))
        y += 50

def mostrar_pista(ventana_principal, pista, fuente, color_texto, color_fondo):
    """
    Muestra una pista en la ventana principal.

    Parámetros:
    ventana_principal (pygame.Surface): Ventana donde se muestra la pista.
    pista (str): Texto de la pista a mostrar.
    """
    superficie_pista = crear_texto_renderizado(pista, fuente, color_texto, color_fondo)
    ventana_principal.blit(superficie_pista, (25, 325))

def actualizar_cronometro(ventana_principal, dict_cronometro):
    """
    Actualiza y muestra el contador de cronómetro en la ventana principal.

    Parámetros:
    ventana_principal (pygame.Surface): Ventana donde se muestra el cronómetro.
    contador_cronometro (int): Valor actual del cronómetro.
    texto_cronometro (str): Texto formateado del cronómetro.
    """
    retorno = True
    fuente = dict_cronometro["fuente"][0]
    color_texto = dict_cronometro["fuente"][1]
    color_fondo = dict_cronometro["fuente"][2]
    
    if dict_cronometro["contador"] < 10 and dict_cronometro["contador"] > 0:
        color_texto = dict_cronometro["fuente"][3]
    elif dict_cronometro["contador"] <= 0:
        retorno = False
    
    texto_cronometro = str(dict_cronometro["contador"]).zfill(2)
    superficie_cronometro = crear_texto_renderizado(texto_cronometro, fuente, color_texto, color_fondo)
    ventana_principal.blit(superficie_cronometro, (25, 40))
    dict_cronometro["contador"] -= 1
    
    return retorno
    

def dibujar_niveles_premios(ventana_principal, dict_niveles_premios):
    """
    Dibuja niveles de premios en una pirámide invertida en la ventana.

    Parámetros:
    ventana_principal (pygame.Surface): Ventana de visualización.
    piramide_niveles_premios (list): Lista de niveles de premios en forma de pirámide invertida.
    """
    y = 25
    fuente = dict_niveles_premios["fuente"][0]
    color_texto = dict_niveles_premios["fuente"][1]
    color_fondo = dict_niveles_premios["fuente"][2]
    for i in range(len(dict_niveles_premios["piramide"]) -1, -1, -1):
        nivel_premio = crear_texto_renderizado(dict_niveles_premios["piramide"][i][1], fuente, color_texto, color_fondo)
        ventana_principal.blit(nivel_premio, (1100, y))
        y += 40

def blitear_elementos(ventana_principal, lista_botones):
    """
    Blitea elementos en la ventana principal.

    Parámetros:
    ventana_principal (pygame.Surface): Ventana donde se blitean los elementos.
    lista_botones (list): Lista de diccionarios con superficies y posiciones.
    """
    exito = True
    try:
        for elemento in lista_botones:
            superficie = elemento["superficie"]
            posicion = elemento["posicion"]
            ventana_principal.blit(superficie, posicion)
    except:
        exito = False
    
    return exito


def blitear_texto_nombre(texto_input_box, texto_surface, input_box_premio, ventana_principal):
    """
    Renderiza y dibuja un cuadro de texto en la pantalla principal. 
    El texto se muestra dentro de un rectángulo ubicado en una posición específica.
    También se dibuja un borde blanco alrededor del rectángulo.
    """
    input_box_premio = pygame.Rect(250, 450, 750, 65)
    texto_surface = crear_texto_renderizado(texto_input_box, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA)
    ventana_principal.blit(texto_surface, (input_box_premio.x, input_box_premio.y))
    pygame.draw.rect(ventana_principal, BLANCO, input_box_premio, 2)


