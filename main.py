from propriedades import primeira_propriedade

continuar = True
opcao = int(input('1 - Demonstrar a Primeira Propriedade\n\n: '))
while opcao != 1:
    if opcao != 1:
        print('\nResposta inválida\n')
    opcao = int(input('1 - Demonstrar a Primeira Propriedade\n\n: '))

while continuar:
    match opcao:

        case 1:
            primeira_propriedade()

    continuar = bool(int(input('Deseja continuar?\n0 - Não\n1 - Sim\n\n: ')))
    opcao = int(input('\n1 - Demonstrar a Primeira Propriedade\n\n: '))
