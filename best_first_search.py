from queue import PriorityQueue
from collections import defaultdict
import math

def listaAdj(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > 0:
                adjList[i].append(j)
    return adjList

def heuristica(vertice, fim):
    dx = abs(vertice[0] - fim[0])
    dy = abs(vertice[1] - fim[1])
    return math.sqrt(pow(dx, 2) + pow(dy, 2)) 

def converte(matriz, fim, lista_vertices):
    distancia_fim = [[] for i in range(len(matriz))]
    for indice in range(len(matriz)):
        distancia_fim[indice] = heuristica(lista_vertices[indice], fim)
    return distancia_fim

def cria_rota(sucessores, inicio, fim):
    atual = sucessores[fim]
    rota = [fim]
    while atual != inicio:
        rota.append(atual)
        atual = sucessores[atual]
    rota.append(inicio)
    #print("Rota")
    #print(rota[::-1])
    return rota[::-1]

def best_first_search(matriz, inicio, fim, lista_vertices, pos):
    distancia_fim = converte(matriz, lista_vertices[fim], lista_vertices)
    sucessores = [-1]*len(matriz)
    lista = listaAdj(matriz)

    visited = [0] * len(lista_vertices)
    visited[inicio] = 1

    pq = PriorityQueue()
    pq.put((0, inicio))
    while pq.empty() == 0:
        atual = pq.get()[1]
        #print(u, end=" ")
        if atual == fim:
            #print(sucessores)
            break
 
        for vertice in lista[atual]:
            distancia = distancia_fim[vertice]
            if visited[vertice] == 0:
                sucessores[vertice] = atual
                visited[vertice] = 1
                pq.put((distancia, vertice))
    return cria_rota(sucessores, inicio, fim)