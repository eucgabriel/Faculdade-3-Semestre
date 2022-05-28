from No import No


class Lista:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def add(self, value):
        if self.first:
            aux = self.first
            ant = None
            while(aux.next):
                ant = aux
                aux = aux.next
            aux.next = No(value)
            aux.next.ant = aux
            aux.ant = ant
            if self.last:
                self.last = aux.next
        else:
            self.first = No(value)
            self.last = No(value)
        self.size += 1

    def Ordenada(self):
        if self.first == None:
            print("Empty List")

        aux = self.first
        while(aux):
            print(aux.report)
            aux = aux.next
        print("Sum: " + str(self.size))
        print("\n -----------------\n")

    def visitaInvertido(self):
        aux = self.last
        print("Lista Inversa: " + str(self.size))
        while(aux):
            print(aux.report)
            aux = aux.ant
        print("Sum: " + str(self.size))
        print("\n -----------------\n")
        
lista = Lista()

lista.add(2)
lista.add(5)
lista.add(12)
lista.add(20)
lista.Ordenada()
lista.visitaInvertido()
