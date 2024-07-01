import pygame

def cargar_imagen(path, dimensiones):
    imagen = pygame.image.load(path)
    imagen = pygame.transform.scale(imagen, dimensiones)
    return imagen

def crear_fuente(fuente, tamaño):
    fuente = pygame.font.SysFont(fuente, tamaño)
    return fuente

def cargar_pantalla(ventana_principal, elementos):
    exito = True
    try:
        for elemento in elementos:
            imagen = elemento[0]
            coordenadas = elemento[1]
            ventana_principal.blit(imagen, coordenadas)
    except:
        exito = False
    
    return exito

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

def dibujar_piramide_premios(ventana, niveles_premios, ANCHO_VENTANA, color_fuente, color_fondo):
    fuente_premios = pygame.font.SysFont("sinsum", 50)
    x_base = ANCHO_VENTANA - 200 
    y_base = 30
    espacio_entre_premios = 40
    
    for i in range(len(niveles_premios)):
        premio = niveles_premios[i][1]
        texto_premio = crear_texto_renderizado(premio, fuente_premios, color_fuente)
        rect_texto_premio = texto_premio.get_rect(left=x_base, top=y_base)
        fondo_premio = crear_fondo_texto(rect_texto_premio, color_fondo)
        ventana.blit(fondo_premio, rect_texto_premio)
        ventana.blit(texto_premio, rect_texto_premio.topleft)
        y_base += espacio_entre_premios

def usar_comodin_publico(pantalla, porcentajes, respuestas, fuente, color_texto, color_fondo):
    x = 150
    y = 150
    ancho_celda = 300
    alto_celda = 50
    
    texto_encabezado = fuente.render("Resp.", False, color_texto)
    texto_porcentaje_encabezado = fuente.render("%", False, color_texto)
    
    pygame.draw.rect(pantalla, color_fondo, (x, y, ancho_celda, alto_celda))
    pantalla.blit(texto_encabezado, (x + 10, y + 10))
    pantalla.blit(texto_porcentaje_encabezado, (x + 180, y + 10))
    y += alto_celda 
    
    for i in range(len(respuestas)):
        pygame.draw.rect(pantalla, color_fondo, (x, y, ancho_celda, alto_celda))
        texto_respuesta = fuente.render(respuestas[i], True, color_texto)
        texto_porcentaje = fuente.render(f"{porcentajes[i]}%", True, color_texto)
        pantalla.blit(texto_respuesta, (x + 10, y + 10))
        pantalla.blit(texto_porcentaje, (x + 180, y + 10))  
        y += alto_celda  







