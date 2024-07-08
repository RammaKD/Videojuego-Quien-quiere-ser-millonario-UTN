import json

def leer_preguntas_csv(ruta_archivo_csv):
    """
    Lee un archivo CSV desde la ruta especificada y retorna una lista de datos estructurada.
    
    Parámetros:
    ruta_archivo_csv (str): Ruta del archivo CSV a leer.
    
    Retorna:
    list: Lista de datos del archivo CSV, con el encabezado y los valores de las preguntas.
    """
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

def cargar_billetera_json(ruta_archivo_json):
    """
    Carga datos de una billetera desde un archivo JSON especificado.

    Si el archivo no existe, retorna una billetera vacía.
    Si hay algún error durante la carga, imprime un mensaje de error y retorna una billetera vacía.

    Retorna:
    dict: Datos de la billetera cargados desde el archivo JSON o una billetera vacía si hay problemas.
    """
    exito = True
    try:
        with open(ruta_archivo_json, 'r') as file:
            billetera = json.load(file)
        return billetera
    except:
        exito = False
    return exito

def actualizar_billetera_json(ruta_archivo_json, puntuacion_actualizada):
    """
    Actualiza un archivo JSON con una nueva puntuación actualizada en la billetera.

    Parámetros:
    ruta_archivo_json (str): Ruta del archivo JSON a actualizar.
    puntuacion_actualizada (dict): Nueva puntuación a agregar a la billetera.

    Retorna:
    bool: True si la actualización fue exitosa, False si hubo algún error.
    """
    exito = True
    try:
        datos = cargar_billetera_json(ruta_archivo_json)
        datos["billetera"].append(puntuacion_actualizada)
        with open(ruta_archivo_json, "w") as archivo:
            json.dump(datos, archivo, indent=2)
    except:
        exito = False
        
    return exito

def obtener_paths(ruta_archivo_json):
    """
    Lee un archivo JSON desde la ruta especificada y retorna un diccionario con los paths obtenidos.

    Parámetros:
    ruta_archivo_json (str): Ruta del archivo JSON a leer.

    Retorna:
    dict: Diccionario con las rutas obtenidas desde el archivo JSON.
    """
    with open(ruta_archivo_json, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    diccionario_paths = {}
    
    for clave, valor in data["paths"].items():
        diccionario_paths[clave] = valor
    
    return diccionario_paths


