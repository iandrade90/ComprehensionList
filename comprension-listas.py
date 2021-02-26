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


