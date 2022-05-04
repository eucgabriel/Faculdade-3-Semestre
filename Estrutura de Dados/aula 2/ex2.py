def selection(x):
    n = len(x)
    for i in range(0, n-1):
        ordenado = True
        for j in range(i+1, n):
            if x[i]>x[j]:
                x[i], x[j] = x[j], x[i]
            print('''{} - {} - {}'''.format(i, j, x))
            ordenado = False
        if ordenado:
            return x
    return x 
x = [1, 7, 8, 9, 13, 26]
print(selection(x))