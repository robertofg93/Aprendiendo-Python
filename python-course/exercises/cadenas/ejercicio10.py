#Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
#separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

#Solución 1
cesta=input("Entre los productos de la compra separdos por coma: ")
print(cesta.replace(',','\n'))

#Solución 2
print( '\n'.join(cesta.split(',')))

#Solución 3 (avanzada)
lista=cesta.split(',')

for lista in lista:
    print(lista + "\n")