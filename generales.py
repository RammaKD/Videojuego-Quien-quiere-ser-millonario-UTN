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


import csv
import json

def leer_preguntas_desde_csv(archivo_csv):
    preguntas = []
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 5:
                categoria = row[0].strip()
                dificultad = row[1].strip()
                pregunta = row[2].strip()
                try:
                    opciones = json.loads(row[3].strip())
                except json.JSONDecodeError as e:
                    print(f"Error de JSON en la fila: {row}")
                    print(f"Mensaje: {e}")
                    continue
                respuesta_correcta = row[4].strip()
                
                preguntas.append({
                    'categoria': categoria,
                    'dificultad': dificultad,
                    'pregunta': pregunta,
                    'opciones': opciones,
                    'respuesta_correcta': respuesta_correcta
                })
            else:
                print(f"Error: Se encontró una fila con un número incorrecto de columnas: {row}")
    return preguntas

# Ejemplo de uso:
archivo_csv = r'c:\Users\Juanma\Desktop\Proyecto_millonario\Quien-quiere-ser-millonario_Barrios-Alfonzo_Azaldegui-Brizuela\preguntas.csv'
lista_preguntas = leer_preguntas_desde_csv(archivo_csv)
for pregunta in lista_preguntas:
    print(f"Categoría: {pregunta['categoria']}")
    print(f"Dificultad: {pregunta['dificultad']}")
    print(f"Pregunta: {pregunta['pregunta']}")
    print(f"Opciones: {pregunta['opciones']}")
    print(f"Respuesta correcta: {pregunta['respuesta_correcta']}")
    print("=" * 50)

