#for 
#Sintáxis for
#for in <list>:
#    <action>

#Ejemplo 1
foods = ["manzana", "peras", "arroz", "queso", "lechugas", "pollo"]

for food in foods:
    if food == "queso":
        print(f"Tu tienes {food}")
    print(food)

#Ejemplo 2
for food in foods:
    if food == "queso":  #break permite que cuando se cumpla la condición pare el ciclo
        break
    print(food)

#Ejemplo 3
for food in foods:
    if food == "queso": #continue permite qu aunque se cumpla la condición siga ejecutandose el ciclo
        continue
    print(food)

#Ejemplo 4
for number in range(1, 10):
    print(number)

#Ejemplo 5
for letra in "Hello":
    print(letra)