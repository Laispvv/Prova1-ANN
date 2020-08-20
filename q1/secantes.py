from math import *

funcoes = ["x**5 - 8*x - 2", #1
    "cos(x**2) - x", #2
    "log(x) + x**2", #3
    "log(x**2) + 2*x", #4
    "cos(sin(x**2)) + x**3 - 2", #5
    "e**(-x**2) - x**2 + 5", #6
    "e**(cos(x)) + log(x**2)", #7
    "x**2 * cos(x) + x -1", #8
    "2*cos(e**x)-x", #9
    "x**3 + x**2 + 0.001"] #10

def function(funcao, x):
    return eval(funcao)
for num in range(10):
    # num = int(input("Digite o numero da questão pra resolver (1-10):"))
    # num = int(input())
    # num -= 1

    n = 10
    chute = [0.1,0.5]
    x0, x1 = chute
    itr = {}
    itr[0] = x0
    itr[1] = x1

    f = funcoes[num]
    print("##### Questão", num+1, "\nChute iniciais:",chute ,"|| Numero de iterações:", n)
    print()

    print("Iteração", 1, ":", x0, "||")
    print("Iteração", 2, ":", x1, "||")
    a, b = x0, x1
    for i in range(2, n):
        try:
            xn = (a * function(f, b) - b * function(f, a)) / (function(f, b) - function(f, a))
        except:
            print(f"Divisão por zero para {a}, {b} na iteração {i}")
            break
        if function(f, xn) == 0:
            print("Achou a raiz antes de 10 iterações!!")
            break
        itr[i + 2] = xn
        a, b = b, xn
        print("Iteração", i+1, ":", xn,"||")
