
import random
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
    indice_random = random.randint(0, len(lista_preguntas) - 1)
    pregunta_aleatoria = lista_preguntas[indice_random]
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

def generar_porcentajes(lista_respuestas, respuesta_correcta):
    lista_porcentajes = []
    porcentaje_maximo = 100
    porcentaje_respuesta_correcta = random.randint(50, 100)
    porcentaje_restante = porcentaje_maximo - porcentaje_respuesta_correcta
    
    for _ in lista_respuestas:
        lista_porcentajes.append(0)
    
    for i in range(len(lista_respuestas)):
        if lista_respuestas[i] == respuesta_correcta:
            lista_porcentajes[i] = porcentaje_respuesta_correcta
            break
    
    respuestas_incorrectas = len(lista_respuestas) - 1
    porcentaje_asignado = []
    suma_asignados = 0

    if respuestas_incorrectas > 0:
        for _ in range(respuestas_incorrectas):
            asignacion = random.randint(0, porcentaje_restante)
            porcentaje_asignado.append(asignacion)
            suma_asignados += asignacion

        # Ajustamos los valores de los porcentajes asignados
        for i in range(respuestas_incorrectas):
            porcentaje_asignado[i] = int(porcentaje_restante * porcentaje_asignado[i] / suma_asignados)
        
        # Aseguramos que la suma final sea 100 ajustando el último elemento
        suma_porcentaje_asignado = 0
        for valor in porcentaje_asignado:
            suma_porcentaje_asignado += valor
        
        ultimo_indice = len(porcentaje_asignado) - 1
        porcentaje_asignado[ultimo_indice] += porcentaje_restante - suma_porcentaje_asignado

        j = 0
        for i in range(len(lista_respuestas)):
            if lista_respuestas[i] != respuesta_correcta:
                lista_porcentajes[i] = porcentaje_asignado[j]
                j += 1

    return lista_porcentajes

def mostrar_tabla_porcentajes_en_ventana(porcentajes, respuestas, pantalla, fuente, color_texto, color_fondo):
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

def crear_elipse_con_texto(ventana_principal, posicion, color_elipse, color_texto, texto, fuente):
    texto_renderizado = crear_texto_renderizado(texto, fuente, color_texto)
    margen = 10
    ancho_texto = texto_renderizado.get_width() + margen * 2
    alto_texto = texto_renderizado.get_height() + margen * 2
    tamaño_elipse = (ancho_texto, alto_texto)
    elipse_rect = pygame.Rect(posicion, tamaño_elipse)
    
    pygame.draw.ellipse(ventana_principal, color_elipse, elipse_rect)
    texto_rect = texto_renderizado.get_rect(center=elipse_rect.center)
    ventana_principal.blit(texto_renderizado, texto_rect)
    
    return elipse_rect

def usar_comodin_50_50(lista_respuestas, respuesta_correcta):
    respuestas_correctas = [respuesta_correcta]
    respuestas_incorrectas = []

    # Separar respuestas correctas de incorrectas
    for resp in lista_respuestas:
        if resp != respuesta_correcta:
            respuestas_incorrectas.append(resp)

    # Selección manual aleatoria de dos respuestas incorrectas
    respuestas_eliminar = []
    if len(respuestas_incorrectas) > 0:
        indice_1 = random.randint(0, len(respuestas_incorrectas))
        respuestas_eliminar.append(respuestas_incorrectas.pop(indice_1))

        if len(respuestas_incorrectas) > 0:
            indice_2 = random.randint(0, len(respuestas_incorrectas))
            respuestas_eliminar.append(respuestas_incorrectas.pop(indice_2))

    # Reconstruir lista_respuestas con respuestas correctas e incorrectas
    lista_respuestas.clear()
    lista_respuestas.extend(respuestas_correctas + respuestas_incorrectas)

    return respuestas_eliminar


lista_respuestas = ["A", "B", "C", "D"]
respuesta_correcta = "C"

respuestas_eliminadas = usar_comodin_50_50(lista_respuestas, respuesta_correcta)
print("Respuestas eliminadas:", respuestas_eliminadas)
print("Lista actual de respuestas:", lista_respuestas)













