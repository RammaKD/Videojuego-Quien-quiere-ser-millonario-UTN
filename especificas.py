from generales import *

#Funciones modificar y resetear
def modificar_dict_pantalla_juego(elementos_pantalla, estado_juego):
    """
    Modifica los textos de los elementos de la pantalla de juego con una nueva pregunta y respuestas.

    Esta funcion actualiza los elementos de texto en la pantalla del juego con la pregunta y 
    las opciones de respuesta proporcionadas en dict_pregunta.

    """
    dict_elementos = elementos_pantalla["dict_elementos_pantalla_juego"]
    dict_pregunta = estado_juego["dict_pregunta_cargada"]
    dict_elementos["textos"][0][0] = dict_pregunta["pregunta"]
    dict_elementos["textos"][1][0] = dict_pregunta["respuestas"][0]
    dict_elementos["textos"][2][0] = dict_pregunta["respuestas"][1]
    dict_elementos["textos"][3][0] = dict_pregunta["respuestas"][2]
    dict_elementos["textos"][4][0] = dict_pregunta["respuestas"][3]

    return dict_elementos
   
def resetear_juego(estado_juego, elementos_pantalla):
    """
    Restaura el estado inicial del juego, reseteando el contador, nivel, 
    lista de elementos interactivos y todas las banderas del juego a sus 
    valores iniciales.
    """
    estado_juego["contador_nivel"] = 0
    estado_juego["dict_cronometro"]["contador"] = 30
    elementos_pantalla["dict_elementos_pantalla_juego"]["interactivos"].clear()
    elementos_pantalla["dict_elementos_pantalla_categorias"]["interactivos"].clear()
    
    # Reseteo de banderas
    estado_juego["flags_variables"]["pantalla_juego"] = False
    estado_juego["flags_variables"]["pantalla_principal"] = True
    estado_juego["flags_variables"]["pregunta_mostrada"] = False
    estado_juego["flags_variables"]["cronometro_activo"] = False
    estado_juego["flags_variables"]["pantalla_game_over"] = False
    estado_juego["flags_variables"]["boton_pantalla_game_over"] = False
    estado_juego["flags_variables"]["botones_respuestas"] = True
    estado_juego["flags_variables"]["pantalla_checkpoint"] = False
    estado_juego["flags_variables"]["botones_pantalla_checkpoint"] = False
    estado_juego["flags_variables"]["Llamada"] = True
    estado_juego["flags_variables"]["Publico"] = True
    estado_juego["flags_variables"]["pantalla_guardar_score"] = False
    estado_juego["flags_variables"]["botones_pantalla_guardar_score"] = False
    estado_juego["flags_variables"]["50_50"] = True
    estado_juego["flags_variables"]["botones_categorias"] = False

    # Reseteo de otras variables
    estado_juego["categoria_elegida"] = None
    estado_juego["respuesta_seleccionada"] = None
    estado_juego["comodin_elegido"] = None
    estado_juego["dict_pregunta_cargada"] = None
    estado_juego["dict_niveles_premios"]["contador_nivel"] = 0  # Asegurarse de resetear el contador del nivel

    return estado_juego["contador_nivel"]

def cargar_comodin_en_pantalla(ventana_principal, estado_juego, elementos_pantalla):
    """
    Esta funcion se encarga de verificar qué comodín ha sido seleccionado por el jugador y 
    de mostrar el efecto correspondiente en la pantalla. Los comodines disponibles son:
    "Llamada", "Público" y "50-50". Dependiendo del comodín elegido, se actualiza la interfaz 
    gráfica para reflejar el uso de dicho comodín. Esto puede incluir mostrar una pista, 
    mostrar porcentajes de votación del público, o eliminar dos respuestas incorrectas
    """
    flags_variables = estado_juego["flags_variables"]
    comodines_en_pantalla = {
        "Llamada" : cargar_llamada,
        "Publico" : cargar_publico,
        "50_50" : cargar_50_50
    }
    
    for comodin in comodines_en_pantalla:
        if estado_juego["comodin_elegido"] == comodin and flags_variables[comodin]:
            comodines_en_pantalla[comodin](ventana_principal, estado_juego, elementos_pantalla)

def cargar_llamada(ventana_principal, estado_juego, elementos_pantalla):
    flags_variables = estado_juego["flags_variables"]
    flags_variables["Llamada"] = False
    fuente =  elementos_pantalla["dict_elementos_pantalla_juego"]["fuente"][0]
    color_texto = elementos_pantalla["dict_elementos_pantalla_juego"]["fuente"][1]
    color_fondo = elementos_pantalla["dict_elementos_pantalla_juego"]["fuente"][2]
    mostrar_pista(ventana_principal, estado_juego["dict_pregunta_cargada"]["pista"], 
                  fuente, color_texto , color_fondo)

