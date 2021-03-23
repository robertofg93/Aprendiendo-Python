#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
#e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

#Solución
nombre=input('Cuales tu nombre:')   #Si en un print se multpica un texto por un numero entero el texto se repite 
                                    #tantas veces como el número entero
num=int(input("Entre el número entero: "))
print((nombre + "\n")* num)