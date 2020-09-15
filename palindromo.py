palabra=input("ingrese palabra: ")

palabra_invertida="".join(list(reversed(palabra)))

if(palabra.lower().replace(" ","")==palabra_invertida.lower().replace(" ","")):
    print(f"{palabra} es palindromo")
else:
    print(f"{palabra} no es palidromo")