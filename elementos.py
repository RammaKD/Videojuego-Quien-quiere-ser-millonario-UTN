from generales import *
from configuraciones import *
from funciones_visuales import *
from funciones_archivos import *

lista_preguntas = []
lista_elementos_menu_principal_inicial = []
lista_elementos_menu_categorias_inicial = []

lista_categorias = ["Historia", "Deporte", "Ciencia", "Entretenimiento", "Geografía"]
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

#Banderas
flag_run = True
flag_pantalla_principal = True
flag_pantalla_categorias = False
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

#Imágenes
logo = cargar_imagen(diccionario_paths["path_logo"], (450,350))
fondo_menu = cargar_imagen(diccionario_paths["path_fondo_menu"], DIMENSIONES_VENTANA)
presentador = cargar_imagen(diccionario_paths["path_presentador"], POS_INCIAL_PRESENTADOR)

#Listas imágenes por pantalla 
lista_imgs_menu_principal = [(fondo_menu, POS_INICIAL_FONDO), (logo, (450,75))]
lista_imgs_menu_categorias = [(fondo_menu, POS_INICIAL_FONDO), (logo, (450,50))]
lista_imgs_jugando = [(fondo_menu, POS_INICIAL_FONDO), (presentador, (650,250))]

#Listas textos y posiciones
lista_textos_y_pos_menu = [("JUGAR", (380, 515)), ("SALIR", (750, 515))]

lista_textos_y_pos_menu_categorias = [
    ("Elija la categoria", (450, 365)),
    ("HISTORIA", (250, 500)),
    ("DEPORTE", (527, 500)),
    ("CIENCIA", (800, 500)),
    ("ENTRETENIMIENTO", (200, 600)),
    ("GEOGRAFÍA", (750, 600))
]

#Listas iniciales
lista_elementos_menu_principal_inicial += lista_imgs_menu_principal 
lista_elementos_menu_categorias_inicial += lista_imgs_menu_principal

#Listas renderizadas
lista_renders_menu = listar_renders(lista_textos_y_pos_menu, FUENTE_PRINCIPAL, BLANCO)
lista_renders_categorias = listar_renders(lista_textos_y_pos_menu_categorias, FUENTE_PRINCIPAL, BLANCO)

#Listas rectángulos
lista_rects_menu = listar_rects(lista_renders_menu)
lista_rects_categorias = listar_rects(lista_renders_categorias)

#Listas fondos
lista_fondos_menu = listar_fondos(lista_rects_menu, VIOLETA)
lista_fondos_categorias = listar_fondos(lista_rects_categorias, VIOLETA)

#Listas elementos interactivos con el usuario
lista_elementos_menu_interactivos = generar_lista_elementos(lista_renders_menu, lista_rects_menu, lista_fondos_menu)
lista_elementos_menu_categorias_interactivos = generar_lista_elementos(lista_renders_categorias, lista_rects_categorias, lista_fondos_categorias)

#Listas elementos finales de cada pantalla
lista_elementos_menu = lista_elementos_menu_principal_inicial + lista_elementos_menu_interactivos
lista_elementos_menu_categorias = lista_elementos_menu_categorias_inicial + lista_elementos_menu_categorias_interactivos

def cargar_elementos_pantalla_jugando(categoria_elegida, nivel):
    lista_posibles_preguntas = cargar_posibles_preguntas(lista_preguntas, categoria_elegida, nivel)
    pregunta_cargada = cargar_pregunta_aleatoriamente(lista_posibles_preguntas)
    pregunta_dividida = dividir_pregunta(pregunta_cargada["Pregunta"])
    lista_respuestas = crear_lista_respuestas(pregunta_cargada)
    respuesta_correcta = pregunta_cargada["Respuesta_correcta"]
    
    if len(pregunta_dividida) == 1:
        texto_pregunta_corte_1 = pregunta_dividida[0]
        texto_pregunta_corte_2 = ""
    else:
        texto_pregunta_corte_1 = pregunta_dividida[0]
        texto_pregunta_corte_2 = pregunta_dividida[1]
    
    lista_elementos_pantalla_jugando_inicial = []
    lista_textos_juego = [(texto_pregunta_corte_1, POS_PREG_CORTE_1), 
                          (texto_pregunta_corte_2, POS_PREG_CORTE_2)]
    lista_textos_respuestas = [(lista_respuestas[0], POS_RESP_A), 
                               (lista_respuestas[1], POS_RESP_B), 
                               (lista_respuestas[2], POS_RESP_C), 
                               (lista_respuestas[3], POS_RESP_D)]
    
    # if not flag_comodin_50_50_usado:
    #     lista_textos_respuestas = aplicar_comodin_5050(lista_textos_respuestas, respuesta_correcta)

        
    lista_textos_pantalla_jugando = lista_textos_juego + lista_textos_respuestas
    lista_elementos_pantalla_jugando_inicial += lista_imgs_jugando
    
    lista_renders_jugando = listar_renders(lista_textos_pantalla_jugando, FUENTE_PANTALLA_JUEGO, BLANCO)
    lista_rects_jugando = listar_rects(lista_renders_jugando)
    lista_fondos_jugando = listar_fondos(lista_rects_jugando, VIOLETA)

    lista_elementos_jugando_interactivos = generar_lista_elementos(lista_renders_jugando, lista_rects_jugando, lista_fondos_jugando)
    lista_elementos_pantalla_jugando = lista_elementos_pantalla_jugando_inicial + lista_elementos_jugando_interactivos

    return lista_elementos_pantalla_jugando, lista_rects_jugando, lista_respuestas, respuesta_correcta

def cargar_elementos_pantalla_retirarse(ventana_principal):
    ventana_principal.blit(fondo_menu, POS_INICIAL_FONDO)

    # Texto de la pregunta
    fuente = pygame.font.Font(None, 74)
    texto = fuente.render("¿Deseas retirarte?", True, BLANCO)
    texto_rect = texto.get_rect(center=(DIMENSIONES_VENTANA[0] // 2, DIMENSIONES_VENTANA[1] // 4))
    ventana_principal.blit(texto, texto_rect)

    # Botón continuar
    texto_continuar = fuente.render("Continuar", True, BLANCO)
    rect_continuar = texto_continuar.get_rect(center=(DIMENSIONES_VENTANA[0] // 2, DIMENSIONES_VENTANA[1] // 2))
    ventana_principal.blit(texto_continuar, rect_continuar)

    # Botón retirarse
    texto_retirarse = fuente.render("Retirarse", True, BLANCO)
    rect_retirarse = texto_retirarse.get_rect(center=(DIMENSIONES_VENTANA[0] // 2, 3 * DIMENSIONES_VENTANA[1] // 4))
    ventana_principal.blit(texto_retirarse, rect_retirarse)

    return rect_continuar, rect_retirarse











