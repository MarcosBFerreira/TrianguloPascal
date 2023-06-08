def gerar_triangulo():

    qtd_linhas = int(input('\nDigite a quantidade de linhas: '))

    matriz = [[0 for i in range(qtd_linhas)] for aux in range(qtd_linhas)]

    matriz[0][0] = 1

    # Gerando o Triângulo
    for i in range(1, qtd_linhas):

        for j in range(1, qtd_linhas):
            if j - 1 == 0:
                matriz[i][j - 1] = 1
            matriz[i][j] = int(matriz[i - 1][j - 1] + matriz[i - 1][j])

    return matriz
