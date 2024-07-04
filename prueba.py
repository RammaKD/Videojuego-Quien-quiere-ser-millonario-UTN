import pygame
import sys
from elementos import *

pygame.init()
ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

ventana_principal = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Flecha Movible")

flecha_img = pygame.Surface((50, 50))
flecha_img.fill(BLANCO)  # Aquí deberías cargar tu imagen real de la flecha

blitear_flecha = lambda nivel: ventana_principal.blit(flecha_img, (100, ALTO - 50 - nivel * 30))

sep = 70
nivel = 15
while True:
    ventana_principal.fill(NEGRO)  # Limpiar la pantalla

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar la flecha según el nivel actual
    blitear_flecha(nivel)

    # Actualizar pantalla
    pygame.display.flip()