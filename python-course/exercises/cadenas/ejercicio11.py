#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades 
#y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario 
#con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos
#enteros y 2 decimales.

#Solución
product=input("Nombre del producto: ")
price=float(input("Precio del producto: "))
quantity=int(input("Cantidad del producto: "))
total=quantity*price
print({total :3f})