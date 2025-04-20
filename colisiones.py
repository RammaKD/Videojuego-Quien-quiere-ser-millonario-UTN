def manejar_colision_pantalla_principal(mouse_pos, dict_elementos):
    """
    Verifica si la posición del mouse colisiona con algún elemento interactivo en la pantalla principal.
    Si hay una colisión, devuelve el nombre del botón correspondiente.
    """
    boton_seleccionado = None
    for elemento in dict_elementos["interactivos"]:
        if elemento[1].collidepoint(mouse_pos):
            boton_seleccionado = elemento[0]

    return boton_seleccionado

def manejar_colision_pantalla_categorias(mouse_pos, dict_elementos):
    """
    Verifica si la posición del mouse colisiona con algún elemento interactivo en la pantalla de categorías.
    Si hay una colisión, devuelve el nombre de la categoría seleccionada.
    """
    
    categoria_elegida = None
    for elemento in dict_elementos["interactivos"]:
        if elemento[1].collidepoint(mouse_pos):
            categoria_elegida = elemento[0]

    return categoria_elegida

def manejar_colision_respuestas_pantalla_juego(estado_juego, mouse_pos, dict_elementos):
    """
    Verifica si la posición del mouse colisiona con alguna respuesta interactiva en la pantalla de juego.
    Si hay una colisión, devuelve la respuesta seleccionada.
    """
    respuesta_seleccionada = None
    for elemento in dict_elementos["dict_elementos_pantalla_juego"]["interactivos"][:4]:
        if elemento[1].collidepoint(mouse_pos):
            respuesta_seleccionada = elemento[0]
            
    return respuesta_seleccionada

def manejar_colision_comodines_pantalla_juego(mouse_pos, dict_elementos):
    """
    Verifica si la posición del mouse colisiona con algún comodín interactivo en la pantalla de juego.
    Si hay una colisión, devuelve el comodín seleccionado.
    """
    comodin_elegido = None
    for elemento in dict_elementos["dict_elementos_pantalla_juego"]["interactivos"][4:7]:
        if elemento[1].collidepoint(mouse_pos):
            comodin_elegido = elemento[0]

    return comodin_elegido

def manejar_colision_pantalla_game_over(mouse_pos, dict_general_pantallas_secundarias):
    """
    Verifica si la posición del mouse colisiona con algún elemento interactivo en la pantalla de game over.
    Si hay una colisión, devuelve True.
    """
    retorno = False
    for elemento in dict_general_pantallas_secundarias["game_over"]["interactivos"]:
        if elemento[1].collidepoint(mouse_pos):
            retorno = True

    return retorno

def manejar_colision_pantalla_checkpoint(mouse_pos, dict_general_pantallas_secundarias):
    """
    Verifica si la posición del mouse colisiona con algún elemento interactivo en la pantalla de checkpoint.
    Si hay una colisión, devuelve el nombre del botón seleccionado.
    """
    boton_seleccionado = None
    for elemento in dict_general_pantallas_secundarias["checkpoint"]["interactivos"]:
        if elemento[1].collidepoint(mouse_pos):
            boton_seleccionado = elemento[0]

    return boton_seleccionado

def manejar_colision_pantalla_victoria(mouse_pos, dict_general_pantallas_secundarias):
    """
    Verifica si la posición del mouse colisiona con algún elemento interactivo en la pantalla de victoria.
    Si hay una colisión, devuelve el nombre del botón seleccionado.
    """
    boton_seleccionado = None
    for elemento in dict_general_pantallas_secundarias["victoria"]["interactivos"]:
        if elemento[1].collidepoint(mouse_pos):
            boton_seleccionado = elemento[0]
         
    return boton_seleccionado













