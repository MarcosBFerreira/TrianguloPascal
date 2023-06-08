from gerando_triangulo import gerar_triangulo


def primeira_propriedade():

    print('')
    matriz = gerar_triangulo()

    for i in range(len(matriz)):

        for j in range(len(matriz)):

            if matriz[i][j] == 1:

                matriz[i][j] = f'\33[31m1\33[m'

            if matriz[i][j] != 0:

                print(matriz[i][j], end=' ')

        print('')

    print('\nExplicação da propriedade\n')


def segunda_propriedade():

    print('')
    matriz = gerar_triangulo()

    for i in range(len(matriz)):

        for j in range(len(matriz)):

            if matriz[i][j] == 1:
                matriz[i][j] = f'\33[31m1\33[m'

            if matriz[i][j] != 0:
                print(matriz[i][j], end=' ')

        print('')

    print('\nExplicação da propriedade\n')