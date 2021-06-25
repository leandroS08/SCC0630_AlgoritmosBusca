import time
from grafos import *
from busca_profundidade import busca_profundidade
from busca_largura import *
from algoritmo_a import *

def main():
    v = 100
    k = 3

    gera_grafo_knn(v, k)

    #NOTE: Lê grafo predefinidos armazenados em arquivos
    pos, M = le_grafo_knn()

    lista_vertices = [0]*len(pos)

    for key, value in pos.items():
        lista_vertices[int(key)] = value

    #print("\nMatriz:")
    #print (M)

    v1 = 0
    v2 = len(M) - 1 

    print("\nVertice origem:", v1, " || Vertice destino ", v2)

    #rota = list(range(v))
    #print("\nRota:")
    #print(rota)

    ti = time.time()
    rota1 = busca_profundidade(M, v1, v2)
    dt = time.time() - ti
    print("\nBusca em profundidade")
    print("   > Rota:", rota1)
    print("   > Distancia:", dist_rota(M, rota1))
    print("   > Tempo:", dt)
    plota_grafo(M, pos, rota1, 1)

    ti = time.time()
    rota2 = busca_largura(M, v1, v2)
    dt = time.time() - ti
    print("\nBusca em largura")
    print("   > Rota:", rota2)
    print("   > Distancia:", dist_rota(M, rota2))
    print("   > Tempo:", dt)
    plota_grafo(M, pos, rota2, 2)

    ti = time.time()
    rota3 = busca_largura_otimizado(M, v1, v2)
    dt = time.time() - ti
    print("\nBusca em largura otimizada")
    print("   > Rota:", rota3)
    print("   > Distancia:", dist_rota(M, rota3))
    print("   > Tempo:", dt)
    plota_grafo(M, pos, rota3, 4)

    ti = time.time()
    rota4 = algoritmo_a(M, lista_vertices, v1, v2)
    dt = time.time() - ti
    print("\nAlgoritmo A*")
    print("   > Rota:", rota4)
    print("   > Distancia:", dist_rota(M, rota4))
    print("   > Tempo:", dt)
    plota_grafo(M, pos, rota4, 4)

    plt.show()

main()