#Escribir un programa que pregunte el nombre del usuario en la consola y 
#después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
#donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

#Solución
nombre=input("Entre su nombre: ")

#variante 1
nombre1=nombre.upper()
longitud=len(nombre)
print(f"El nombre {nombre1} tiene {longitud} letras")

#variante 2
print("El nombre", nombre.upper(),"y tiene",len(nombre),"letras")