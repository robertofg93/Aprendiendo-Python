#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión.

#Solución
# Fórmula Capital Final 
# capitalf = capitalin*(1+(int_anual/100))^num_annos

capitalin = float(input("Cantidad a invertir: "))
int_anual = float(input("Interés anual: "))
num_annos = int(input("Números de años: "))

capitalf = round(capitalin*(1+(int_anual/100))**num_annos,2)
print(f"Capital: {capitalf}")