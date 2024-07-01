
import random
import random
from funciones_visuales import *

#Funciones generales
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

#Funciones preguntas/respuestas
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

def crear_lista_respuestas(pregunta):
    lista_respuestas = pregunta["Respuestas"].split("-")
    return lista_respuestas

def corroborar_respuesta(respuesta_seleccionada, respuesta_correcta):
    if respuesta_seleccionada == respuesta_correcta:
        retorno = True
    else:
        retorno = False
    
    return retorno

def manejar_respuesta_correcta(m, contador_nivel, niveles_premios, CRONOMETRO):
    m += 1
    contador_nivel = niveles_premios[m][0]
    flag_pregunta_mostrada = False
    flag_respuesta_seleccionada = False
    contador_cronometro = 10
    texto_cronometro = str(contador_cronometro).zfill(2)
    pygame.time.set_timer(CRONOMETRO, 1000)
    return m, contador_nivel, flag_pregunta_mostrada, flag_respuesta_seleccionada, contador_cronometro, texto_cronometro

def manejar_respuesta_incorrecta(niveles_premios):
    flag_pantalla_juego = False
    flag_pregunta_mostrada = False
    flag_respuesta_seleccionada = False
    flag_pantalla_principal = True
    flag_cronometro_activo = False
    flag_comodin_50_50_usado = False
    flag_boton_salir = True
    m = 0
    contador_nivel = niveles_premios[m][0]
    return flag_pantalla_juego, flag_pregunta_mostrada, flag_respuesta_seleccionada, flag_pantalla_principal, flag_cronometro_activo, flag_comodin_50_50_usado, flag_boton_salir, m, contador_nivel

#Funciones listas
def listar_rects(lista_elementos):
    lista_rects = []
    for i in range(len(lista_elementos)):
        elemento = lista_elementos[i][0]
        posicion = lista_elementos[i][1]
        rect_texto = crear_rect_texto(elemento, posicion)
        lista_rects.append(rect_texto)
    return lista_rects

def listar_renders(lista_textos_y_pos,fuente,color):
    lista_renders = []
    for elemento in lista_textos_y_pos:
        texto = elemento[0]
        texto_renderizado = crear_texto_renderizado(texto,fuente,color)
        lista_renders.append((texto_renderizado, elemento[1]))
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
        posicion = lista_textos[i][1]
        elemento_1 = lista_fondos[i],(lista_rects[i])
        elemento_2 = lista_textos[i][0],posicion
        lista_elementos.append(elemento_1)
        lista_elementos.append(elemento_2)
        

    return lista_elementos

#Funciones lógica comodines
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
        for i in range(respuestas_incorrectas):
            porcentaje_asignado[i] = int(porcentaje_restante * porcentaje_asignado[i] / suma_asignados)
        
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

def aplicar_comodin_5050(lista_respuestas_y_pos, respuesta_correcta):
    """Aplica el comodín 50:50 seleccionando una respuesta incorrecta aleatoria junto con la correcta."""
    incorrectas = []
    for i in range(len(lista_respuestas_y_pos)):
        if lista_respuestas_y_pos[i][0] != respuesta_correcta:
            incorrectas.append(lista_respuestas_y_pos[i])
               
    indice_incorrecta = random.randint(0, len(incorrectas) - 1)
    respuesta_incorrecta = incorrectas[indice_incorrecta]
    
    for respuesta in lista_respuestas_y_pos[:]:
        if respuesta[0] != respuesta_correcta and respuesta != respuesta_incorrecta:
            lista_respuestas_y_pos.remove(respuesta)

    return lista_respuestas_y_pos






def actualizar_cronometro_pantalla_juego(ventana_principal, lista_elementos_pantalla_jugando, niveles_premios, ANCHO_VENTANA, texto_cronometro, fuente, color_texto, color_fondo):
    cargar_pantalla(ventana_principal, lista_elementos_pantalla_jugando)
    dibujar_piramide_premios(ventana_principal, niveles_premios, ANCHO_VENTANA, color_texto, color_fondo)
    
    texto_cronometro_render, rect_texto_cronometro, fondo_texto_cronometro = crear_texto_cronometro(texto_cronometro, fuente, color_texto, color_fondo)
    ventana_principal.blit(fondo_texto_cronometro, rect_texto_cronometro.topleft)
    ventana_principal.blit(texto_cronometro_render, rect_texto_cronometro.topleft)

def crear_texto_cronometro(texto_cronometro, fuente, color_texto, color_fondo):
    texto_cronometro_render = crear_texto_renderizado(texto_cronometro, fuente, color_texto)
    rect_texto_cronometro = crear_rect_texto(texto_cronometro_render, (25, 50))
    fondo_texto_cronometro = crear_fondo_texto(rect_texto_cronometro, color_fondo)
    return texto_cronometro_render, rect_texto_cronometro, fondo_texto_cronometro

    
    







































