#un numero oblongo es un numero que es el producto de dos numeros naturales consecutivos, es decir,
# n es un numero oblongo si existe un numero natural x tal que n=x(x+1)
#por ejemplo 42, ese oblongo, 6*7=42
numero=int(input('Ingrese un numero: '))
es_oblongo=False
for x in range(numero):
    n=x*(x+1)
    if n==numero:
        print(numero,' Es oblongo')
        es_oblongo=True
        break
    n+=1
if es_oblongo==False:
    print(numero,'No es oblongo')

