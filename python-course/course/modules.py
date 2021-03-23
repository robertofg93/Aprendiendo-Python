#Existen tres tipos de módulos
#-El creado por uno mismo
#-El de terceros
#-Librerías de python

import datetime #módulo de python que se encarga de la hora del sistema
#Ejemplo 1
print(datetime.date.today())

#Ejemplo 2
print(datetime.timedelta(minutes=80))

#Ejemplo 3
#otra forma de definir los módulos
from datetime import timedelta
print(timedelta(minutes=100))

#Ejemplo 4
from datetime import timedelta, date
print(date.today())


#Ejemplo 5
from fmath import sum, rest
sum(3,4)
rest(4,3)

