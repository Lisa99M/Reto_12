#Cantidad de consonantes
def Contar_consonantes (read:str) -> int:
    consonantes = 0
    vocales = "aeiou"
    for i in read.lower():
        if i.isalpha() and i not in vocales:
            consonantes += 1
    print("En el texto hay: " + str(consonantes) + " consonantes.")
       
if __name__ == "__main__":
    address = "D:/Cosas Lis/College/Materias/Programacion I/Reto 12/mbox-short.txt"
    
    with open(address) as file_object:
        read = file_object.read()
    cantidad_de_consonantes = Contar_consonantes(read)    



