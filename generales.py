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

def listar_rects(lista_elementos, lista_posiciones):
    lista_rects = []
    for i in range(len(lista_elementos)):
        elemento = lista_elementos[i]
        posicion = lista_posiciones[i]
        rect_texto = crear_rect_texto(elemento, posicion)
        lista_rects.append(rect_texto)
    return lista_rects

def listar_renders(lista_textos,fuente,color):
    lista_renders = []
    for textos in lista_textos:
        texto_renderizado = crear_texto_renderizado(textos,fuente,color)
        lista_renders.append(texto_renderizado)
    return lista_renders

def listar_fondos(lista_rects, color_fondo):
    lista_fondos = []
    for rect in lista_rects:
        fondo_texto = crear_fondo_texto(rect, color_fondo)
        lista_fondos.append(fondo_texto)
    return lista_fondos

def generar_lista_elementos(lista_textos, lista_rects, lista_fondos):
    lista_elementos = []
    for i in range(len(lista_textos)):
        posicion = lista_rects[i].topleft
        elemento_1 = lista_fondos[i],(lista_rects[i])
        elemento_2 = lista_textos[i],posicion
        lista_elementos.append(elemento_1)
        lista_elementos.append(elemento_2)
        

    return lista_elementos

def dividir_pregunta(pregunta, limite=75):
    if len(pregunta) <= limite:
        return [pregunta]

    corte = limite
    for i in range(limite, 0, -1):
        if pregunta[i] == ' ':
            corte = i
            break
    primera_parte = pregunta[:corte].rstrip()
    segunda_parte = pregunta[corte:].lstrip()

    return [primera_parte, segunda_parte]














