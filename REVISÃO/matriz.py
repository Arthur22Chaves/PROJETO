import numpy
# Cria uma matriz 9x9 com valores aleatórios entre 0 e 20
matrix = numpy.random.randint(0, 15, size=(3, 3))
# Exibe a matriz completa
print("Matriz completa:")
print(matrix)
# Filtra e exibe os valores maiores que 10
valores_maiores_que_10 = matrix[matrix > 10]
print("\nValores maiores que 10:")
print(valores_maiores_que_10)