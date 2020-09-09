numero=int(input("Ingrese numero: "))
x=1
contador=0
if(numero==1):
    print("No es primo")
else:
    while x <= numero:
        if numero%x==0:
            contador+=1
        x+=1
    if contador==2:
        print('el numero primo')
    else:
        print('no es primo')