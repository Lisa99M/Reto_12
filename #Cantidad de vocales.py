#Cantidad de vocales
def Contar_vocales (read:str) -> int:
    list= []
    for i in read.lower():
        if i == "a" or "e" or "i" or "o" or "u":
            list.append(i)
    print("En el texto hay: " + str(len(list)) + " vocales.")

if __name__ == "__main__":
    address = "D:/Cosas Lis/College/Materias/Programacion I/Reto 12/mbox-short.txt"
    with open(address) as file_object:
        read = file_object.read()
    cantidad_de_vocales = Contar_vocales(read)    

