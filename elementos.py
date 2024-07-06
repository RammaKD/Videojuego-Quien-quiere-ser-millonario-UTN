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
logo = cargar_imagen(diccionario_paths["path_logo"], (450,350))
fondo_menu = cargar_imagen(diccionario_paths["path_fondo_menu"], DIMENSIONES_VENTANA)
presentador = cargar_imagen(diccionario_paths["path_presentador"], (450, 600))
flecha = cargar_imagen(diccionario_paths["path_flecha"], (100, 50))


texto_input_box = ""
texto_surface = crear_texto_renderizado(texto_input_box, FUENTE_PANTALLA_GAME_OVER, BLANCO, VIOLETA)
input_box_premio = texto_surface.get_rect()


contador_nivel = 0
dict_cronometro = {
        "contador" : 30,
        
        "fuente" : [FUENTE_CRONOMETRO,BLANCO,VIOLETA]
        
}


dict_niveles_premios ={
        "piramide" : [
                        [1, "$100"],
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


dict_prop_texto = {"fuente_principal" : FUENTE_PRINCIPAL,
                "fuente_pantalla_juego": FUENTE_PANTALLA_JUEGO,
                "fuente_cronometro" : FUENTE_CRONOMETRO,
                "fuente_comodines" : FUENTE_COMODINES,
                "fuente_pantalla_game_over":FUENTE_PANTALLA_GAME_OVER,
                "fuente_piramide_premios" :FUENTE_PIRAMIDE_PREMIOS,
                "color_texto" : BLANCO,
                "color_fondo" : VIOLETA
}

flags_variables = {
    "flag_run": True,
    "flag_pantalla_principal": True,
    "flag_pantalla_categorias": False,
    "flag_pantalla_juego": False,
    "flag_pregunta_mostrada": False,
    "flag_cronometro_activo": False,
    "flag_pantalla_game_over": False,
    "flag_pantalla_checkpoint": False,
    "flag_boton_pantalla_game_over": False,
    "flag_botones_pantalla_checkpoint": False,
    "flag_botones_respuestas": True,
    "flag_pantalla_guardar_score": False,
    "flag_botones_pantalla_guardar_score": False,
    "flag_pantalla_victoria": False,
    "flag_botones_pantalla_victoria": False,
    "flag_comodin_pista": True,
    "flag_comodin_publico": True,
    "flag_comodin_50_50": True,
    "flag_scores_mostrados" : True
}


dict_elementos_pantalla_principal ={
        "imagenes":[(fondo_menu, POS_INICIAL_FONDO, False),                    
                                        (logo, (450, 75), False)],
        
        "textos" : [("JUGAR", (380, 515), True), 
                                        ("SALIR", (750, 515), True),
                                        ("Pantalla puntajes[tab]",(370,600),False)],

        "fuente" :[FUENTE_PRINCIPAL,BLANCO,VIOLETA],

        "interactivos" : []
    }
        
dict_elementos_pantalla_categorias ={
        
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
dict_general_pantallas_secundarias ={   
        "dict_elementos_pantalla_victoria" : {
                
                "imagenes" : [(fondo_menu, POS_INICIAL_FONDO, False)],

                "textos" :[ ("Felicidades!", (300, 300), False),
                        ("Ha ganado el millón!", (300, 450), False),
                        ("Retirar premio", (300, 600), True)],
                
                "fuente" :[FUENTE_PANTALLA_GAME_OVER,BLANCO,VIOLETA],
                
                "interactivos": []
        },

        "dict_elementos_pantalla_game_over" : {
                "imagenes" : [(fondo_menu, POS_INICIAL_FONDO, False)],

                "textos" : [("Has perdido!", (450, 300), False),
                        ("Volver al menu principal", (270, 450), True)],
                
                "fuente" :[FUENTE_PANTALLA_GAME_OVER,BLANCO,VIOLETA],

                "interactivos": [],
        },
      
        
        "dict_elementos_pantalla_checkpoint" :{
                "imagenes" : [(fondo_menu, POS_INICIAL_FONDO, False)],

                "textos" :[("Quiere seguir jugando?", (250, 200), False),
                                                ("Seguir jugando", (350, 450), True),
                                                ("Retirarse", (450, 550), True)],

                "fuente" :[FUENTE_PANTALLA_GAME_OVER,BLANCO,VIOLETA],

                "interactivos": []
},

        "dict_elementos_pantalla_score" : {
                "imagenes" : [(fondo_menu, POS_INICIAL_FONDO, False)],

                "textos" : [("Introduzca su nombre", (300, 300), False)],

                "fuente" :[FUENTE_PANTALLA_GAME_OVER,BLANCO,VIOLETA],

                "interactivos" : []
}}

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

        "fuente" :[ FUENTE_PANTALLA_JUEGO,BLANCO,VIOLETA],
        

        "interactivos" : []
}

# lista_elementos_interactivos_principal = []
# lista_elementos_interactivos_categorias = []
# lista_elementos_interactivos_game_over = []
# lista_elementos_interactivos_checkpoint = []
# lista_elementos_interactivos_score = []
# lista_elementos_interactivos_victoria = []



# lista_textos_pantalla_principal = [("JUGAR", (380, 515), True), 
#                                    ("SALIR", (750, 515), True),
#                                    ("Pantalla puntajes[tab]",(370,600),False)]

# lista_textos_pantalla_categorias = [("Eliga una categoria", (450, 365), False),
#                                     ("Historia", (275, 500), True),
#                                     ("Deportes", (515, 500), True),
#                                     ("Ciencia", (800, 500), True),
#                                     ("Entretenimiento", (275, 600), True),
#                                     ("Geografía", (715, 600), True)]

# lista_textos_pantalla_checkpoint = [("Quiere seguir jugando?", (250, 200), False),
#                                     ("Seguir jugando", (350, 450), True),
#                                     ("Retirarse", (450, 550), True)]

# lista_textos_pantalla_game_over_incorrecta = [("Has perdido!", (450, 300), False),
#                                               ("Volver al menu principal", (270, 450), True)]

# lista_textos_pantalla_game_over_tiempo_finalizado = [("Has perdido!", (450, 300), False),
#                                                      ("Volver al menu principal", (270, 450), True)]

# lista_textos_pantalla_score = [("Introduzca su nombre", (300, 300), False)]

# lista_textos_pantalla_victoria = [("Felicidades!", (300, 300), False),
#                                   ("Ha ganado el millón!", (300, 450), False),
#                                   ("Retirar premio", (300, 600), True)]

# lista_imgs_pantalla_principal = [(fondo_menu, POS_INICIAL_FONDO, False),                    
#                                  (logo, (450, 75), False)]

# lista_imgs_pantalla_categorias = [(fondo_menu, POS_INICIAL_FONDO, False),                    
#                                   (logo, (450, 0), False)]

# lista_imgs_pantalla_juego = [(fondo_menu, POS_INICIAL_FONDO, False),                    
#                              (presentador, POS_INICIAL_PRESENTADOR, False)]

# lista_imgs_pantalla_game_over = [(fondo_menu, POS_INICIAL_FONDO, False)]

# lista_posiciones_porcentajes = [(450, 100), (450, 130), (450, 160), (450, 190)]

# lista_elementos_pantalla_principal = lista_imgs_pantalla_principal + lista_textos_pantalla_principal
# lista_elementos_pantalla_categorias = lista_imgs_pantalla_categorias + lista_textos_pantalla_categorias
# lista_elementos_pantalla_victoria = lista_imgs_pantalla_game_over + lista_textos_pantalla_victoria
# lista_elementos_pantalla_score = lista_imgs_pantalla_game_over + lista_textos_pantalla_score




