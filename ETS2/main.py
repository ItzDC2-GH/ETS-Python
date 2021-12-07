minimo = int (input("Dime el mínimo ")) #Pedimos el minimo
maximo = int (input("Dime el máximo ")) #Pedimos el máximo
for minimo in range(maximo + 1): #Creamos el bucle
    if minimo % 2 == 0: #Comprobación (% 2 == 0: par; % 2 != 0: impar;)
        print(str(minimo) + " es par") #Imprimimos el resultado
    else:
        print(str(minimo) + " es impar") #Imprimimos el resultado
print("Terminado") #Imprimimos cuando se acaba el bucle.

