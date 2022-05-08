from bubbleSort import NaoOtima
obj = NaoOtima()
n = 5000
a = []
for i in range(0, n):
    a.append(n-i)
a = obj.bubbleSort(a)
print(a)
