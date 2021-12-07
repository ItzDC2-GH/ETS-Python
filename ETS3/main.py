minimo = int(input("Dime el mínimo ")) #Pedimos el mínimo
maximo = int(input("Dime el máximo ")) #Pedimos el máximo

print("Números primos desde el " + str(minimo) + " hasta el " + str(maximo)) 

if minimo >= 1 and minimo < 10000 and maximo < 10000: #Comprobaciones previas
   for numero in range(minimo, maximo + 1): #Creamos el primer bucle 
       if numero > 1: #Comprobamos que sea mayor que 1
           for i in range(2, numero): #Creamos el segundo bucle
               if(numero % i) == 0: #Comprobamos que de 0 (si da, rompemos la iteración para que salte a la otra.)
                #    pass
                #    print(str(numero) + " no es primo")
                   break
               else: # Sería primo, se le añade break, para romper el segundo ciclo ya que si no, se imprimiría varias veces la misma variable.
                   print(str(numero) + " es primo")
                   break
elif maximo >= 10000 or minimo >= 10000: #Comprobaciones secundarias
    print("No se puede calcular ese número.")
elif minimo < 1: #Comprobaciones secundarias
    print("El mínimo tiene que ser mayor que 1")


