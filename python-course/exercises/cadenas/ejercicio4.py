#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
#y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
#Escribir un programa que pregunte por un número de teléfono con este formato
#muestre por pantalla el número de teléfono sin el prefijo y la extensión.

#Solución

#variante 1 recomendada
telefonofull=input("Entre el teléfono empresarial con el formato +xx-xxxxxxx-xx: ")
lista = telefonofull.split('-')
print(lista[1])             

#variante2
telefonofull=input("Entre el teléfono empresarial con el formato +xx-xxxxxxx-xx: ")
print(telefonofull[4:-3])