#usuario ingresa total de bloques y se crea piramide con esos bloques
blocks=int(input("ingrese numero de bloques: "))
#height es la altura de la piramide
height=0
#suma es una variable que se ocupa para comparar
suma=0

#ocupamos el while para sacar la altura que tendra nuestra piramide
while suma<=blocks:
    height += 1
    suma+=height

i=1
altura=int(height)
usados=0
j=0

while i < int(altura):
    print(" "*(altura-i),"* "*i)
    usados=usados+(1*i)
    i += 1

sobrantes=blocks-usados
print('Bloques sobrantes',sobrantes)