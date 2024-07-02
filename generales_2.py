import random
from funciones_visuales_2 import *
from elementos_2 import *



#Preguntas y respuestas
def crear_lista_respuestas(pregunta):
    lista_respuestas = pregunta["Respuestas"].split("-")
    return lista_respuestas

def crear_diccionario_preguntas(lista_datos, lista_preguntas):
    for valores in lista_datos[1]:
        pregunta = {}
        for i in range(len(lista_datos[0])):
            pregunta[lista_datos[0][i]] = valores[i]
        lista_preguntas.append(pregunta)
    
    return lista_preguntas

def cargar_posibles_preguntas(lista_preguntas, categoria_elegida, nivel):
    lista_preguntas_posibles = []
    for pregunta in lista_preguntas:
        if pregunta["Categoría"] == categoria_elegida and pregunta["Nivel"] == nivel:
           lista_preguntas_posibles.append(pregunta)

    return lista_preguntas_posibles

def cargar_pregunta_aleatoriamente(lista_preguntas):
    indice_random = random.randint(0, len(lista_preguntas) - 1)
    pregunta_aleatoria = lista_preguntas[indice_random]
    return pregunta_aleatoria

def corroborar_respuesta(respuesta_seleccionada, respuesta_correcta):
    if respuesta_seleccionada == respuesta_correcta:
        retorno = respuesta_seleccionada
    else:
        retorno = False
    
    return retorno 
###########################

def crear_diccionario_botones(lista_botones, texto, surface, rect, posicion, fondo):
    try:
        elemento = {
            "texto": texto,
            "superficie": surface,
            "rectangulo": rect,
            "posicion": posicion,
            "fondo" : fondo
        }
        lista_botones.append(elemento)
    except:
        elemento = False
    
    return elemento
        
def crear_propiedades_botones(lista_textos, fuente, color_texto, color_fondo, lista_elementos_interactivos):
    lista_botones = []
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
        
def cargar_pantalla(pantalla, lista_textos, lista_imgs, fuente, color_texto, color_fondo, lista_elementos_interactivos):
    lista_botones = crear_propiedades_botones(lista_textos, fuente, color_texto, color_fondo, lista_elementos_interactivos)
    blitear_imagenes(pantalla, lista_imgs)
    blitear_objetos_interactivos(pantalla, lista_botones)
    
def cargar_pantalla_game_over(texto, pantalla, lista_imgs_pantalla_game_over, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over):
    lista_textos_pantalla_game_over = [("Haz perdido!", (450, 300), False),
                                       ("Volver al menu principal", (270, 450), True),
                                       (texto, (320, 200), False)]
    cargar_pantalla(pantalla, lista_textos_pantalla_game_over, lista_imgs_pantalla_game_over, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA, lista_elementos_interactivos_game_over)
                
def resetear_juego(m, nivel, lista_elementos_interactivos, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, contador_cronometro):
    contador_cronometro = 5
    m = 0
    nivel = str(niveles_premios[m][0])
    lista_elementos_interactivos.clear()
    flag_pantalla_juego = False
    flag_pantalla_principal = True
    flag_pregunta_mostrada = False
    flag_cronometro_activo = False
    return m, nivel, lista_elementos_interactivos, flag_pantalla_juego, flag_pantalla_principal, flag_pregunta_mostrada, flag_cronometro_activo, contador_cronometro                    

def cargar_elementos_pantalla_juego(lista_preguntas, categoria_elegida, nivel, flag_pregunta_mostrada, fuente, color_texto, color_fondo):
    lista_posibles_preguntas = cargar_posibles_preguntas(lista_preguntas, categoria_elegida, nivel)
    pregunta_cargada = cargar_pregunta_aleatoriamente(lista_posibles_preguntas)
    lista_respuestas = crear_lista_respuestas(pregunta_cargada)
    respuesta_correcta = pregunta_cargada["Respuesta_correcta"]
    
    lista_textos_pantalla_juego = [(pregunta_cargada["Pregunta"], (25, 425), False),
                                    (lista_respuestas[0], (25, 550), True),
                                    (lista_respuestas[1], (450, 550), True),
                                    (lista_respuestas[2], (25, 650), True),
                                    (lista_respuestas[3], (450, 650), True),
                                    (f"50-50", (150,55), True),
                                    (f"Publico", (275,55), True),
                                    (f"Llamada", (440,55), True)]
    
    flag_pregunta_mostrada = True
    cargar_pantalla(ventana_principal, lista_textos_pantalla_juego, lista_imgs_pantalla_juego, fuente, color_texto, color_fondo, lista_elementos_interactivos_juego)
    dibujar_niveles_premios(ventana_principal, niveles_premios)
    return flag_pregunta_mostrada, respuesta_correcta

lista_preguntas = []
diccionario_paths = obtener_paths("archivos\\paths.json")
lista_datos_csv = leer_preguntas_csv(diccionario_paths["path_preguntas"])
crear_diccionario_preguntas(lista_datos_csv, lista_preguntas)