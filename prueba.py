import pygame
import random

# Inicialización de Pygame
pygame.init()

# Funciones de creación de elementos

def crear_texto_renderizado(texto, fuente, color):
    """ Crea y devuelve un texto renderizado con la fuente y color dados. """
    texto_renderizado = fuente.render(texto, True, color)
    return texto_renderizado

def aplicar_comodin_5050(dict_respuestas_y_pos, respuesta_correcta):
    """ Aplica el comodín 50:50 seleccionando una respuesta incorrecta aleatoria junto con la correcta. """
    respuestas = []
    claves_respuestas = []

    # Extraer respuestas y sus claves del diccionario
    for clave, valor in dict_respuestas_y_pos.items():
        respuestas.append(valor[0])
        claves_respuestas.append(clave)
    
    # Crear una lista de respuestas incorrectas y sus claves
    incorrectas = []
    claves_incorrectas = []

    for i in range(len(respuestas)):
        if respuestas[i] != respuesta_correcta:
            incorrectas.append(respuestas[i])
            claves_incorrectas.append(claves_respuestas[i])
    
    # Seleccionar una respuesta incorrecta aleatoriamente
    indice_incorrecta = random.randint(0, len(incorrectas) - 1)
    respuesta_incorrecta = incorrectas[indice_incorrecta]
    clave_incorrecta = claves_incorrectas[indice_incorrecta]

    # Crear el nuevo diccionario con solo la respuesta correcta y una incorrecta aleatoria
    nuevo_dict_respuestas_y_pos = {}
    for clave, valor in dict_respuestas_y_pos.items():
        if valor[0] == respuesta_correcta:
            nuevo_dict_respuestas_y_pos[clave] = valor
        elif valor[0] == respuesta_incorrecta:
            nuevo_dict_respuestas_y_pos[clave] = valor

    return nuevo_dict_respuestas_y_pos

def crear_fuente(fuente, tamaño):
    """ Crea y devuelve una fuente de Pygame con el tipo y tamaño especificados. """
    fuente = pygame.font.SysFont(fuente, tamaño)
    return fuente

# Configuración de la ventana y variables globales

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Ejemplo de Juego con Comodín 50:50')

FUENTE_PANTALLA_JUEGO = crear_fuente("Arial", 35)
BLANCO = (255, 255, 255)

# Datos de prueba
texto_pregunta_corte_1 = "¿Cuántos años tenés?"
dict_textos_y_pos_preguntas = {
    "posicion_pregunta_a": (texto_pregunta_corte_1, (25, 425))
}

dict_respuestas_y_pos = {
    "posicion_respuesta_a": ("París", (25, 50)),
    "posicion_respuesta_b": ("Londres", (450, 50)),
    "posicion_respuesta_c": ("Madrid", (25, 150)),
    "posicion_respuesta_d": ("Berlín", (450, 150))
}
respuesta_correcta = "Madrid"

# Función para listar renders y rects y devolver una lista para blitear luego
def listar_renders_pos(ventana, dict_textos_pos, fuente, color):
    """ Lista los renders y rects de texto y los devuelve en una lista para blitear después. """
    renders_y_rects = []
    for key in dict_textos_pos:
        texto = dict_textos_pos[key][0]
        posicion = dict_textos_pos[key][1]
        texto_renderizado = crear_texto_renderizado(texto, fuente, color)
        renders_y_rects.append((texto_renderizado, posicion))
        
    return renders_y_rects

# Listar renders y rects de preguntas y respuestas
lista_renders_rects_preguntas = listar_renders_pos(ventana, dict_textos_y_pos_preguntas, FUENTE_PANTALLA_JUEGO, BLANCO)
lista_renders_rects_respuestas = listar_renders_pos(ventana, dict_respuestas_y_pos, FUENTE_PANTALLA_JUEGO, BLANCO)

# Aplicar comodín 50:50 a las respuestas
dict_respuestas_y_pos = aplicar_comodin_5050(dict_respuestas_y_pos, respuesta_correcta)
lista_renders_rects_respuestas_actualizadas = listar_renders_pos(ventana, dict_respuestas_y_pos, FUENTE_PANTALLA_JUEGO, BLANCO)

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # Dibujar elementos en la ventana
    ventana.fill((0, 0, 0))  # Limpiar pantalla con color negro
    
    # Blitear renders de preguntas
    for render, posicion in lista_renders_rects_preguntas:
        ventana.blit(render, posicion)
    
    # Blitear renders de respuestas actualizadas
    for render, posicion in lista_renders_rects_respuestas_actualizadas:
        ventana.blit(render, posicion)

    # Actualizar pantalla una sola vez por ciclo
    pygame.display.flip()

# Salir del juego
pygame.quit()
