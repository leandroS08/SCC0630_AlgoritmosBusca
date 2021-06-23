from busca_largura import *
from grafos import *


def main():

    #lista_vertices, v, k, v1, v2, M = grafo_knn_fixo(1)

    v = 10
    k = 3
    lista_vertices, v1, v2, M = grafo_knn_aleatorio(v, k)

    print("\nMatriz:")
    print (M)

    print("\nVertice origem:", v1, " || Vertice destino ", v2)

    #rota = list(range(v))
    #print("\nRota:")
    #print(rota)

    rota1 = busca_largura(M, v1, v2)

    print("\nRota (busca em largura):", rota1)

    plota_grafo(M, lista_vertices)

main()