#encontrando el recuento de horas.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#se crea un diccionario.
diccionario=dict()
#se empieza a hacer una lectura del archivo linea por linea.
for line in handle:
    line=line.rstrip()
    #cuando la linea comienza en From se hace una split
    if line.startswith("From") and line.endswith("2008"):
        arrai=line.split()
        palabra=arrai[5]
        #aqui sehace un segundo split
        arrai2=palabra.split(":")
        clave=arrai2[0]
        if clave not in diccionario:
            diccionario[clave]=1
        else:
            diccionario[clave]=diccionario[clave]+1

ordenado=sorted(diccionario.items())

for c,v in ordenado:
    print(c,v)