def cargar_publico(ventana_principal, estado_juego, elementos_pantalla):
    flags_variables = estado_juego["flags_variables"]
    flags_variables["Publico"] = False
    fuente =  elementos_pantalla["dict_elementos_pantalla_juego"]["fuente"][0]
    color_texto = elementos_pantalla["dict_elementos_pantalla_juego"]["fuente"][1]
    color_fondo = elementos_pantalla["dict_elementos_pantalla_juego"]["fuente"][2]
    lista_respuestas = estado_juego["dict_pregunta_cargada"]["respuestas"]
    respuesta_correcta = estado_juego["dict_pregunta_cargada"]["respuesta_correcta"]
    lista_porcentajes = generar_porcentajes(lista_respuestas, respuesta_correcta)
    blitear_porcentajes(ventana_principal, lista_porcentajes, lista_respuestas, 
                        fuente, color_texto, color_fondo)

def cargar_50_50(ventana_principal, estado_juego, elementos_pantalla):
    flags_variables = estado_juego["flags_variables"]
    flags_variables["50_50"] = False
    dict_niveles_premios = estado_juego["dict_niveles_premios"]
    lista_respuestas = estado_juego["dict_pregunta_cargada"]["respuestas"]
    respuesta_correcta = estado_juego["dict_pregunta_cargada"]["respuesta_correcta"]
    dict_elementos_pantalla_juego = elementos_pantalla["dict_elementos_pantalla_juego"]
    dict_elementos_pantalla_juego["interactivos"].clear()
    dict_elementos_pantalla_juego["textos"] = aplicar_comodin_50_50(dict_elementos_pantalla_juego["textos"], 
                                                                    lista_respuestas, respuesta_correcta)
    cargar_pantalla(ventana_principal, dict_elementos_pantalla_juego)
    dibujar_niveles_premios(ventana_principal, dict_niveles_premios)
    blitear_flecha(estado_juego["contador_nivel"])

#Funciones manejar
def manejar_respuesta_seleccionada(estado_juego, elementos_pantalla):
    """
    Procesa la respuesta seleccionada por el jugador y actualiza el estado del juego en consecuencia.

    Si la respuesta seleccionada es correcta, se incrementa el nivel del contador, se reinicia el cronómetro,
    se marca la pregunta como no mostrada y se limpia la lista de elementos interactivos en la pantalla de juego.
    """
    retorno = False
    if estado_juego["dict_pregunta_cargada"]["respuesta_correcta"] == estado_juego["respuesta_seleccionada"]:
        estado_juego["contador_nivel"] += 1
        estado_juego["dict_cronometro"]["contador"] = 30
        estado_juego["flags_variables"]["pregunta_mostrada"] = False
        elementos_pantalla["dict_elementos_pantalla_juego"]["interactivos"].clear()
        retorno = estado_juego["respuesta_seleccionada"]
        
    return retorno

def manejar_boton_pantalla_principal(boton_seleccionado, flags_variables):
    """
    Maneja la acción a realizar cuando se selecciona un botón en la pantalla principal.

    Si el botón seleccionado es "JUGAR", desactiva la pantalla principal y activa la pantalla de categorías.
    Si el botón seleccionado es "SALIR", detiene la ejecución del juego.
    """
    if boton_seleccionado == "JUGAR":
        flags_variables["pantalla_principal"] = False
        flags_variables["pantalla_categorias"] = True
             
        
    elif boton_seleccionado == "SALIR":
        flags_variables["run"] = False

def manejar_boton_pantalla_checkpoint(boton, flags_variables):
    """
    Maneja la acción a realizar cuando se selecciona un botón en la pantalla de checkpoint.

    Si el botón seleccionado es "Retirarse", activa la pantalla para guardar el score y marca la pregunta como no mostrada.
    Si el botón seleccionado es "Seguir jugando", activa la pantalla del juego, los botones de respuesta, 
    el cronómetro, y marca la pregunta como no mostrada, desactivando los botones de checkpoint.
    """
    if boton == "Retirarse":
        flags_variables["pantalla_guardar_score"] = True
        flags_variables["pregunta_mostrada"] = False
    elif boton == "Seguir jugando":
        flags_variables["pantalla_juego"] = True
        flags_variables["botones_respuestas"] = True
        flags_variables["cronometro_activo"] = True
        flags_variables["pregunta_mostrada"] = False
        flags_variables["botones_pantalla_checkpoint"] = False

def manejar_boton_pantalla_victoria(boton, flags_variables):
    if boton == "Retirar premio":
        flags_variables["pantalla_guardar_score"] = True
        flags_variables["botones_pantalla_guardar_score"] = True
        flags_variables["pregunta_mostrada"] = False

