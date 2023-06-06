def correos_por_fecha (read:str)-> dict: 
    read = read.lower()
    lines = read.split()
    contador_de_correos = {}
    mails = []
    bandera = False
    
    for i in range(len(lines)):
        if lines[i] == "received:":
            bandera = True
        elif lines[i] == "(gmt)" or lines[i] == "-0500":
            bandera = False
        if bandera == True and lines[i] == "jan":
            mails.append(int(lines[i-1]))
    
    for i in mails: contador_de_correos[i] = 0  
    for i in mails: contador_de_correos[i] += 1 
    
    return contador_de_correos

if __name__ == "__main__":
    address = "D:/Cosas Lis/College/Materias/Programacion I/Reto 12/mbox-short.txt"
    with open(address, 'r') as file_object:
        read = file_object.read()
        correos = list(correos_por_fecha (read).items())

        for i in correos:
            print(str(i) + " (dia, correos enviados)")

        