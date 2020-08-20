import math

#informações pra questão Q1
intervalos = [(-5, 5), (-5, 5), (0.001, 5), (0.001, 5), (-5, 5), (-5, 5), (0.001, 5), (-5, 5), (-5, 5), (-5, 5)]
funcoes = ["x**5 - 8*x - 2", #1
    "math.cos(x**2) - x", #2
    "math.log(x) + x**2", #3
    "math.log(x**2) + 2*x", #4
    "math.cos(math.sin(x**2)) + x**3 - 2", #5
    "math.pow(math.e, -x**2) - x**2 + 5 ", #6
    "math.pow(math.e, math.cos(x)) + math.log(x**2)", #7
    "x**2 * math.cos(x) + x -1", #8
    "2*math.cos(math.e**x)-x", #9
    "x**3 + x**2 + 0.001"] #10

#algoritmo
# num = int(input("Digite o numero da questão pra resolver (1-10):"))
num = int(input())
num -= 1
a, b = intervalos[num]
f = funcoes[num]
vetorItera = []
n = 10 # número de iterações
print("##### Questão", num+1, "\nIntervalo:", intervalos[num],"|| Numero de iterações:", n)
print()

def function(funcao, x):
    return eval(funcao)

for i in range(n):
    m = (a + b) / 2
    if function(f, m) == 0:
        print('A raiz é:', m)
    elif function(f, m) * function(f, a) < 0: # teorema de Bolzano
        b = m
    else:
        a = m
    print("Iteração", i+1, ":", m)
