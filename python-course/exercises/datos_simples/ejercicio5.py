#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

#Solución
horasT = input("Ingrese las horas trabajadas: ")
costporH = input("Ingrese el coste por hora: ")

paga = float(horasT)*float(costporH)
print(f"La paga que le correponde es: {paga}")
