myStr = 'Hello World Roberto'
#print (dir(myStr)) #devuelve todos los métodos de un string  

print(myStr.upper()) #string usando su método upper (convierte todo a mayúscula)

name = 'HOLA ROBERTO'
print (name.lower()) #método para convertir todo a minúscula 
print (name.swapcase()) #método para convertir las mayúsculas a minúscula y viceversa
print (name.capitalize()) #método para convertir las palabra inicial a mayúscula
print (name.replace('O', 'A')) #método para remplazar un caracter por otro
  

print (myStr.endswith ('Hello')) #pregunta si termina el texto en 'Hello'
print (myStr.count ('e')) #cuenta la cantidad de caracteres
print (myStr.split()) #método para separar un string por un valor determinado por defecto es ('')
print (myStr.split(',')) #ejemplo de lo anterior
print (myStr.find('o')) #permite encontrar el caracter 'o'
print (len (myStr)) #develve la longitud de un string
print (myStr.index ('e')) #devuelve la posición en que se encuentra el caracter
print (myStr.isnumeric()) #pregunta si el string es de tipo númerico
print (myStr[4]) #devuelve el caracter en la 4ta posición