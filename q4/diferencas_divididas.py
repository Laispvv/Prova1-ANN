pnts = [
    [(-2.5,0.89),(-2.0,-1.18),(-1.5,1.88),(-1.0,4.06),(-0.5,1.21)],
    [(-2.5,-3.99),(-2.0,-5.26),(-1.5,0.54),(-1.0,-4.29),(-0.5,-2.59),(0.0,-0.95),(0.5,-0.15)],
    [(-2.5,0.94),(-2.0,-3.08),(-1.5,5.33),(-1.0,2.57),(-0.5,-5.94),(0.0,4.39),(0.5,-2.35),(1.0,0.17),(1.5,5.38),(2.0,-1.13),(2.5,-2.63)],
    [(-2.5,-5.6),(-2.0,-4.03),(-1.5,-0.4),(-1.0,-1.12),(-0.5,1.51),(0.0,2.98),(0.5,-4.59),(1.0,0.56),(1.5,-4.43),(2.0,-5.53),(2.5,2.14),(3.0,4.02),(3.5,0.85),(4.0,1.37),(4.5,5.26),(5.0,2.79),(5.5,5.16),(6.0,-2.28),(6.5,-2.9),(7.0,-0.61),(7.5,-3.93),(8.0,2.04),(8.5,5.61),(9.0,-2.09),(9.5,1.55),(10.0,-0.59),(10.5,-5.47),(11.0,-5.5),(11.5,2.64),(12.0,2.0),(12.5,5.1)]
    ]
for num in range(4):
    print("##### Questão", num+1)
    print()
    pontos = pnts[num]
    xs, ys = zip(*pontos)
    n = len(pontos)

    # auxiliares
    def prod(lista):
        p = 1
        for i in lista:
            p *= i
        return p

    def sign(x):
        if x < 0:
            return str(x)
        return f'+{x}'

    # algoritmo
    def tabela(pontos):
        Y = {}
        Y[0] = {k: v for k, v in enumerate(ys)}
        for j in range(1, n):
            Y[j] = {}
            for i in range(n - j):
                Y[j][i] = (Y[j - 1][i + 1] - Y[j - 1][i]) / (xs[j + i] - xs[i])
        return Y

    t = tabela(pontos)
    a = [v[0] for k, v in t.items()]

    def p(x):
        soma = 0
        for k in range(n):
            termo_k = prod([(x - xi) for i, xi in enumerate(xs) if i < k])
            soma += a[k] * termo_k
        return soma

    def eq(coefs):
        equation = ""
        for k in range(n):
            termo_k = "*".join([f'(x{sign(-xi)})' for i, xi in enumerate(xs) if i < k])
            if k == 0:
                equation += str(a[k])
            else:
                equation += f'{sign(a[k])}*' + termo_k
        return equation

    poly = eq(a)
    print("p(x) =",poly)

# ============ Parte que plota o gráfico =============================
    # Método das diferenças divididas (de Newton)
    #
    # import matplotlib.pyplot as plt
    # import numpy as np
    #
    # def poly_f(x):
    #     return eval(poly)
    #
    # a, b = min(xs) - 0.5, max(xs) + 0.5
    # t = np.arange(a, b, 0.01)
    # plt.scatter(xs, ys)
    # plt.plot(t, poly_f(t), color="red", label="polinômio interpolador")
    # plt.show()
