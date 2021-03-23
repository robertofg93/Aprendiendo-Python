#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico 
#con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.


#Solucion 1
correo=input("Ingrese el correo electrónico: ")
lista=correo.split('@')
lista[1] = 'ceu.us'
print(lista[0]+'@'+ lista[1])

#Solución 2
correo=input("Ingrese el correo electrónico: ")
print(correo[:correo.find('@')] + '@ceu.us')