#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, y 
# muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

# Nota: IMC = masa/(estatura)2

#Solución
masa = input("Entre el peso corporal en kg: ")
estatura = input("Entre la estatura en m: ")

imc = float(masa)/(float(estatura)**2)
print(round(imc,2))                    #la función round() toma como argumento un número float y retorna un int
                                       #según las reglas de redondeo.
                                       #Un segundo argumento indica la cantidad de digítos a tomar en cuenta después
                                       #de la coma.
