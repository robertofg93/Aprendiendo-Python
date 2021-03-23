# Definir una función se realiza con la palabra reservada def

#Ejemplo 1
def hello(name):
    print("Hello " + name)

hello("joe")

#Ejemplo 2
def hello(name="Persona"):  # Asi se puede definir parámetros por defecto
    print("Hello " + name)

hello("joe")
hello("betty")
hello()

#Ejemplo 3          #Ejemplo de funcíón que retorna la suma de 2 números
def sum(num1, num2):
    return num1 + num2

print(sum(3,4))


#Funciones lambda
#Las funciones lambdas son funciones anónimas que toman un número 
# de argumentos pero que tan solo pueden escritas utilizando uan sola expresión

#Ejemplo 4

sum = lambda num1, num2: num1 + num2
print(sum(4,4))

