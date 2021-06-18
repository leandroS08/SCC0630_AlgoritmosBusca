from sklearn.neighbors import kneighbors_graph
import matplotlib.pyplot as plt
import random
import networkx as nx
import numpy as np

lista_vertices = []
d_max = 10

def main():
    v = 10
    k = 3

    m = grafo_knn(v, k)

    rota = list(range(v))

    print("\nRota:")
    print(rota)

    plota_resultado(m, rota)

    #coordenadas = np.array(lista_vertices)
    #print(coordenadas)
    # 


def grafo_knn(v, k):
    # TODO: gerar vertices a partir do input V
    while len(lista_vertices) < v:
        new = ([random.randint(0, d_max), random.randint(0, d_max)])
        if new  not in lista_vertices:
            lista_vertices.append(new)

    print("\nLista de vértices:")
    print(lista_vertices)

    # TODO: gera matrix KNN de distâncias
    A = kneighbors_graph(lista_vertices, k, mode='distance', include_self=False)
    array = A.toarray()
    
    print("\nMatriz resultante:")
    print(A)

    print("\nArray:")
    print(array)
    

    return array

def plota_resultado(array, rota):
    g = nx.Graph()

    for x in range(len(array)):
        for y in range(len(array[x])):
            if array[x][y] != 0.0:
                g.add_edge(str(x),str(y),weight=array[x][y])
    
    nx.draw_networkx(g,alpha=0.6,node_size=70,font_size=8, edge_color="b")

    plt.show()

main()