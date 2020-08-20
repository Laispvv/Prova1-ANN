#1) [[4, 1, 1, 6], [2, 5, 2, 3], [1, 2, 4, 11]] -> [1, -1, 3]
M = [
    [[4, 1, 1, 6], [2, 5, 2, 3], [1, 2, 4, 11]],
    [[3, 2, 1, 2], [2, 7, 2, -3], [1, 3, 5, 3]],
    [[1, 2, -3, 5], [0, -2, 1, -3], [-4, 1, -1, -2]],
    [[3, 1, 1, 1], [1, -4, 2, 3], [1, -3, 5, -1]]
    ]
for num in range(4):
    print("##### Questão", num+1, "\nLista de operações realizadas:\n")
    m = M[num]
    tam = len(m[0])-1
    #PARTE QUE ESCALONA A MATRIZ
    # garantindo que o pivô não é zero
    for pivo in range(tam):
        if m[pivo][pivo] == 0:
            #quando o pivo é zero, buscamos os elementos abaixo do pivô(mesma coluna)
            for troca in range(tam):
                if m[troca][pivo] != 0:
                    print("Troca de linha", pivo, "com linha", troca)
                    m[pivo], m[troca] = m[troca], m[pivo] #troca as linhas
                    break
            else:
                print("coluna igual a zero")
        #percorrendo a coluna abaixo do pivô para zerar ele
        for coluna in range(pivo+1, tam):
            #achando qual é o número que devemos multiplicar por outro para zerar o digito abaixo do pivô
            delta = -m[coluna][pivo] / m[pivo][pivo]
            for linha in range(tam+1):
                print(f"L{coluna}-> {delta}*L{pivo} + L{coluna}\n")
                m[coluna][linha] = m[pivo][linha]*delta + m[coluna][linha]

    # for linha in range(tam):
    #     print(*m[linha])

    #PARTE QUE RESOLVE O SISTEMA
    result = [0 for i in range(tam)]

    for linha in range(tam-1, -1, -1):
        soma = 0
        for coluna in range(linha+1, tam):
            soma += result[coluna] * m[linha][coluna]
        #calcula o valor da variavel
        result[linha] = (m[linha][tam]-soma)/m[linha][linha]

    print(f"resultado = {result}")
