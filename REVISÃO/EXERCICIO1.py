matriz = [
    [35, 2, 3],
    [4, 5, 25],
    [7, 50, 60]
]


valormaior_10 = []

for linha in matriz: 
    for valor in linha:
        if valor > 10: 
            valormaior_10.append(valor)


print(valormaior_10)