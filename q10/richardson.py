from math import *
N = [1, 2, 4] # ordem do erro
x0 = 1 #ponto para derivar
p = 1 #b
H = [0.1, 0.05, 0.025, 0.0125]

funcoes = ["cos(x**x)",#1
            "sin(x)", #2
            "x**(cos(x))",#3
            "e**(x**(-2))"#4
            ]
dfs = ["(f(p)-f(p-h))/h",#f1
        "(f(p+h)-f(p-h))/(2*h)",#f2
        "(f(p-2*h)-8*f(p-h)+8*f(p+h)-f(p+2*h))/(12*h)"#f3
        ]

def function(funcao, x):
    return eval(funcao)

for num in range(3):
    print("##### Questão", num+1)
    print()
    for hzinho in range(4):
        #definições
        h = H[hzinho]
        df = dfs[num]
        n = N[num]

        def f(x):
            return eval(funcoes[num])

        def Fk(h, n, p):
            # I'm recursive :)
            if n == 1:
                return function(df, h)
            n -= 1
            return (2 ** (n * p) * Fk(h/2, n, p) - Fk(h, n, p)) / (2 ** (n * p) - 1)

        print(f"Aproximação O(h**{n}): {Fk(h, n, p)} -> com h = {h}\n")
