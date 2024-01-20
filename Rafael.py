import random

print("Bem-vindo ao Jogo dos Países!")

while True:
    print("\nMenu:")    #Menu do ínicio
    print("1. Start")
    print("2. Quit")
    escolha = input('Escolha uma opção: ')

    if escolha == '1':  #escolha 1
        print("Vamos começar!\n")
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        letra_aleatoria = random.choice(letras)

        print(f'A letra aleatória é: {letra_aleatoria}\n')
        categorias = ['Nome','País','Cidade', 'Animal', 'Marca', 'Objeto', 'Cor', 'Alimento']

        for categoria in categorias:
            while True:
                palavra = input(f'Digite um(a) {categoria} que comece com a letra {letra_aleatoria}: ')
                if palavra.lower().startswith(letra_aleatoria.lower()):
                    print(f'{categoria}: {palavra}\n')
                    break
                else:
                    print(f'Erro! A {categoria} deve começar com a letra {letra_aleatoria}. Tente novamente.')
        print("Ganhaste, Parabens!")
        break

    elif escolha == '2':    #escolha 2
        print("Até á proxima!")
        break
    else:
        print("Opção inválida. Escolha novamente.")