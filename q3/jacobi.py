# E = [[9,1,1,3,6], [2,7,2,1,3], [1,2,6,1, 11], [1,1,1,19,0]] # matrix estendida do sistema
# 4x+y+z=6 --> x = (6 - y - z) / 4
# 2x+5y+2z=3 --> y = (3 - 2x - 2z) / 5
# x+2y+4z=11 --> z = (11 - x - 2y) / 4

M = [
    [[4, 1, 1, 6], [2, 5, 2, 3], [1, 2, 4, 11]],
    [[3, 2, 1, 2], [2, 7, 2, -3], [1, 3, 5, 3]],
    [[1, 2, -3, 5], [0, -2, 1, -3], [-4, 1, -1, -2]],
    [[3, 1, 1, 1], [1, -4, 2, 3], [1, -3, 5, -1]]
    ]
for num in range(4):
    m = M[num]
    tam = len(m[0])-1
    n  = 10
    itr = {}
    chute = [0,0,0]
    print("##### Questão", num+1, "\nChute inicial:",chute, "|| Numero de iterações:", n)
    print()

    def test(matrix, vec):
        err = []
        for row in matrix:
            prod = abs(sum([col * vec for col, vec in zip(row[:-1], vec)]) - row[-1])
            err.append(prod)
        return err


    for i in range(n):
        xn = []
        for j, row in enumerate(M[num]):
            subs = sum([el * chute[k] for k, el in enumerate(row[:-1]) if k != j])
            subs = (row[-1] - subs) / row[j]
            xn.append(subs)
        # print(xn, test(E, xn))
        chute = xn
        print("Iteração", i+1, ":", chute,"||")
