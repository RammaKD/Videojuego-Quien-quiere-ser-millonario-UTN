import json

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

def obtener_paths(ruta_archivo_json):
    with open(ruta_archivo_json, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    diccionario_paths = {}
    
    for clave, valor in data["paths"].items():
        diccionario_paths[clave] = valor
    
    return diccionario_paths

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



