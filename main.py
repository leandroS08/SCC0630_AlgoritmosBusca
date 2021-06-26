from best_first_search import best_first_search
import time
from grafos import *
from busca_profundidade import busca_profundidade
from busca_largura import *
from algoritmo_a import *

def main():
    v = 1000
    k = 5

    gera_grafo_knn(v, k)

    #NOTE: Lê grafo predefinidos armazenados em arquivos
    pos, M = le_grafo_knn()

    lista_vertices = [0]*len(pos)

    for key, value in pos.items():
        lista_vertices[int(key)] = value

    #print("\nMatriz:")
    #print (M)

    v1 = 642
    v2 = 23

    print("\nVertice origem:", v1, " || Vertice destino ", v2)

    #rota = list(range(v))
    #print("\nRota:")
    #print(rota)

    ti = time.time()
    rota1 = busca_profundidade(M, v1, v2)
    dt = time.time() - ti
    print("\nBusca em profundidade")
    print("   > Rota:", rota1)
    print("   > Distancia: {:.4f}".format(dist_rota(M, rota1)))
    print("   > Tempo: {:.4f}".format(dt))
    plota_grafo(M, pos, rota1, v1, v2, 1)

    ti = time.time()
    rota2 = busca_largura(M, v1, v2)
    dt = time.time() - ti
    print("\nBusca em largura")
    print("   > Rota:", rota2)
    print("   > Distancia: {:.4f}".format(dist_rota(M, rota2)))
    print("   > Tempo: {:.4f}".format(dt))
    plota_grafo(M, pos, rota2, v1, v2, 2)

    '''ti = time.time()
    rota3 = busca_largura_otimizado(M, v1, v2)
    dt = time.time() - ti
    print("\nBusca em largura otimizada")
    print("   > Rota:", rota3)
    print("   > Distancia:", dist_rota(M, rota3))
    print("   > Tempo:", dt)
    plota_grafo(M, pos, rota3, v1, v2, 3)'''

    ti = time.time()
    rota4 = best_first_search(M, v1, v2, lista_vertices, pos)
    dt = time.time() - ti
    print("\nBest first Search")
    print("   > Rota:", rota4)
    print("   > Distancia: {:.4f}".format(dist_rota(M, rota4)))
    print("   > Tempo: {:.4f}".format(dt))
    plota_grafo(M, pos, rota4, v1, v2, 1)

    #ti = time.time()
    #rota4 = algoritmo_a(M, lista_vertices, v1, v2)
    #dt = time.time() - ti
    #print("\nAlgoritmo A*")
    #print("   > Rota:", rota4)
    #print("   > Distancia:", dist_rota(M, rota4))
    #print("   > Tempo:", dt)
    #plota_grafo(M, pos, rota4, v1, v2, 4)

    plt.show()

    return 0

main()