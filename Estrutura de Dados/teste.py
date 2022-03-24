def buscaSeq(x, proc):
    for i in range(0, len(x)):
        if x[i] == proc:
            return i
    return -1

x = [2, 1, 4, 5, 7, 9, 10, 8, 3]
i = 0
k = buscaSeq(x, 0)
if k >= 0:
    print('''{} está na posição {} do vetor'''.format(i, k))
else:
    print('''{} não se encontra no vetor'''.format(i))