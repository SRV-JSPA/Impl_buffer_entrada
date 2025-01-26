# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = entrada[inicio:inicio + tamano_buffer]
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

def procesar_buffer(buffer):
    print("Buffer inicial:", buffer)

    lexema = []
    inicio = 0  
    avance = 0  

    while inicio < len(buffer):
        
        while avance < len(buffer) and buffer[avance] not in [" ", ""]:
            avance += 1

        if avance > inicio:
            lexema.append("".join(buffer[inicio:avance]))  

        avance += 1  
        inicio = avance  

    print(lexema)

entrada = list("Esto es un ejemplo eof")
inicio = 0
tamano_buffer = 10
buffer = cargar_buffer(entrada, inicio, tamano_buffer)
procesar_buffer(buffer)