import json
import random
import pygame

def desea_continuar(mensaje:str, mensaje_error: str) -> bool:
    """Pregunta al usuario si quiere continuar con una determinada funcion o no.

    Args:
        mensaje (str): recibe un mensaje si quiere seguir
        mensaje_error (str): recibe un mensaje de error si el usuario no ingresa
        SI / NO

    Returns:
        bool: retorna True si el usuario ingresó SI, y sino False.
    """
    while True:
        try:
            continuar = input(mensaje).lower()
            while continuar != "si" and continuar != "no":
                continuar = input(mensaje_error).lower()
            if continuar == "si":
                retorno = True
                break
            else:
                retorno = False
                break
        except:
            mensaje = mensaje_error
            
    
    return retorno
    
def seleccionar_opcion_menu(mensaje: str) -> int:
    """Permite al usuario ingresar una opcion numérica del menu que quiera.
    Pero si la opcion no se encuentra retorna False 

    Args:
        mensaje (str): recibe una mensaje para seleccionar una opcion

    Returns:
        int|bool: retorna el número en caso de ser en entero, sino False.
    """
    try:
        opciones_menu = int(input(mensaje))
    except:
        opciones_menu = False

    return opciones_menu

def comprobar_len_lista(lista: list) -> bool:
    """Comprueba el largo de una lista, si está vacía o no.

    Args:
        lista (list): recibe una lista

    Returns:
        bool: devuelve False si el largo es 0, sino True
    """
    if len(lista) == 0:
        lenght = False
    else:
        lenght = True
    
    return lenght

def cargar_billetera_json(ruta_archivo_json):
    billetera = True
    try:
        with open(ruta_archivo_json, 'r') as file:
            billetera = json.load(file)["billetera"]
    except:
        billetera = False
    
    return billetera

def actualizar_billetera_json(ruta_archivo_json, puntuacion_actualizada):
    exito = True
    try:
        with open(ruta_archivo_json, "w") as archivo:
            nueva_puntuacion = {"billetera" : puntuacion_actualizada}
            json.dump(nueva_puntuacion, archivo, indent=2)
    except:
        exito = False
    
    return exito

def obtener_paths(ruta_archivo_json):
    with open(ruta_archivo_json, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    diccionario_paths = {}
    
    for clave, valor in data["paths"].items():
        diccionario_paths[clave] = valor
    
    return diccionario_paths
        
def leer_preguntas_csv(ruta_archivo_csv):
    lista_datos_csv = []
    with open(ruta_archivo_csv, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        encabezado = lineas[0].strip().split(',')
        lista_datos_csv.append(encabezado)
        
        valores_preguntas = []
        for linea in lineas[1:]:
            valores_preguntas.append(linea.strip().split(','))
        
        lista_datos_csv.append(valores_preguntas)
    
    return lista_datos_csv

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
    pregunta_aleatoria = random.choice(lista_preguntas)
    return pregunta_aleatoria
           
def crear_lista_respuestas(pregunta):
    lista_respuestas = pregunta["Respuestas"].split("-")
    return lista_respuestas
    
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




















#REVEERLAS#####################################################################
def activar__50_50(respuestas: list, respuesta_correcta: int):
    respuestas_incorrectas = []
    
    for respuesta in respuestas:
        indice = respuestas.index(respuesta)
        if indice != respuesta_correcta:
            respuestas_incorrectas.append(respuesta)
    
    respuesta_incorrecta_mantenida = random.choice(respuestas_incorrectas)
    respuestas_finales = [respuestas[respuesta_correcta], respuesta_incorrecta_mantenida]
    
    
    return respuestas_finales

def activar_ayuda_del_publico(respuestas: list, indice_correcto: int):
    num_respuestas = len(respuestas)
    
    # Probabilidad base para la respuesta correcta (50% a 70%)
    prob_correcta = random.uniform(50, 70)
    
    # Probabilidad restante para distribuir entre las respuestas incorrectas
    prob_restante = 100 - prob_correcta
    
    # Lista para almacenar las probabilidades de las respuestas incorrectas
    prob_incorrectas = [0] * num_respuestas
    
    # Ajustar la probabilidad de la respuesta correcta
    prob_incorrectas[indice_correcto] = prob_correcta
    
    # Calcular el espacio restante para las respuestas incorrectas
    espacio_restante = prob_restante
    
    # Distribuir proporcionalmente el espacio restante entre las respuestas incorrectas
    for i in range(num_respuestas):
        if i != indice_correcto:
            prob_incorrecta = random.uniform(0, espacio_restante)
            prob_incorrectas[i] = prob_incorrecta
            espacio_restante -= prob_incorrecta
    
    # Ajustar cualquier diferencia debido a redondeos
    prob_incorrectas[indice_correcto] += espacio_restante
    
    return prob_incorrectas















