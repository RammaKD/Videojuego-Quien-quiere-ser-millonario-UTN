from generales_2 import *
from configuraciones import *
from funciones_archivos import *
# from funciones_visuales_2 import *

lista_preguntas = []
diccionario_paths = obtener_paths("archivos\\paths.json")
lista_datos_csv = leer_preguntas_csv(diccionario_paths["path_preguntas"])
crear_diccionario_preguntas(lista_datos_csv, lista_preguntas)

niveles_premios = [
    [1, "$100"],
    [2, "$200"],
    [3, "$300"],
    [4, "$500"],
    [5, "$1000"],
    [6, "$2000"],
    [7, "$4000"],
    [8, "$8000"],
    [9, "$16000"],
    [10, "$32000"],
    [11, "$64000"],
    [12, "$125000"],
    [13, "$250000"],
    [14, "$500000"],
    [15, "$1000000"],
]

logo = cargar_imagen(diccionario_paths["path_logo"], (450,350))
fondo_menu = cargar_imagen(diccionario_paths["path_fondo_menu"], DIMENSIONES_VENTANA)
presentador = cargar_imagen(diccionario_paths["path_presentador"], POS_INICIAL_PRESENTADOR)

# Listas de botones y elementos interactivos
lista_elementos_interactivos_principal = []
lista_elementos_interactivos_categorias = []
lista_elementos_interactivos_juego = []
lista_elementos_interactivos_game_over = []

lista_textos_pantalla_principal = [("JUGAR", (380, 515), True), 
                                   ("SALIR", (750, 515), True)]

lista_textos_pantalla_categorias = [("Eliga una categoria", (450, 365), False),
                                    ("Historia", (250, 500), True),
                                    ("Deportes", (527, 500), True),
                                    ("Ciencia", (800, 500), True),
                                    ("Entretenimiento", (200, 600), True),
                                    ("Geografía", (750, 600), True)]

lista_imgs_pantalla_principal = [(fondo_menu, POS_INICIAL_FONDO),                    
                                 (logo, (450, 75))]

lista_imgs_pantalla_categorias = [(fondo_menu, POS_INICIAL_FONDO),                    
                                  (logo, (450, 0))]

lista_imgs_pantalla_juego = [(fondo_menu, POS_INICIAL_FONDO),                    
                             (presentador, POS_INICIAL_PRESENTADOR)]

lista_imgs_pantalla_game_over = [(fondo_menu, POS_INICIAL_FONDO)]

pygame.init()
ventana_principal = pygame.display.set_mode((DIMENSIONES_VENTANA))
pygame.display.set_caption("Quien quiere ser millonario?")