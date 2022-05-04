import random
import time

def bubble(y):
    x = y[0:len(y)]
    ini = time.time()
    n = len(x)-1
    for i in range(0, n):
        for j in range(n-1, i-1, -1):
            if x[j]>x[j+1]:
                t = x[j]
                x[j] = x[j+1]
                x[j+1] = t
    fim = time.time()
    print ('''\n\n Tempo de Resposta Bubble: {} segundos\n\n'''.format(fim - ini))
    return x

x = []
for i in range(0, 1000):
    x.append(random.randint(0, 1000))
k = bubble(x)
print(k)