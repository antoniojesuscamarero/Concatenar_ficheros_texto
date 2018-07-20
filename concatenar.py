#Concatenar ficheros de texto en un único fichero

nombre=[]
lista=[]
list=39 #Numerar numeros ficheros a concatenar
f=open("000.txt","r+")
extension = ".txt"
for i in range(0,list):
    #print(i)
    nombre.append("00" + str(i+1) + extension)
    archivo = open(nombre[i], "r")

    for index in archivo:
        lista.append(index)
        
final_archivo = f.tell()
f.write(str(lista))

print(nombre)