def manejar_pantalla_guardar_score(elementos_pantalla, ventana_principal):
    """
    Maneja la acción a realizar cuando se selecciona un botón en la pantalla de victoria.
    Si el botón seleccionado es "Retirar premio", activa la pantalla para guardar el score, 
    activa los botones para guardar el score y marca la pregunta como no mostrada.
    """
    botones = cargar_pantalla(ventana_principal, elementos_pantalla["dict_general_pantallas_secundarias"]["score"])
    dibujar_input_box(botones, ventana_principal, ROJO)

def corroborar_checkpoint_y_victoria(estado_juego, flags_variables, elementos_pantalla):
    """
    Verifica si el jugador ha alcanzado un checkpoint o ha ganado el juego, y ajusta el estado del juego en consecuencia.

    Si el nivel actual es 6 o 11, desactiva la pantalla del juego y muestra la pantalla de checkpoint con la opción de retirarse.
    Si el nivel actual es 16, desactiva la pantalla del juego y muestra la pantalla de victoria.
    """
    retorno = None
    contador_nivel = estado_juego["contador_nivel"]
    nivel = contador_nivel + 1

    if nivel == 6 or nivel == 11:
        desactivar_pantalla_juego(flags_variables)
        dinero_a_retirar = estado_juego["dict_niveles_premios"]["piramide"][contador_nivel - 1][1]
        elementos_pantalla["dict_general_pantallas_secundarias"]["checkpoint"]["textos"][3][0] = f"O retirarse con: {dinero_a_retirar}"
        retorno = True
    elif nivel == 16:
        desactivar_pantalla_juego(flags_variables)
        flags_variables["pantalla_victoria"] = True
        flags_variables["botones_pantalla_victoria"] = True
        retorno = False
        
       
    return retorno


#Funciones actualizar, habilitar o cargar pantallas/elementos
def cargar_pantalla(ventana_principal, dict_elementos):
    """
    Carga y muestra elementos interactivos en una ventana principal, usando una fuente y colores específicos.
    """
    lista_botones = crear_propiedades_botones(dict_elementos)
    blitear_elementos(ventana_principal, lista_botones)

    return lista_botones

def actualizar_pantalla(estado_juego, elementos_pantalla, ventana_principal):
    """
    Actualiza la pantalla del juego según el estado actual.
    Muestra y actualiza los elementos gráficos de la pantalla correspondiente según la fase del juego:
    - Pantalla principal
    - Pantalla de categorías
    - Pantalla de juego con una nueva pregunta si es necesario
    - Pantalla de guardar score
    """
    flags_variables = estado_juego["flags_variables"]

    actualizacion_pantallas = {
        "pantalla_principal": actualizar_pantalla_principal,
        "pantalla_categorias" : actualizar_pantalla_categorias,
        "pantalla_juego" : actualizar_pantalla_juego,
        "pantalla_guardar_score" : actualizar_pantalla_guardar_score
    }

    for estado in actualizacion_pantallas:
        if flags_variables[estado]:
            actualizacion_pantallas[estado](ventana_principal, elementos_pantalla, estado_juego)

def actualizar_pantalla_principal(ventana_principal, elementos_pantalla, estado_juego):
    cargar_pantalla(ventana_principal, elementos_pantalla["dict_elementos_pantalla_principal"])

def actualizar_pantalla_categorias(ventana_principal, elementos_pantalla, estado_juego):
    cargar_pantalla(ventana_principal, elementos_pantalla["dict_elementos_pantalla_categorias"])
    
def actualizar_pantalla_juego(ventana_principal, elementos_pantalla, estado_juego):
    flags_variables = estado_juego["flags_variables"] 
    if not estado_juego["flags_variables"]["pregunta_mostrada"]:
        estado_juego["dict_pregunta_cargada"] = cargar_elementos_juego(estado_juego)
        elementos_pantalla["dict_elementos_pantalla_juego"] = modificar_dict_pantalla_juego(elementos_pantalla, estado_juego)
        cargar_pantalla(ventana_principal, elementos_pantalla["dict_elementos_pantalla_juego"])
        dibujar_niveles_premios(ventana_principal, estado_juego["dict_niveles_premios"])
        actualizar_cronometro(ventana_principal, estado_juego["dict_cronometro"])
        flags_variables["pregunta_mostrada"] = True
        blitear_flecha(estado_juego["contador_nivel"])

def actualizar_pantalla_guardar_score(ventana_principal, elementos_pantalla, estado_juego):
    estado_juego["flags_variables"] = habilitar_pantalla_guardar_score(estado_juego["flags_variables"])
    manejar_pantalla_guardar_score(elementos_pantalla, ventana_principal)

