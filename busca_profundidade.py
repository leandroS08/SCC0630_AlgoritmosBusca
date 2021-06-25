
from collections import defaultdict

#NOTE: É utilizada a lista de adjacências, então a matriz é convertida na lista
def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > 0:
                adjList[i].append(j)
    return adjList

def DFS(lista, visitados, inicio, fim, rota):
    rota.append(inicio)
    visitados[inicio] = 1

    if inicio == fim:
        #print(rota)
        return rota
    else:
        for v in lista[inicio]:
            if visitados[v] == 0 and v != 0:
                caminho = DFS(lista, visitados, v, fim, rota)
                if caminho is not None:
                    return rota
    rota.pop()
    visitados[inicio] = -1

def busca_profundidade(matriz, inicio, final):
    visitados = [0 for i in range(len(matriz) + 1)]
    lista = convert(matriz)
    rota = []

    #print(lista)
    return  DFS(lista, visitados, inicio, final, rota)
