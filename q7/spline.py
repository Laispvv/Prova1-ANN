import matplotlib.pyplot as plt
import numpy as np

def function(funcao, x):
    return eval(funcao)

#=============== pra quando tem função=====================
funcoes = ["1 / (1 + x**2)",#1
            "1 / (1 + x**2)",#2
            "1 / ((1 + x**2)**(1/2))",#3
            "2 / (1 + x**2)", #4
            "2 / (1 + x**2)" #5
            ]
xss = [[-2, -1, 1, 2],
    [-2, -1, 0, 1, 2],
    [0, 0.3, 0.9, 1.3, 2],
    [-1.97, -1.16, -0.34, 0.32, 0.38, 0.61, 1.09, 1.44, 1.81, 1.825],
    [-4.65, -4.62, -4.39, -4.25, -4.01, -3.6, -3.52, -2.62, -0.75, 0.47, 0.77, 0.78, 1.44, 2.45, 2.91, 3.06, 3.17, 3.7, 4.49, 4.83],
    ]

pnts = []
#gera a lista de pontos pra todas as funções e conjuntos de x
for gerarPontos in range(5):
    f = funcoes[gerarPontos]
    xs = xss[gerarPontos]
    pontos = [(xn, function(f, xn)) for xn in xs]
    pnts.append(pontos)

#======================pra quando tem ponto ======================================
# pontos = []
#==================================================================================

for num in range(5): # gera os 5 polinômios
    print("##### Questão", num+1)
    print()
    pontos = pnts[num] #pontos da questão
    xs = xss[num] #x's da questão
    f = funcoes[num]#pega a função da questão

    xs, ys = zip(*pontos)
    n = len(xs) - 1
    h = [xs[k+1] - xs[k] for k in range(n)]

    # Matrix (N+1) por (N+1) ou len(pontos) por len(pontos)
    matrix = []
    first_row = [1] + [0 for _ in range(n)]
    matrix.append(first_row)
    for i in range(1, n):
        zeros_before = [0 for _ in range(i - 1)]
        zeros_after = [0 for _ in range(i + 1, n)]
        row = zeros_before + [h[i - 1], 2 * (h[i - 1] + h[i]), h[i]] + zeros_after
        matrix.append(row)
    last_row = [0 for _ in range(n)] + [1]
    matrix.append(last_row)

    B = [0] + [3 * (ys[k+1] - ys[k]) / h[k] - 3 * (ys[k] - ys[k-1]) / h[k-1] for k in range(1, n)] + [0]

    solucao = np.linalg.solve(matrix, B)

    c = [v for v in solucao]
    b = [(ys[k+1] - ys[k]) / h[k] - h[k] * (2 * c[k] + c[k+1]) / 3 for k in range(n)]
    d = [(c[k+1] - c[k]) / (3 * h[k]) for k in range(n)]

    eq = [f'{ys[k]}{b[k]:+.2f}*(x{-xs[k]:+}){c[k]:+.2f}*(x{-xs[k]:+})**2{d[k]:+.2f}*(x{-xs[k]:+})**3' for k in range(n)]
    for i in range(n):
        print(f"eq {i}:", eq[i])

    plt.figure()
    for i in range(n):
        a, b, inc = xs[i], xs[i + 1], 0.001
        t = np.arange(a, b + inc, inc)
        plt.plot(t, function(eq[i], t))

    plt.scatter(xs, ys)
    # plt.show()
    plt.savefig(f"/home/lais/Documents/Aula/ANN/prova1/q7/f{num}.png", dpi=400)
