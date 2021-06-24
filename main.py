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

    rota1 = busca_largura_otimizado(M, v1, v2)
    #rota2 = busca_largura(M, v1, v2)

    #NOTE: Busca em profundidade
    rota3 = busca_profundidade(M, v1, v2)
    print("\nRota (busca em profundidade):", rota3)

    print("\nRota (busca em largura):", rota1)
    #print("Rota (algoritmo A):", rota)

    plota_grafo(M, pos, rota1)

main()