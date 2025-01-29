def cargar_buffer(entrada, inicio, tamano_buffer):
    """Carga un segmento del texto en el buffer con tamaño fijo."""
    buffer = entrada[inicio:inicio + tamano_buffer]
    
    # Si el buffer es menor al tamaño esperado, añadimos "eof"
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    
    return buffer

def procesar_buffer(entrada, tamano_buffer=10):
    """Procesa la entrada simulando un buffer de entrada con punteros."""
    inicio = 0  # Puntero que indica desde dónde se recarga el buffer
    lexema = ""  # Variable para acumular caracteres entre buffers
    
    while inicio < len(entrada):
        buffer = cargar_buffer(entrada, inicio, tamano_buffer)
        avance = 0  # Reiniciamos el puntero avance en cada recarga
        
        while avance < len(buffer):
            caracter = buffer[avance]
            
            # Si encontramos un espacio o "eof", procesamos el lexema
            if caracter == " " or caracter == "eof":
                if lexema:  # Evitar imprimir lexemas vacíos
                    print(f"Lexema procesado: {lexema}")
                    lexema = ""  # Reiniciamos para el próximo lexema
            else:
                lexema += caracter  # Acumulamos caracteres en el lexema
            
            avance += 1  # Avanzamos al siguiente carácter
        
        inicio += tamano_buffer  # Avanzamos al siguiente bloque del buffer

    # Si quedó un lexema pendiente al final, lo imprimimos
    if lexema:
        print(f"Lexema procesado: {lexema}")

# Entrada de prueba
entrada = list("Esto es un ejemplo de entrada con eof")
procesar_buffer(entrada)
