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

def cargar_billetera_json(ruta_archivo_json):
    try:
        with open(ruta_archivo_json, 'r') as file:
            billetera = json.load(file)
        return billetera
    except FileNotFoundError:
        return {"billetera": []}
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return {"billetera": []}

def actualizar_billetera_json(ruta_archivo_json, puntuacion_actualizada):
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
    with open(ruta_archivo_json, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    diccionario_paths = {}
    
    for clave, valor in data["paths"].items():
        diccionario_paths[clave] = valor
    
    return diccionario_paths
































