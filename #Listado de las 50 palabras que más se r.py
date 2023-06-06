#Listado de las 50 palabras que más se repiten
def limpiar_texto(texto):
    # Lista de signos de puntuación a eliminar
    signos_puntuacion = [".", ",", "!", "?", "'", '"', ";", ":", "-", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\"]

    # Eliminar los signos de puntuación del texto
    for signo in signos_puntuacion:
        texto = texto.replace(signo, "")

    return texto

def encontrar_palabras_repetidas(texto, cantidad_palabras):
    # Convertir el texto a minúsculas
    texto = texto.lower()
    
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Crear un diccionario para almacenar la frecuencia de las palabras
    frecuencia = {}
    
    # Calcular la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    # Ordenar las palabras por su frecuencia en orden descendente
    palabras_ordenadas = sorted(frecuencia, key=frecuencia.get, reverse=True)
    
    # Obtener las palabras más repetidas
    palabras_repetidas = palabras_ordenadas[:cantidad_palabras]
    
    return palabras_repetidas

def imprimir_palabras(palabras_repetidas, frecuencia):
    print("Las 50 palabras más repetidas son:")
    for palabra in palabras_repetidas:
        repeticiones = frecuencia[palabra]
        print(palabra)

if __name__ == "__main__":
    address = "D:/Cosas Lis/College/Materias/Programacion I/Reto 12/mbox-short.txt"
    with open(address) as file_object:
        read = file_object.read()
    
    cantidad_palabras = 50
    
    # Limpiar el texto de signos de puntuación
    read = limpiar_texto(read)
    
    palabras_repetidas = encontrar_palabras_repetidas(read, cantidad_palabras)
    
    # Crear un diccionario con la frecuencia de las palabras
    frecuencia = {}
    for palabra in palabras_repetidas:
        frecuencia[palabra] = read.count(palabra)
    
    imprimir_palabras(palabras_repetidas, frecuencia)