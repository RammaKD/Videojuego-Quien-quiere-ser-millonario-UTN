from generales import *

lista_preguntas = []
lista_preguntas_tocadas = []
path_preguntas = cargar_paths("paths.json")[0]
path_dinero = cargar_paths("paths.json")[1]

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
                lista_categorias = ["Historia", "Deporte", "Entretenimiento", "Ciencia", "Geografía"]
                opcion_categoria = seleccionar_opcion_menu("Elija una opción: ")
                lista_preguntas.clear()
                if opcion_categoria != 6:
                    categoria_elegida = lista_categorias[opcion_categoria - 1]
                    leer_preguntas_desde_csv(lista_preguntas, categoria_elegida, path_preguntas)
                    billetera = cargar_puntuaciones_json(path_dinero)
                    print(f"Billetera: ${billetera}")
                
                match opcion_categoria:
                    case 1:
                        ejecutar_juego(lista_preguntas, lista_preguntas_tocadas, piramide_premios, billetera, path_dinero)
                        break
                    case 2: 
                        ejecutar_juego(lista_preguntas, lista_preguntas_tocadas, piramide_premios, billetera, path_dinero)
                        break
                    case 3:
                        ejecutar_juego(lista_preguntas, lista_preguntas_tocadas, piramide_premios, billetera, path_dinero)
                        break
                    case 4:
                        ejecutar_juego(lista_preguntas, lista_preguntas_tocadas, piramide_premios, billetera, path_dinero)
                        break
                    case 5:
                        ejecutar_juego(lista_preguntas, lista_preguntas_tocadas, piramide_premios, billetera, path_dinero)
                        break
                        
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


