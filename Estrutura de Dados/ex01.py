import random
import time
random.seed(time.time())
nome = str(input('Qual o seu nome?'))
n1 = 20
mag = 99
x=1
while(n1 != mag):
    mag = (random.randint(1,10))
    n1 = int(input('\033[0;30;45m Digite o nº de 0 a 10:\033[m'))
    print('\033[0;30;45m O nº da máquina foi {}\033[m'.format(mag))
    if(n1 == mag):
        print('''\033[0;30;45m 
        PARABÉNS, {}
            VOCÊ GANHOU DA MÁQUINA DEPOIS DE {} TENTATIVA(S).\033[m
        '''.format(nome,x))
    elif(n1>10)or(n1<0):
        print('''\33[0;33;41m
                    POOOOOOORRAAA, {} FALEI DE 0 A 10 PQ VC NÃO FEZ DO JEITO Q FALEI
        \33[m'''.format(nome))
    x=x+1