#Escribir un programa que lea un entero positivo n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
# La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
#suma = n(n+1)

#Solución
number = int(input("Entre el número: "))
 
#for number in range(1,int(number)):
suma = number*(number + 1)/2
print(suma)
