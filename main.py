from generales import *


seguir = True
while seguir:
    print("1. JUGAR")
    print("2. SALIR")
    opcion = seleccionar_opcion_menu("Elija una opción: ")

    match opcion:
        case 1:
            pass
        case 2:
            if not desea_continuar("Desea continuar jugando? SI/NO: ", "Error. Ingrese SI/NO: "):
                seguir = False
                break
        case _:
            print("Error. Ingrese una opción del Menú.")


