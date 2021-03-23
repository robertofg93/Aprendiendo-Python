# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros 
# tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

#Solución
dinero = float(input("Ingrese la cant de dinero depositado en el banco: "))

primer_anno = round((dinero*(1+ 0.04)),2)
segundo_anno = round(primer_anno*(1 + 0.04),2)
tercer_anno = round(segundo_anno*(1 + 0.04),2)
print(f"Primer año: {primer_anno}, Segundo año: {segundo_anno}, Tercer año: {tercer_anno}")