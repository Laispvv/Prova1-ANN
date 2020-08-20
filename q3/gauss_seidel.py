M = [
    [[4, 1, 1, 6], [2, 5, 2, 3], [1, 2, 4, 11]],
    [[3, 2, 1, 2], [2, 7, 2, -3], [1, 3, 5, 3]],
    [[1, 2, -3, 5], [0, -2, 1, -3], [-4, 1, -1, -2]],
    [[3, 1, 1, 1], [1, -4, 2, 3], [1, -3, 5, -1]]
    ]
for num in range(4):
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
            chute = xn + chute[len(xn):] # this line updates chute
            subs = sum([el * chute[k] for k, el in enumerate(row[:-1]) if k != j])
            subs = (row[-1] - subs) / row[j]
            xn.append(subs)
        chute = xn
        print("Iteração", i+1, ":", chute,"||")
