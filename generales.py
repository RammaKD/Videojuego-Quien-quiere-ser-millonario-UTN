import csv
import json
import re
import random

lista_preguntas = []

lista_preguntas_tocadas = []

piramide_premios =  [
    [1, 100, False],
    [2, 200, False],
    [3, 300, False],
    [4, 500, False],
    [5, 1000, False],
    [6, 2000, False],
    [7, 4000, False],
    [8, 8000, False],
    [9, 16000, False],
    [10, 32000, False],
    [11, 64000, False],
    [12, 125000, False],
    [13, 250000, False],
    [14, 500000, False],
    [15, 1000000, False]
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

def leer_preguntas_desde_csv(lista, archivo_csv):
    exito = True
    try:
        with open(archivo_csv, "r", encoding="utf8") as archivo:
            for linea in archivo:
                registro = re.split(",|\n", linea)
                
                if registro[0] != "id":
                    diccionario = crear_pregunta(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                    lista.append(diccionario)
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
        
def crear_pregunta(id: int, categoria: str, dificultad: str, pregunta: str, respuestas: dict, respuesta_correcta: str) -> dict:
    diccionario_pregunta = {
        "id" : int(id),
        "categoria" : categoria,
        "dificultad" : dificultad,
        "pregunta" : pregunta,
        "respuestas" : respuestas,
        "respuesta_correcta" : int(respuesta_correcta),
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

def llamar_amigo(pregunta_tocada, respuestas):
    respuesta_dada = pregunta_tocada["respuesta_correcta"]
    print(respuestas[respuesta_dada])
    return respuesta_dada

leer_preguntas_desde_csv(lista_preguntas, cargar_paths("paths.json")[0])

while True:
    id_pregunta = elegir_pregunta_random("Muy fácil", lista_preguntas_tocadas)
    #print(id_pregunta)
    pregunta_tocada = mostrar_pregunta(lista_preguntas, id_pregunta)
    respuestas = pregunta_tocada["respuestas"].split("-")
    respuesta_correcta = pregunta_tocada["respuesta_correcta"]
    print("1. 50-50%")
    print("2. Público")
    print("3. Amigo")
    print("4. Salir")
    comodin = seleccionar_opcion_menu("Selecciones una opción: ")
    match comodin:
        case 1:
            print(realizar_50_50(respuestas, respuesta_correcta))
        case 2:
            print(ayuda_del_publico(respuestas, respuesta_correcta))
        case 3:
            llamar_amigo(pregunta_tocada, respuestas)
        case 4:
            pass
        case _:
            print("Elija una opción válida.")

    opcion_elegida = seleccionar_opcion_menu("Seleccione una opción, 1-2-3-4: ") - 1
    if opcion_elegida == pregunta_tocada["respuesta_correcta"]:
        piramide_premios[0][2] = True
        lista_preguntas_tocadas.append(pregunta_tocada["id"])
        print("Respuesta correcta.")
        
    else:
        print("Respuesta incorrecta, ha perdido.")
        break



















































































# Ejemplo de uso:
# archivo_csv = "preguntas.csv"
# leer_preguntas_desde_csv(lista_preguntas, archivo_csv)
# # for pregunta in lista_preguntas:
# #     print(f"Categoría: {pregunta['categoria']}")
# #     print(f"Dificultad: {pregunta['dificultad']}")
# #     print(f"Pregunta: {pregunta['pregunta']}")
# #     print(f"Opciones: {pregunta['opciones']}")
# #     print(f"Respuesta correcta: {pregunta['respuesta_correcta']}")
# #     print("=" * 50)
# print(lista_preguntas)
