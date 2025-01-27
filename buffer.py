def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")  
    return buffer


def procesar_buffer(entrada, tamano_buffer):
    inicio_global = 0
    lexema_incompleto = ""
    buffer = cargar_buffer(entrada, 0, tamano_buffer)
    puntero = 0

    while True:
        while puntero < len(buffer):
            if buffer[puntero] == "eof":
                if lexema_incompleto:
                    print(f"Lexema procesado: {lexema_incompleto}")
                return

            if buffer[puntero] == " ":
                if lexema_incompleto:
                    print(f"Lexema procesado: {lexema_incompleto}")
                    lexema_incompleto = ""
            else:
                lexema_incompleto += buffer[puntero]
            
            puntero += 1

        inicio_global += tamano_buffer
        buffer = cargar_buffer(entrada, inicio_global, tamano_buffer)
        puntero = 0


entrada = list("Esto es un ejemplo de entrada con eof")
tamano_buffer = 10
procesar_buffer(entrada, tamano_buffer)
