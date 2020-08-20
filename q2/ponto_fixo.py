# seja g:[a,b]->R
# 0. g tem que ser contínua
# 1. g(x)\in [a,b] para todo x\in[a,b] é o mesmo que g([a, b])\subset[a,b]
# 2. |g'(x)| < 1 para todo x\in[a,b]
# f(x) = 0 <--> g(x) = x
from math import *
intervalos = [(2,3), (2, 3), (2, 2.5), (2, 3), (1, 2), (1, 2), (1, 2), (2, 3)]

F = ["x**2 - 7",
    "x**3 - 11",
    "x**3 - 11",
    "x**3 - 11",
    "e**x - 2*x - 1",
    "x**3 - x - 4",
    "x**4 - x**2 - 5",
    "sin(x) - 2*x + 4"
    ]

G = ["1/2*(x+7/x)", #1
    "1/2*(x+11/x**2)", #2
    "(11/x)**(1/2)", #3
    "x-(x**3-11)/(3*x**2)", #4
    "log(2*x+1)", #5
    "(x+4)**(1/3)", #6
    "(x**2+5)**(1/4)", #7
    "(sin(x)+4)/2"] #8

def function(funcao, x):
    return eval(funcao)

for num in range(8):
    g = G[num]
    f = F[num]
    chute = intervalos[num]
    n = 10
    print()
    a, b = chute
    x0 = (a+b)/2
    print("##### Questão", num+1, "\nIntervalo procurado:",chute ,"||Ponto procurado:",x0, "|| Numero de iterações:", n)
    print()
    for i in range(n):
        x0 = function(g, x0)
        # print(i, x0, f(x0))
        print("Iteração", i+1, ":", x0, " -> f(x)=",function(f, x0), "\n")
