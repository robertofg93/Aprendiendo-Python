#if

# Sintaxis if-else
  # if condicion:
  #   <accion>
  # elif condicion:
  # else:
  #   <accion>    

#Ejemplo 1
x = 40

if x < 30:
    print("x es menor que 30")
else:
    print("x es mayor que 30")

#Ejemplo 2
color = "rojo"

if color == "verde":
    print("El color es verde")
elif color == "azul":
    print("El color es azul")
else:
    print("Ningún color")

# Ejemplo if anidado
name = "Juan"
last_name = "Perez"

if name == "Juan":
    if last_name == "Perez":
        print(f"Tu eres: {name}{last_name}")
    else:
        print(f"Tu no eres:{name}{last_name}")
else:
    print(f"Tu no eres: {name}")