def administrar_pantalla_juego(mouse_pos, estado_juego, elementos_pantalla, ventana_principal, flags_variables):
    """
    Administra la interacción y actualización de la pantalla del juego.

    Esta función gestiona las colisiones del ratón con las respuestas y comodines en la pantalla del juego,
    carga y muestra los comodines seleccionados, y actualiza el estado del juego según las respuestas del jugador.
    """
    dict_general_pantallas_secundarias = elementos_pantalla["dict_general_pantallas_secundarias"]
    estado_juego["respuesta_seleccionada"] = manejar_colision_respuestas_pantalla_juego(estado_juego, mouse_pos, elementos_pantalla)
    estado_juego["comodin_elegido"] = manejar_colision_comodines_pantalla_juego(mouse_pos, elementos_pantalla)
    
    if estado_juego["comodin_elegido"] != None:
        cargar_comodin_en_pantalla(ventana_principal, estado_juego, elementos_pantalla)
    elif estado_juego["respuesta_seleccionada"] != None:
        estado_juego["respuesta_seleccionada"] = manejar_respuesta_seleccionada(estado_juego, elementos_pantalla)
        corroborar = corroborar_checkpoint_y_victoria(estado_juego, flags_variables, elementos_pantalla)
        if corroborar:
            flags_variables["pantalla_checkpoint"] = True
            flags_variables["botones_pantalla_checkpoint"] = True
            cargar_pantalla(ventana_principal, dict_general_pantallas_secundarias["checkpoint"])
        elif corroborar == False:
            cargar_pantalla(ventana_principal, dict_general_pantallas_secundarias["victoria"])
        if not estado_juego["respuesta_seleccionada"]:
            msj_error = "Respuesta incorrecta"
            dict_general_pantallas_secundarias = habilitar_game_over(flags_variables, elementos_pantalla, msj_error)
            cargar_pantalla(ventana_principal, dict_general_pantallas_secundarias["game_over"])
                
    return estado_juego

def habilitar_game_over(flag_variables, elementos_pantalla, msj_error):
    """Habilita la pantalla de game over con un mensaje de error específico.
    """
    flag_variables["pantalla_game_over"] = True
    flag_variables["boton_pantalla_game_over"] = True
    desactivar_pantalla_juego(flag_variables)
    elementos_pantalla["dict_general_pantallas_secundarias"]["game_over"]["textos"][2][0] = msj_error
    
    return elementos_pantalla["dict_general_pantallas_secundarias"]

def habilitar_pantalla_juego(flags_variables):
    """
    Habilita la pantalla de juego.
    Este método configura las banderas necesarias para mostrar la pantalla de juego,
    desactivando la pantalla de categorías y activando el cronómetro."""
    flags_variables["pantalla_categorias"] = False
    
    flags_variables["pantalla_juego"] = True
    flags_variables["cronometro_activo"] = True

def habilitar_pantalla_guardar_score(flags_variables):
    """
    Habilita la pantalla de guardar puntuación.
    Este método configura las banderas necesarias para mostrar la pantalla de guardar puntuación,
    desactivando los botones de respuestas, el botón de pantalla de game over y los botones de pantalla de checkpoint."""
    
    flags_variables["botones_respuestas"] = False
    flags_variables["boton_pantalla_game_over"] = False
    flags_variables["botones_pantalla_checkpoint"] = False
    flags_variables["botones_pantalla_guardar_score"] = True

    return flags_variables

def desactivar_pantalla_juego(flags_variables):
    """
    Desactiva la pantalla de juego."""
    
    flags_variables["pantalla_juego"] = False
    flags_variables["cronometro_activo"] = False
    flags_variables["botones_respuestas"] = False

    return flags_variables

def cargar_elementos_juego(estado_juego):
    """
    Carga y muestra los elementos del juego en la pantalla. Filtra las preguntas según 
    la categoría y nivel, selecciona una pregunta aleatoria y prepara las respuestas 
    y pistas para mostrar. Combina las imágenes y textos para la pantalla de juego y 
    los carga en la ventana.

    Retorna la respuesta correcta, pista, lista de textos en pantalla, lista de respuestas y 
    sus posiciones.
    """
    dict_pregunta_tocada = estado_juego["dict_pregunta_cargada"]
    lista_preguntas = estado_juego["lista_preguntas"]
    categoria_elegida = estado_juego["categoria_elegida"]
    contador_nivel = estado_juego["contador_nivel"]
    dict_pregunta_tocada = {}
    lista_posibles_preguntas = cargar_posibles_preguntas(lista_preguntas, categoria_elegida, contador_nivel)
    pregunta_cargada = cargar_pregunta_aleatoriamente(lista_posibles_preguntas)
    dict_pregunta_tocada["pregunta"] = pregunta_cargada["Pregunta"]
    dict_pregunta_tocada["respuestas"] = crear_lista_respuestas(pregunta_cargada)
    dict_pregunta_tocada["respuesta_correcta"] = pregunta_cargada["Respuesta_correcta"]
    dict_pregunta_tocada["pista"] = pregunta_cargada["Pista"]

    return dict_pregunta_tocada
