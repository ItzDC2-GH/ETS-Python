minimo = int(input("Dime el mínimo "))
maximo = int(input("Dime el máximo "))

print("Números primos desde el " + str(minimo) + " hasta el " + str(maximo))

if minimo >= 1 and minimo < 10000 and maximo < 10000: #
   for numero in range(minimo, maximo + 1):
       if numero > 1:
           for i in range(2, numero):
               if(numero % i) == 0:
                #    pass
                #    print(str(numero) + " no es primo")
                   break
               else:
                   print(str(numero) + " es primo")
                   break
elif maximo >= 10000 or minimo >= 10000: 
    print("No se puede calcular ese número.")
elif minimo < 1:
    print("El mínimo tiene que ser mayor que 1")


