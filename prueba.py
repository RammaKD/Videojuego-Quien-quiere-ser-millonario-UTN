dict_elementos_pantalla_principal ={
        "imagenes":[("fondo_men", (450, 75), False),                    
                    ("logo", (450, 75), False)],
        
        "textos" : [["pregunta", (25, 425), False],
                    ["respuesta_A", (25, 550), True],
                    ["respuesta_B",(450, 550), True],
                    ["respuesta_C", (25, 650), True],
                    ["respuesta_D", (450, 650), True],
                    ("50-50", (150,55), True),
                    ("Publico", (275,55), True),
                    ("Llamada", (440,55), True)],

        "interactivos" : []
    }



print(dict_elementos_pantalla_principal["textos"][0][0])
        

    # for elementos in clave:
    #     print(elementos)
    #if clave != "interactivos":
        #for elemento in clave:
         #   if type(elemento[0]) == str: 
                #     surface = elemento[clave][0]
                #     texto = str(surface)
                # else:
                #     texto = elemento[0]
                #     surface = crear_texto_renderizado(texto, fuente, color_texto, color_fondo)
                # posicion = elemento[1]
                # interactivo = elemento[2]
                # rect = surface.get_rect()
                # rect.topleft = posicion