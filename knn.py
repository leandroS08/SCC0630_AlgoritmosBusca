from sklearn.neighbors import kneighbors_graph
import matplotlib.pyplot as plt
import random
import networkx as nx
import numpy as np

matrix = []
lista_vertices = []
d_max = 10

def main():
    v = 10
    k = 3

    grafo_knn(v, k)

    #rota = list(range(v))
    #print(rota)

    #coordenadas = np.array(lista_vertices)
    #print(coordenadas)
    # plota_resultado(rota, coordenadas)


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
    g = nx.Graph()

    print("\nMatriz resultante:")
    print(A)

    print("\nArray:")
    print(array)
    coordenadas = np.array(lista_vertices)

    for x in range(len(array)):
        for y in range(len(array[x])):
            if array[x][y] != 0.0:
                g.add_edge(str(x),str(y),weight=array[x][y])

    nx.draw_networkx(g,alpha=0.6,node_size=70,font_size=5)
    plt.show()

    # plota_resultado(array, coordenadas)


def plota_resultado(rota, coordenadas):
    # d_plot = np.concatenate((np.array([coordenadas[rota[i]] for i in range(len(rota))]),np.array([coordenadas[rota[0]]])))

    plt.scatter(coordenadas[:,0],coordenadas[:,1])

    # plt.plot(d_plot[:,0],d_plot[:,1])

    # for i, txt in enumerate(rota):
    #     plt.annotate(str(rota[i]), coordenadas[rota[i]])

    plt.show()

main()