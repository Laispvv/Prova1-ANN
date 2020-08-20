from math import *

def N1(h, p):
    return (function(f, p) - function(f,p-h)) / h

def N2(h, p):
    return (function(f, p+h) - function(f,p-h)) / (2*h)

def N3(h, p):
    return (function(f, p-2*h) - 8*function(f,p-h) + 8*function(f,p+h) - function(f,p+2*h)) / (12*h)

#============ para todas as funções de Q8 =================
funcoes = ["cos(x**x)",#1
            "sin(x)", #2
            "x**(cos(x))",#3
            "e**(x**(-2))"#4
            ]

H = [0.1, 0.05, 0.025, 0.0125]
P = 1


def function(funcao, x):
    return eval(funcao)
#=============================================================
for num in range(4):
    print("##### Questão", num+1)
    print("\n```")
    f = funcoes[num]
    for hzinho in H:
        print(f"\nAproximação de f(x) = {f}, com h = {hzinho}\n")
        print(f"F1(h) = {N1(hzinho, P)}\nF2(h) = {N2(hzinho, P)}\nF3(h) = {N3(hzinho, P)}")
    print("```")
