#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
#y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

#Solución
#el programa solo funciona si la vocal se encuentra en la frase
frase=input("Escriba una frase: ")
vocal=input("Escriba una vocal: ")
print(frase.replace(vocal,vocal.upper()))
