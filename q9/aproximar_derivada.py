import numpy as np
import matplotlib.pyplot as plt
from math import *
#==================== encontra o polinômio interpolador com vandermond ===========================================
#========= pra quando tem a função ============================================
def function(funcao, x):
    return eval(funcao)

funcoes = ["x**x", #1
        "cos(x)", #2
        "e**x" #3
        ]
X = [[0.99, 1, 1.01], [0.99, 1, 1.01, 1.02], [0.98, 0.99, 1, 1.01]]
pnts = []
for gerarPontos in range(3):
    f = funcoes[gerarPontos]
    xs = X[gerarPontos]
    pontos = [(xn, function(f, xn)) for xn in xs]
    pnts.append(pontos)
#==============================================================================
#======== pra quando tem a lista de pontos ====================================
# pnts = [
#     [(-2.5,0.89),(-2.0,-1.18),(-1.5,1.88),(-1.0,4.06),(-0.5,1.21)],
#     [(-2.5,-3.99),(-2.0,-5.26),(-1.5,0.54),(-1.0,-4.29),(-0.5,-2.59),(0.0,-0.95),(0.5,-0.15)],
#     [(-2.5,0.94),(-2.0,-3.08),(-1.5,5.33),(-1.0,2.57),(-0.5,-5.94),(0.0,4.39),(0.5,-2.35),(1.0,0.17),(1.5,5.38),(2.0,-1.13),(2.5,-2.63)],
#     [(-2.5,-5.6),(-2.0,-4.03),(-1.5,-0.4),(-1.0,-1.12),(-0.5,1.51),(0.0,2.98),(0.5,-4.59),(1.0,0.56),(1.5,-4.43),(2.0,-5.53),(2.5,2.14),(3.0,4.02),(3.5,0.85),(4.0,1.37),(4.5,5.26),(5.0,2.79),(5.5,5.16),(6.0,-2.28),(6.5,-2.9),(7.0,-0.61),(7.5,-3.93),(8.0,2.04),(8.5,5.61),(9.0,-2.09),(9.5,1.55),(10.0,-0.59),(10.5,-5.47),(11.0,-5.5),(11.5,2.64),(12.0,2.0),(12.5,5.1)]
#     ]
#==============================================================================
hs = [1, 1/2, 1/4, 1/8, 1/16, 1/64, 1/128, 1/1024]
x0 = 1 # <- deriva neste ponto

#formulas para as derivadas
def f1(x0, h): # f1
    return (function(eq2, x0 + h) - function(eq2, x0 - h)) / (2*h) #primeira

def f2(x0, h): # f2 com erro h**2
    return (function(eq2, x0 + h) - 2 * function(eq2,x0) + function(eq2,x0 - h)) / h**2 #segunda

def f3(x0, h): # f3
    return ((-1/2)*function(eq2, x0+(-2*h)) + function(eq2,x0+(-1*h)) - function(eq2,x0+(1*h)) + (1/2)*function(eq2,x0+(2*h))) / (h**3) #terceira

for num in range(3):
    print("##### Questão", num+1)
    print()
    f = funcoes[num]
    pontos = pnts[num]
    n = len(pontos)

    def vandermond(pontos):
        xs, ys = zip(*pontos)
        A = [[x ** k for k in range(n)] for x in xs]
        B = ys
        a2 = np.linalg.solve(A, B) #resolve sistema linear
        return a2

    def sign(x):
        if x < 0:
            return str(x)
        return f'+{x}'

    def equation(pontos):
        eq = ""
        eq += "".join([f'{sign(a[k])}*x**{k}' for k in range(n)])
        return eq

    a = vandermond(pontos)
    eq2 = equation(pontos)
    print(f"Polinômio encontrado:\np(x) = {eq2}\n")

#===================== PARTE PARA APROXIMAR A DERIVADA DO POLINÔNIMO GERADO ================================

    for hzinho in hs:
        print("Para o polinômio encontrado essas são as aproximações para cada derivada:\n```")
        print(f"f1(x0) = {f1(x0, hzinho)}, com h = {hzinho}\n")
        print(f"f2(x0) = {f2(x0, hzinho)}, com h = {hzinho}\n")
        if(num != 0):
            print(f"f3(x0) = {f3(x0, hzinho)}, com h = {hzinho}\n")
        print("```")
