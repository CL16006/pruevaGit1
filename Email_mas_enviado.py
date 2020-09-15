#lo que vamos hacer aqui es leer el archivo linea por linea y a contar cuantas veces aparece un correo electronico
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#se define la variable diccionario
diccionario=dict()
#definimos una lista
lista=list()
#con este for leemos el archivo linea por linea
for line in handle:
    #quitamos espacios en blancos de la lines
    line=line.rstrip()
    #verificamos si la linea comienza con la palabra From
    if line.startswith('From'):
        #convertimos la linea en un array
        n=line.split()
        #asignamos la clave que sera el correo y esta en la posicion n[1]
        clave=n[1]
        #agregamos la clave a una lista
        lista.append(clave)
        #si la clave no esta en el diccionario la agregamos con el valor de uno.
        if clave not in diccionario:
            diccionario[clave]=1
        else:
            diccionario[clave]=diccionario[clave]+1
mayor=None
correo=None
#usamos este for para encontrar la clave con mayor numero.
for word,count in diccionario.items():
    if mayor is None or count>mayor:
        correo=word
        mayor=count

print(correo,mayor)
#print(diccionario)
