from busca_profundidade import busca_profundidade
from grafos import *
from busca_largura import *
from algoritmo_a import *

def main():
    v = 10
    k = 5

    #gera_grafo_knn(v, k)

    #NOTE: Lê grafo predefinidos armazenados em arquivos
    pos, M = le_grafo_knn()

    print("\nMatriz:")
    print (M)

    v1 = 0
    v2 = len(M) - 1 

    print("\nVertice origem:", v1, " || Vertice destino ", v2)

    #rota = list(range(v))
    #print("\nRota:")
    #print(rota)

    #rota1 = busca_profundidade(M, v1, v2)
    #print("\nRota (busca em profundidade):", rota1)

    #rota2 = busca_largura(M, v1, v2)
    #print("\nRota (busca em largura):", rota2)

    #rota3 = busca_largura_otimizado(M, v1, v2)
    #print("\nRota (busca em largura otimizado):", rota3)

    rota4 = algoritmo_a(M, pos, v1, v2)
    print("\nRota (algoritmo A):", rota4)

    #plota_grafo(M, pos, rota4)

main()