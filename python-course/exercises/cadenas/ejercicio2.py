#Escribir un programa que pregunte el nombre completo del usuario en la consola 
#y después muestre por pantalla el nombre completo del usuario tres veces,
#una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
#El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

#Solución
nombrefull=input("Entre su nombre completo: ")
print(nombrefull.lower())
print(nombrefull.upper())
print(nombrefull.capitalize())
print(nombrefull.title()) #El método title permite comenzar cada palabra por mayúscula 