from sklearn.neighbors import kneighbors_graph
import matplotlib.pyplot as plt
import random
import networkx as nx
import numpy as np
from busca_largura import *
from grafos_fixos import *


d_max = 10 #Limite das coordenadas x e y

def main():
    #v = 5
    #k = 3
    #lista_vertices, m = grafo_knn(v, k)

    lista_vertices, v, k, M = grafos_fixos(1)

    print("\n Matriz:")
    print (M)

    v_1 = 0
    v_2 = 5

    print("\n Vertices: (", v_1, "  ", v_2, ")")

    #rota = list(range(v))
    #print("\nRota:")
    #print(rota)

    rota1 = busca_largura(M, v_1, v_2)

    print("\n Rota:", rota1)

    plota_grafo(M, lista_vertices)


def grafo_knn(v, k):
    lista_vertices = []

    # NOTE: gera vertices a partir do input V
    while len(lista_vertices) < v:
        new = ([random.randint(0, d_max), random.randint(0, d_max)])
        if new  not in lista_vertices:
            lista_vertices.append(new)

    #print("\nLista de vértices:")
    #print(lista_vertices)

    # NOTE: gera matrix KNN de distâncias com vétices 
    A = kneighbors_graph(lista_vertices, k, mode='distance', include_self=False)
    array = A.toarray()
    
    #print("\nMatriz resultante:")
    #print(A)

    #print("\nArray:")
    #print(array)

    return lista_vertices, array

def plota_grafo(array, lista_vertices):
    g = nx.Graph()

    # NOTE: mapeia as arestas para plotar
    for x in range(len(array)):
        for y in range(len(array[x])):
            if array[x][y] != 0.0:
                g.add_edge(str(x),str(y),weight=array[x][y])

    # NOTE: Dicionário {chave: índice do vetor lista_vertices, valor: coordenadas do ponto}
    pos ={str(index):value for index,value in enumerate(np.array(lista_vertices))}

    #print("\Mapa [índice, coordenada]:")
    #print(pos)
    fig = plt.figure(facecolor="w")

    ax = fig.add_subplot(111)
    nx.draw_networkx(g,alpha=0.6,node_size=30, with_labels=False,pos= pos, font_size=8, edge_color="b", ax=ax)

    #Adicionado para printar eixos x e y
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    ax.grid()
    plt.show()

main()