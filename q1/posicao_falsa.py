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

def function(f, x):
    return eval(f)

intervalos = [(1, 2), (-5, 5), (0.001, 5), (0.001, 5), (2, 3), (2, 3), (0.001, 5), (-5, 5), (-5, 5), (-5, 5)]
n = 10
for num in range(10):
    chute = intervalos[num]
    f = funcoes[num]
    a, b = chute
    print("##### Questão", num+1, "\nChute iniciais:",chute ,"|| Numero de iterações:", n)
    print("Iteração", 1, ":", a, "||")
    print("Iteração", 2, ":", b, "||")
    for i in range(2, n):
        try:
            xn = (a * function(f, b) - b * function(f, a)) / (function(f, b) - function(f, a))

        except:
            print(f"Divisão por zero para {a}, {b} na iteração {i}")
            break
        if function(f, xn) == 0:
            print('Achou raiz antes de 10 iterações!!', xn)
            break
        elif function(f, a) * function(f, xn) < 0:
            b = xn
        else:
            a = xn
        print("Iteração", i+1, ":", xn,"||")
