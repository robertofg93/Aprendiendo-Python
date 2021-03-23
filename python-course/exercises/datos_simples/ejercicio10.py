#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así 
#que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
#Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y 
#muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

#Solución
cant_payasos = int(input("Entre la cantidad de payasos: "))
cant_munnecas = int(input("Entre la cantidad de muñecas: "))
  
pqt = (cant_payasos*112) + (cant_munnecas*75)
print(f"El peso total del pqt es {pqt}")

