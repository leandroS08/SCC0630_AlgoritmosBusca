from sklearn.neighbors import kneighbors_graph
import matplotlib.pyplot as plt
import random
import networkx as nx
import numpy as np

matrix = []
lista_vertices = []
d_max = 10

def main():
    v = 5
    k = 1
    grafo_knn(v, k)
    rota = [1, 2, 3, 4, 0]
    coordenadas = np.array(lista_vertices)
    plota_resultado(rota, coordenadas)


def grafo_knn(v, k):
    # TODO: gerar vertices a partir do input V
    while len(lista_vertices) < v:
        new = ([random.randint(0, d_max), random.randint(0, d_max)])
        if new  not in lista_vertices:
            lista_vertices.append(new)

    print(lista_vertices)

    # TODO: gera matrix KNN de distâncias
    A = kneighbors_graph(lista_vertices, 2, mode='distance', include_self=False)
    array = A.toarray()
    print(A)
    print(array)

def plota_resultado(rota, coordenadas):
    d_plot = np.concatenate((np.array([coordenadas[rota[i]] for i in range(len(rota))]),np.array([coordenadas[rota[0]]])))

    plt.scatter(coordenadas[:,0],coordenadas[:,1])

    plt.plot(d_plot[:,0],d_plot[:,1])

    for i, txt in enumerate(rota):
        plt.annotate(str(rota[i]), coordenadas[rota[i]])

    plt.show()

if __name__ == '__main__':
    main()