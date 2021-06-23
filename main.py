from grafos import *
from busca_largura import *
from algoritmo_a import *

def main():
    v = 5
    k = 2

    gera_grafo_knn(v, k)
    pos, M = le_grafo_knn()

    print("\nMatriz:")
    print (M)

    v1 = 0
    v2 = len(M) - 1 

    print("\nVertice origem:", v1, " || Vertice destino ", v2)

    #rota = list(range(v))
    #print("\nRota:")
    #print(rota)

    #rota1 = busca_largura(M, v1, v2)
    rota2 = busca_largura(M, v1, v2)

    #print("\nRota (busca em largura):", rota1)
    print("Rota (algoritmo A):", rota2)

    plota_grafo(M, pos, rota2)

main()