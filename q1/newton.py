from sympy import *
from math import *
#informações pra questão Q1
# intervalos = [(-5, 5), (-5, 5), (0.001, 5), (0.001, 5), (-5, 5), (-5, 5), (0.001, 5), (-5, 5), (-5, 5), (-5, 5)]
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
    # x = symbols('x')
    return eval(funcao)

# num = int(input("Digite o numero da questão pra resolver (1-10):"))
num = int(input())
num -= 1

f = str(funcoes[num])
df = str(diff(f, 'x', 1))
x0 = 1
n = 10 #numero de iterações

print("##### Questão", num+1, "\nChute inicial:", x0,"|| Numero de iterações:", n)
print()

# print(f,df)
# itr = {}
itr = [x0]
for i in range(1, n+1):
    x0 = x0 - function(f, x0) / function(df, x0)
    itr.append(x0)
    print("Iteração", i, ":", x0,"||")

# for i in range(n+1):
    # print(k, v, function(f, v))
