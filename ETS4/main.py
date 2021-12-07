maximo = input("Dime el máximo ") #Pedimos el número de iteraciones

fibonacci = [0,1] #Creamos la tabla fibonacci dos argumentos (int)
for i in range(2, int(maximo) + 1): #Creamos el bucle
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2]) #Añadimos a la lista el resultado
    print("Iteración número " + str(i) + ": " + str(fibonacci[i])) #Imprimimos la iteración

