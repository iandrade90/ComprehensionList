#Diferentes ejercicios de comprension de listas
#Different exercises of lists comprehension

#Lista por extension a = [1, 2, 3, 4, 5, 6]
#Lista por comprension a = [n for n in range(1, 7)]

# Crear un lista tomando en cuenta cierto rango
# Creating a list within a range

a = [n for n in range(1, 7)]

#print(a)

# Primeras 10 potencias de 2
# First 10 squares of 2

b = [2 ** n for n in range(10)]

#print(b)

# Obtener todos los numeros que son multiplos de 7 en un range
# Getting all the numbers multiples by 7 within a range

c = [n for n in range(100) if n % 7 == 0]

#print(c)

# Combinar listas de lista
# Combine lists of list

d = [['Camisa roja', 'Camisa azul', 'Camisa verde', 'Camisa amarilla'], ['Pantalon negro', 'Pantalon blanco']]

d_a = [(n, x) for n in d[0] for x in d[1]]

#print(d_a)

# O Or

eA = ['Camisa roja', 'Camisa azul', 'Camisa verde', 'Camisa amarilla']
eB = ['Pantalon negro', 'Pantalon blanco']

eC = [(n, x) for n in eA for x in eB]

#print(eC)

# Imprimir elemento de la lista si concuerda con un parametro pasado
# Print an element of a list if a given parameter matches 

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in fruits if 'a' in x]

#print(newlist)

# Colocar primera letra en mayuscula
# Capitalize first letter

newlist2 = [x.capitalize() for x in fruits]

#print(newlist2)

# Colocar todas las letras en mayuscula
# Upper case all letters

newlist3 = [x.upper() for x in fruits]


#print(newlist3)

#Trabajando con diccionarios
#working with Dictionaries

# Acceder a las keys de un diccionarios como listas
# Accesing to the keys of a dict as lists

dict_one = {
  'Marca': 'Fiat',
  'Modelo': 'Palio',
  'Año': '2014'
}

itr = [[k for k in dict_one[v]] for v in dict_one.keys()]

#Muestra cuales son las keys relacionados a los values
#Shows the keys related to the values

itr2 = [v for v in dict_one.values()]

#Muestra cuales son los values relacionados a las keys
#Shows the values related to the keys

itr3 = [v for v in dict_one.keys()]

#print(itr2)
#print(itr3)

#Muestra values y keys en tuplas
#Tuples the values and keys

itr4 = [v for v in dict_one.items()]

#print(itr2)
#print(itr3)
#print(itr4)

#Copiar una lista
#Copy a list

list_to_copy = [1, 2, 3, 4, 5, 6]
copied_list = [element for element in list_to_copy]

#print(copied_list)