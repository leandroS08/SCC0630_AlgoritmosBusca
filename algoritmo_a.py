import math
from matplotlib.pyplot import flag
import numpy as np
from collections import defaultdict

def algoritmo_a(M, vertices, v1, v2):
    f = [ 0 for i in range(len(M)) ]
    novo_f = 0
    g = [ 0 for i in range(len(M)) ]
    h = [ 0 for i in range(len(M)) ]
    pai = [ -1 for i in range(len(M)) ]
    abertos = []
    fechados = []
    rota = []

    for i in range(len(M)):
        h[i] = np.sqrt(pow(vertices[v2][0]-vertices[i][0],2)+pow(vertices[v2][1]-vertices[i][1],2))

    f[v1] = g[v1] + h[v1]

    abertos.append(v1)

    flag = False

    while len(abertos) > 0 and flag == False:
        #print("oi")
        i_melhor =  abertos[0]
        for i in range(len(abertos)):
            if(f[i_melhor] > f[abertos[i]]):
                i_melhor = abertos[i]

        v = i_melhor

        rota.append(v)

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
                    abertos.append(u)
        
        abertos.remove(v)
        fechados.append(v)

    #print("\nPai:")
    #print(pai)

    return rota

