demo_list = [ 1, 'hello', True , 1.34, [ 1, 2, 3]]
colors = [ 'red', 'blue', 'green']

numers_list = list((1, 2)) #la listas solo soportan un elemento para pasarle varios 
                            #elementos hay que pasar una tupla
print(numers_list)

#range() #palabra reservada que define un rango
list(range(1, 10)) #crea una lista basada un en rango
ls = list(range(1, 10))
print(ls)


print('green' in colors) #devuelve si se encuentra green en la lista colors
print(colors)

colors[1] = 'yellow' #cambia un elemento de la lista por otro
print(colors)

colors.append('violet') #método que agrega un elemento a la lista, solo puede agregar un elemento a la vez
print(colors) 

colors.extend(['black', 'white']) #método que te permite extender la lista través de otra lista
print(colors)

colors.insert(1,'pink') #inserta pink en posición 1 de la lista
print(colors)

colors.pop() #elimina un elemento de la lista por defecto el último
print(colors)

colors.remove('red') #elimina un elemento específico de la lista
print(colors)

colors.clear() #limpia de elementos la lista
print(colors)

colors.sort() #organiza la lista en orden alfabetico si son strings y en orden numerico si son números
print(colors) #si se quiere cambiar el orden se le debe pasar al método reverse=True

colors.index('blue') #método que devuelve la posición del elemento en la lista
print(colors)

colors.count('blue') #cuenta la cantidad de elementos de el tipo determinado en la lista 
print(colors)