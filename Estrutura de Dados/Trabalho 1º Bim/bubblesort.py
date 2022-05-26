import time
class NaoOtima:
	def bubbleSort(self, x):
		n = len(x)-1
		k = 0
		i = 0
		ini = time.time()
		for i in range(0, n):
			trocou = False
			for j in range(n-1, i-1, -1):
				k = k + 1
				if x[j]>x[j+1]:
					trocou = True
					x[i], x[j] = x[j], x[i]
			if not trocou:
				break
		fim = time.time()
		print("Bubble Sort Tempo:", (fim - ini), "\n")
		return x