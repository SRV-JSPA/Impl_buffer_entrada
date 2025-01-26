# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer and "eof" not in buffer:
        buffer.append("eof")
    return buffer

def procesar_buffer(entrada, tamano_buffer):
    inicio_global = 0
    lexema_incompleto = ""  

    while True:
        buffer = cargar_buffer(entrada, inicio_global, tamano_buffer)
        print("Buffer inicial:", buffer)

        inicio = 0
        avance = 0

        while avance < len(buffer):
            while avance < len(buffer) and buffer[avance] == " ":
                avance += 1
            inicio = avance

            while avance < len(buffer) and buffer[avance] not in [" ", "eof"]:
                avance += 1

            if avance > inicio:
                lexema = "".join(buffer[inicio:avance])
                lexema_incompleto += lexema  

                if avance < len(buffer) or "eof" in buffer:
                    print(f"Lexema procesado: {lexema_incompleto}")
                    lexema_incompleto = ""  

            avance += 1  
            inicio = avance  

        if "eof" in buffer:
            break

        inicio_global += tamano_buffer

entrada = list("Esto es un ejemplo de entrada con eof")
tamano_buffer = 10

procesar_buffer(entrada, tamano_buffer)
