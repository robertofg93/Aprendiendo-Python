#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
#y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

#Solución 1
price=input("Ingrese el precio de un producto en euros con dos decimales: ")
lista=price.split('.')
print('El precio en euros es: ' + lista[0] , "y el número de céntimos es: " + lista[1])

#Solución 2
price=input("Ingrese el precio de un producto en euros con dos decimales: ")
print('El precio en euros es: ' + price[:price.find('.')] , "y el número de céntimos es: " + price[price.find('.')+1:])
