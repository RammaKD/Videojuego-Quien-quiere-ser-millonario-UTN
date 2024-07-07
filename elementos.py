from generales import *
from configuraciones import *
from funciones_visuales import *
from funciones_archivos import *

pygame.init()
lista_preguntas = []
diccionario_puntaje = {}
diccionario_paths = obtener_paths("archivos\\paths.json")
lista_datos_csv = leer_preguntas_csv(diccionario_paths["path_preguntas"])
crear_diccionario_preguntas(lista_datos_csv, lista_preguntas)
fondo_menu = cargar_imagen(diccionario_paths["path_fondo_menu"], DIMENSIONES_VENTANA)
logo = cargar_imagen(diccionario_paths["path_logo"], (450,350))
presentador = cargar_imagen(diccionario_paths["path_presentador"], (450, 600))
flecha = cargar_imagen(diccionario_paths["path_flecha"], (100, 50))
contador_nivel = 0

ventana_principal = pygame.display.set_mode(DIMENSIONES_VENTANA)
pygame.display.set_caption("Quien quiere ser millonario?")
pygame.display.set_icon(logo)
pygame.time.set_timer(CRONOMETRO, 1000)

dict_cronometro = {
        "contador" : 30,
        "fuente" : [FUENTE_CRONOMETRO, BLANCO, VIOLETA, ROJO]
}

dict_niveles_premios = {
        "piramide" : [[1, "$100"],
                      [2, "$200"],
                      [3, "$300"],
                      [4, "$500"],
                      [5, "$1000"],
                      [6, "$2000"],
                      [7, "$4000"],
                      [8, "$8000"],
                      [9, "$16000"],
                      [10, "$32000"],
                      [11, "$64000"],
                      [12, "$125000"],
                      [13, "$250000"],
                      [14, "$500000"],
                      [15, "$1000000"],
                      [16, ""]],
        "fuente" :[FUENTE_PIRAMIDE_PREMIOS,BLANCO,VIOLETA] 
}

dict_prop_texto = {
    "fuente_principal" : FUENTE_PRINCIPAL,
    "fuente_pantalla_juego": FUENTE_PANTALLA_JUEGO,
    "fuente_cronometro" : FUENTE_CRONOMETRO,
    "fuente_comodines" : FUENTE_COMODINES,
    "fuente_pantalla_game_over":FUENTE_PANTALLA_GAME_OVER,
    "fuente_piramide_premios" :FUENTE_PIRAMIDE_PREMIOS,
    "color_texto" : BLANCO,
    "color_fondo" : VIOLETA
}

flags_variables = {
    "run": True,
    "pantalla_principal": True,
    "pantalla_categorias": False,
    "pantalla_juego": False,
    "pregunta_mostrada": False,
    "cronometro_activo": False,
    "pantalla_game_over": False,
    "pantalla_checkpoint": False,
    "boton_pantalla_game_over": False,
    "botones_pantalla_checkpoint": False,
    "botones_respuestas": True,
    "pantalla_guardar_score": False,
    "botones_pantalla_guardar_score": False,
    "pantalla_victoria": False,
    "botones_pantalla_victoria": False,
    "comodin_pista": True,
    "comodin_publico": True,
    "comodin_50_50": True,
    "scores_mostrados" : False,
    "colision_rects" : False
}

dict_elementos_pantalla_principal = {
        "imagenes":[(fondo_menu, POS_INICIAL_FONDO, False),                    
                    (logo, (450, 75), False)],
        
        "textos" : [("JUGAR", (380, 515), True), 
                    ("SALIR", (750, 515), True),
                    ("Pantalla puntajes[tab]",(370,600),False)],
        
        "fuente" :[FUENTE_PRINCIPAL,BLANCO,VIOLETA],
        
        "interactivos" : []
}
        
dict_elementos_pantalla_categorias = {
        
        "imagenes" : [(fondo_menu, POS_INICIAL_FONDO, False),                    
                      (logo, (450, 0), False)],
        
        "textos": [("Eliga una categoria", (450, 365), False),
                   ("Historia", (275, 500), True),
                   ("Deportes", (515, 500), True),
                   ("Ciencia", (800, 500), True),
                   ("Entretenimiento", (275, 600), True),
                   ("Geografía", (715, 600), True)],
        
        "fuente" :[FUENTE_PRINCIPAL,BLANCO,VIOLETA],

        "interactivos" : []
}

dict_general_pantallas_secundarias = {   
        "victoria" : {
            "imagenes" : [(fondo_menu, POS_INICIAL_FONDO, False)],
            
            "textos" : [("Felicidades!", (300, 300), False),
                        ("Ha ganado el millón!", (300, 450), False),
                        ("Retirar premio", (300, 600), True)],
            
            "fuente" :[FUENTE_PANTALLA_GAME_OVER,BLANCO,VIOLETA],
                
            "interactivos": []
        },

        "game_over" : {
            "imagenes" : [(fondo_menu, POS_INICIAL_FONDO, False)],
            
            "textos" : [("Has perdido!", (450, 300), False),
                        ("Volver al menu principal", (270, 450), True),
                        ["", (320, 200), False]],
                
            "fuente" :[FUENTE_PANTALLA_GAME_OVER,BLANCO,VIOLETA],

            "interactivos": [],
        },
      
        "checkpoint" : {
            "imagenes" : [(fondo_menu, POS_INICIAL_FONDO, False)],

            "textos" : [("Quiere seguir jugando?", (250, 200), False),
                        ("Seguir jugando", (100, 400), True),
                        ("Retirarse", (800, 400), True),
                        ["", (250, 300), False]],

            "fuente" : [FUENTE_PANTALLA_GAME_OVER,BLANCO,VIOLETA],

            "interactivos": []
},

        "score" : {
            "imagenes" : [(fondo_menu, POS_INICIAL_FONDO, False)],

            "textos" : [("Introduzca su nombre", (300, 300), False),
                        ["", (400,400), True]],

            "fuente" :[FUENTE_PANTALLA_GAME_OVER,BLANCO,VIOLETA],

            "interactivos" : []
        }
}

dict_elementos_pantalla_juego = {
        "imagenes" : [(fondo_menu, POS_INICIAL_FONDO, False),                    
                      (presentador, POS_INICIAL_PRESENTADOR, False)],

        "textos" : [["pregunta", (25, 425), False],
                    ["respuesta_A", (25, 550), True],
                    ["respuesta_B",(450, 550), True],
                    ["respuesta_C", (25, 650), True],
                    ["respuesta_D", (450, 650), True],
                    ("50-50", (150,55), True),
                    ("Publico", (275,55), True),
                    ("Llamada", (440,55), True)],

        "fuente" : [FUENTE_PANTALLA_JUEGO, BLANCO, VIOLETA],
        
        "interactivos" : []
}





