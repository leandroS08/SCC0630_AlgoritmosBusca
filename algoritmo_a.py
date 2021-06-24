import math
from matplotlib.pyplot import flag
import numpy as np
from collections import defaultdict

def algoritmo_a(M, pos, v1, v2):
    f = [ 0 for i in range(len(M)) ]
    novo_f = 0
    g = [ 0 for i in range(len(M)) ]
    h = [ 0 for i in range(len(M)) ]
    pai = [ -1 for i in range(len(M)) ]
    abertos = []
    fechados = []

    #print("\nCoisa de posição:")
    #print (pos)
    #item = pos[0]
    #print (item)

    f[v1] = g[v1] + h[v1]

    abertos.append(v1)

    flag = False

    while len(abertos) > 0 and flag == False:
        i_melhor =  0
        for i in range(len(M)):
            if(f[i_melhor] < f[i]):
                i_melhor = i

        v = abertos[i_melhor]

        print("\nPai:")
        print(pai)

        if (v == v2):
            flag = True
    
        for u in range(len(M)):
            if(M[v][u] != 0):
                novo_f = g[v] + M[v][u] + h[u]
                
                if( (u in abertos or u in fechados) and (novo_f >= f[u])):
                    continue
                else:
                    pai[u] = v
                    g[u] = g[v] + M[v][u]
                    f[u] = novo_f

                    if u in fechados:
                        fechados.remove(u)
                    if u in abertos:
                        abertos.remove(u)
                    abertos.append(u)
        fechados.append(u)

    print("\nPai:")
    print(pai)

    return 0

