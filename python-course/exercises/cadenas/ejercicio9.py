#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa
#y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también
#funcione cuando el día o el mes se introduzcan con un solo carácter.

#Solución 1
date=input("Introduzca la fecha de su nacimiento en formato dd/mm/aaaa: ")
lista=date.split('/')
print("Dia:",lista[0]), print("Mes:",lista[1]), print("Año:",lista[2])

#Solución 2
date=input("Introduzca la fecha de su nacimiento en formato dd/mm/aaaa: ")
day = date[:date.find('/')]
monthyear = date[date.find('/')+1:]
month = monthyear[:monthyear.find('/')]
year = monthyear[monthyear.find('/')+1:]

print("Dia:",day), print("Mes:",month), print("Año:",year)