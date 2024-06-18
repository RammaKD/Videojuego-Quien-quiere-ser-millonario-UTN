import csv
import json
import re
import random

lista_preguntas_historia = []
lista_preguntas_ciencia = []
lista_preguntas_geografia = []
lista_preguntas_deporte = []
lista_preguntas_entretenimiento = []

lista_preguntas_tocadas = []

piramide_premios =  [
    ["Muy fácil", 100],
    ["Muy fácil", 200],
    ["Fácil", 300],
    ["Fácil", 500],
    ["Fácil", 1000],
    ["Medio", 2000],
    ["Medio", 4000],
    ["Medio", 8000],
    ["Medio", 16000],
    ["Medio", 32000],
    ["Dificil", 64000],
    ["Dificil", 125000],
    ["Dificil", 250000],
    ["Muy dificil", 500000],
    ["Muy dificil", 1000000]
]

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

def leer_preguntas_desde_csv(lista_preguntas_historia, lista_preguntas_ciencia, lista_preguntas_geografia,
                             lista_preguntas_deporte,  lista_preguntas_entretenimiento, archivo_csv):
    exito = True
    try:
        with open(archivo_csv, "r", encoding="utf8") as archivo:
            for linea in archivo:
                registro = re.split(",|\n", linea)
                
                if registro[0] != "id":
                    diccionario = crear_pregunta(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                    match diccionario["categoria"]:
                        case "Historia":
                            lista_preguntas_historia.append(diccionario)
                        case "Ciencia":
                            lista_preguntas_ciencia.append(diccionario)
                        case "Geografía":
                            lista_preguntas_geografia.append(diccionario)
                        case "Deporte":
                            lista_preguntas_deporte.append(diccionario)
                        case "Entretenimiento":
                            lista_preguntas_entretenimiento.append(diccionario)
    except:
        exito = False

    return exito

def cargar_puntuaciones_json(archivo_json):
    with open(archivo_json, 'r') as file:
        puntuaciones = json.load(file)["premio"]
    return puntuaciones

def cargar_paths(archivo_data):
    with open(archivo_data, "r") as file:
        diccionario_paths = json.load(file)
        for path in diccionario_paths:
            archivo_preguntas = diccionario_paths[path]["path_preguntas"]
            archivo_premios = diccionario_paths[path]["path_premios"]
        lista_paths = [archivo_preguntas, archivo_premios]
        
    return lista_paths
        
def crear_pregunta(id: int, categoria: str, dificultad: str, pregunta: str, respuestas: dict, respuesta_correcta: str, palabra_clave: str) -> dict:
    diccionario_pregunta = {
        "id" : int(id),
        "categoria" : categoria,
        "dificultad" : dificultad,
        "pregunta" : pregunta,
        "respuestas" : respuestas,
        "respuesta_correcta" : int(respuesta_correcta),
        "palabra_clave" : palabra_clave
        }
    
    return diccionario_pregunta

def mostrar_pregunta(lista_preguntas, id_pregunta):
    try:
        for pregunta in lista_preguntas:
            if pregunta["id"] == id_pregunta:
                print(pregunta["pregunta"])
                print(pregunta["respuestas"])
                retorno = pregunta
                break
    except:
        retorno = False

    return retorno

def elegir_pregunta_random(nivel: int, lista_preguntas_tocadas: list):
    try:
        match nivel:
            case "Muy fácil":
                while True:
                    id_random = random.randint(1,3)
                    if id_random not in lista_preguntas_tocadas:
                        id_retorno = id_random
                        break
            case "Fácil":
                while True:
                    id_random = random.randint(4,5)
                    if id_random not in lista_preguntas_tocadas:
                        id_retorno = id_random
                        break
    except:
        id_retorno = False
    return id_retorno

def realizar_50_50(respuestas: list, respuesta_correcta: int):
    respuestas_incorrectas = []
    
    for respuesta in respuestas:
        indice = respuestas.index(respuesta)
        if indice != respuesta_correcta:
            respuestas_incorrectas.append(respuesta)
    
    respuesta_incorrecta_mantenida = random.choice(respuestas_incorrectas)
    respuestas_finales = [respuestas[respuesta_correcta], respuesta_incorrecta_mantenida]
    
    
    return respuestas_finales

def ayuda_del_publico(respuestas: list, indice_correcto: int):
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

def llamada(pregunta_tocada):
    palabra_clave = pregunta_tocada["palabra_clave"]
    print(f"-{palabra_clave}-")
    return palabra_clave

leer_preguntas_desde_csv(lista_preguntas_historia, lista_preguntas_ciencia, lista_preguntas_geografia,
                         lista_preguntas_deporte,  lista_preguntas_entretenimiento, cargar_paths("paths.json")[0])
bandera_50_50 = True
bandera_publico = True
bandera_llamada = True
m = 0


while True:
    nivel = piramide_premios[m][0]
    id_pregunta = elegir_pregunta_random(nivel, lista_preguntas_tocadas)
    pregunta_tocada = mostrar_pregunta(lista_preguntas_historia, id_pregunta)
    respuestas = pregunta_tocada["respuestas"].split("-")
    respuesta_correcta = pregunta_tocada["respuesta_correcta"]
    
    
    seguir_comodines = True
    while seguir_comodines:
        print("1. 50-50%")
        print("2. Público")
        print("3. Amigo")
        print("4. Salir")
        comodin = seleccionar_opcion_menu("Selecciones una opción: ")
        
        match comodin:
            case 1:
                if bandera_50_50:
                    print(realizar_50_50(respuestas, respuesta_correcta))
                    bandera_50_50 = False
                else:
                    print("No tiene mas el comodín 50-50%")
            case 2:
                if bandera_publico:
                    print(ayuda_del_publico(respuestas, respuesta_correcta))
                    bandera_publico = False
                else:
                    print("No tiene mas el comodín del público")
            case 3:
                if bandera_llamada:
                    llamada(pregunta_tocada)
                    bandera_llamada = False
                else:
                    print("No tiene mas el comodín de llamada")
            case 4:
                if desea_continuar("Seguro que no quiere uitilizar comodines? SI/NO: ", "Error. Ingrese SI/NO: "):
                    seguir_comodines = False
            case _:
                print("Elija una opción válida.")

    opcion_elegida = seleccionar_opcion_menu("Seleccione una opción, 1-2-3-4: ") - 1
    if opcion_elegida == pregunta_tocada["respuesta_correcta"]:
        m += 1
        lista_preguntas_tocadas.append(pregunta_tocada["id"])
        print("Respuesta correcta.")
    else:
        print("Respuesta incorrecta, ha perdido.")
        break