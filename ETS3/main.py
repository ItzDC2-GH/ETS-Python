minimo = int(input("Dime el mínimo ")) #Pedimos el mínimo
maximo = int(input("Dime el máximo ")) #Pedimos el máximo

print("Números primos desde el " + str(minimo) + " hasta el " + str(maximo))

if minimo >= 1 and minimo < 10000 and maximo < 10000: #Comprobaciones previas
    for numero in range(minimo, maximo + 1): #Creamos el bucle
        if all(numero % i != 0 for i in range(2, numero)): #Chequeamos que todas las condiciones sean correctas.
            print("El número " + str(numero) + " es primo.") #Imprimimos el resultado
elif maximo >= 10000 or minimo >= 10000: #Comprobaciones secundarias
    print("No se puede calcular ese número.")
elif minimo < 1: #Comprobaciones secundarias
    print("El mínimo tiene que ser mayor que 1")


