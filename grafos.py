from sklearn.neighbors import kneighbors_graph
import matplotlib.pyplot as plt
import random
import networkx as nx
import numpy as np

def grafo_knn_fixo(arg):
    lista_vertices = []

    if arg == 1:
        v = 9
        k = 2

        v1 = 0
        v2 = 5

        lista_vertices.append([0,0])
        lista_vertices.append([0,2])
        lista_vertices.append([0,6])
        lista_vertices.append([2,0])
        lista_vertices.append([2,2])
        lista_vertices.append([2,6])
        lista_vertices.append([4,0])
        lista_vertices.append([4,2])
        lista_vertices.append([4,6])

        M = kneighbors_graph(lista_vertices, k, mode='distance', include_self=False)
        print(M)

        return lista_vertices, v, k, v1, v2, M.toarray()

def grafo_knn_aleatorio(v, k):
    d_max = 10 #Limite das coordenadas x e y
    v1 = 0
    v2 = v-1

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

    return lista_vertices, v1, v2, A.toarray()

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
    nx.draw_networkx(g,alpha=0.6,node_size=30, with_labels=True,pos= pos, font_size=8, edge_color="b", ax=ax)

    #Adicionado para printar eixos x e y
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    ax.grid()
    plt.show()