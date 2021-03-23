#Una panadería vende barras de pan a 3.49€ cada una. 
#El pan que no es el día tiene un descuento del 60%. 
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
#Después el programa debe mostrar el precio habitual de una barra de pan, 
#el descuento que se le hace por no ser fresca y el coste final total.

#Solución
pan = 3.49
pan_viejo = pan * 0.6
cant_panviejo = int(input("Ingrese el número de barras vendidas que no son del día: "))
costefinal = cant_panviejo*pan_viejo*(1-0.6)

print(f"El precio habitual de una barra de pan es: {pan}",
f"El precio de un pan que no es fresco es: {pan_viejo}", 
f"el coste total es {costefinal}")