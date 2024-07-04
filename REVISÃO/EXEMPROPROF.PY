import numpy as np

def gerar_problema_matematico():
    a = np.random.randint(1, 11)
    b = np.random.randint(1, 11)
    operacao = np.random.choice(['+', '-'])
    if operacao == '+':
        resultado = a + b
    else:
        resultado = a - b
    return a, b, operacao, resultado

def jogo_batalha_naval():
    tabuleiro = np.zeros((5, 5), dtype=int)
    posicao_navio = (np.random.randint(0, 5), np.random.randint(0, 5))
    tentativas = 0
    acertou = False
    dicas_usadas = 0
    
    while not acertou:
        print("\nTabuleiro:")
        print(tabuleiro)
        print(f"Tentativas: {tentativas}")
        print(f"Dicas usadas: {dicas_usadas}")
        
        a, b, operacao, resultado = gerar_problema_matematico()
        print(f"Resolva o problema: {a} {operacao} {b} = ?")
        resposta = int(input("Sua resposta: "))
        
        if resposta == resultado:
            linha = int(input("Adivinhe a linha (0-4): "))
            coluna = int(input("Adivinhe a coluna (0-4): "))
            tentativas += 1
            if (linha, coluna) == posicao_navio:
                print(f"Você acertou o navio em {tentativas} tentativas!")
                acertou = True
            else:
                tabuleiro[linha, coluna] = -1
                print("Errou! Tente novamente.")
        else:
            print("Resposta incorreta. Tente novamente.")
        
        if not acertou:
            dica = input("Deseja uma dica? (s/n) ")
            if dica.lower() == 's':
                dicas_usadas += 1
                tentativas += 1
                dica_linha, dica_coluna = np.random.randint(0, 5), np.random.randint(0, 5)
                while (dica_linha, dica_coluna) == posicao_navio:
                    dica_linha, dica_coluna = np.random.randint(0, 5), np.random.randint(0, 5)
                print(f"A dica é: Tente a posição ({dica_linha}, {dica_coluna})")
                tabuleiro[dica_linha, dica_coluna] = -2

jogo_batalha_naval()