
#Listado de destinatarios con cantidad de mensajes recibidos
def destinatariosConMensajesRecibidos(read:str) -> dict:
    read = read.lower()
    words = read.split()
    emails = []
    bandera = False 
    diccionario = {}
    for i in range(len(words)):
        if words[i] == "received:":
            bandera = True
        elif words[i] == "(gmt)" or words[i] == "-0500":
            bandera = False
        if bandera == True and words[i] == "by":
            emails.append(words[i+1])
    
    for i in emails: diccionario[i] = 0  
    for i in emails: diccionario[i] += 1 
    
    return diccionario

if __name__ == "__main__":
    address = "D:/Cosas Lis/College/Materias/Programacion I/Reto 12/mbox-short.txt"
    with open(address, 'r') as file_object:
        read = file_object.read()
        destinatariosYMensajes = destinatariosConMensajesRecibidos(read)
        destino = list(destinatariosYMensajes.items())
        print(destino)