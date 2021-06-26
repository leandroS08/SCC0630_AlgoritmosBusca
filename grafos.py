from sklearn.neighbors import kneighbors_graph
import matplotlib.pyplot as plt
import random
import networkx as nx
import numpy as np
from collections import defaultdict

def le_grafo_knn():
    file = open("pos.txt", "r")
    f = open("graph.txt", "r")

    contents = file.read()
    pos = eval(contents)
    file.close()
    #print(pos)

    matrix = np.loadtxt('graph.txt', dtype=np.float32)
    matrix = matrix.tolist()

    return pos, matrix

def gera_grafo_knn(v, k):
    d_max = v #Limite das coordenadas x e y
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

    matrix = A.toarray()

    for i in range(v):
        for j in range(v):
            if matrix[i][j] != matrix[j][i]:
                if matrix[i][j] == 0:
                    matrix[i][j] = matrix[j][i] 
                else:
                    matrix[j][i] = matrix[i][j]

    pos ={str(index):value for index,value in enumerate(lista_vertices)}

    f = open("pos.txt", "w")
    f.write(str(pos))
    f.close()

    file = open("graph.txt", "w")
    np.savetxt('graph.txt', matrix, fmt='%.8f')
    file.close()

def plota_grafo(matrix, pos, rota, inicio, fim, index):
    g = nx.Graph()
    r = nx.Graph()
    n = nx.Graph()

    # NOTE: mapeia as arestas para plotar
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] != 0.0:
                g.add_edge(str(x),str(y),weight=matrix[x][y])

    # NOTE: grafo com nós da rota
    for i in range(len(rota)-1):
        r.add_edge(str(rota[i]),str(rota[i+1]),weight=matrix[rota[i]][rota[i+1]])

    n.add_node(str(inicio))
    n.add_node(str(fim))

    fig = plt.figure(facecolor="w")

    ax = fig.add_subplot(111)

    #NOTE: plota grafo
    nx.draw_networkx(g,alpha=0.6,node_size=10, with_labels=False,pos= pos, font_size=8, edge_color="b", ax=ax, width = 1)
    #NOTE: plota rota
    nx.draw_networkx(r,alpha=0.6,node_size=20, with_labels=False,pos= pos, font_size=8, node_color="r", edge_color="r", ax=ax, width = 3)
    #NOTE: plota ponto de inĩcio e fim
    nx.draw_networkx(n,alpha=0.6,node_size=70, with_labels=True,pos= pos, node_color="g", font_size=10, ax=ax, width = 3)

    #Adicionado para printar eixos x e y
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    #ax.grid()
    
    plt.figure(index)

def dist_rota(M, rota):
    distancia = 0
    if(rota is not np.empty):
        for i in range(len(rota)-1):
            distancia += M[rota[i]][rota[i+1]]
        return distancia
    else:
        return -1