from generales import *

archivo_preguntas = "preguntas.csv"
archivo_premios = "premios.json"

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


seguir = True
while seguir:
    print("1. JUGAR")
    print("2. SALIR")
    opcion = seleccionar_opcion_menu("Elija una opción: ")

    match opcion:
        case 1:
            seguir_eligiendo = True
            while seguir_eligiendo:
                print("1. Historia")
                print("2. Deporte")
                print("3. Entretinimiento")
                print("4. Ciencia")
                print("5. Geografía")
                print("6. Salir")
                opcion_categoria = seleccionar_opcion_menu("Elija una opción: ")

                match opcion_categoria:
                    case 1:
                        nivel = piramide_premios[0][0]
                        
                    case 2: 
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        if desea_continuar("Desea dejar de elegir? SI/NO: ", "Error. Ingrese SI/NO: "):
                            seguir_eligiendo = False
                    case _:
                        print("Error. Ingrese una opción del Menú.")
                        
        case 2:
            if desea_continuar("Desea salir? SI/NO: ", "Error. Ingrese SI/NO: "):
                seguir = False
                break
        case _:
            print("Error. Ingrese una opción del Menú.")


