import time
from grafos import *
from busca_profundidade import busca_profundidade
from buscas_largura import *
from best_first_search import best_first_search
from buscas_a import *

def main():
    indice = 1
    v = 500
    k = 3

    #gera_grafo_knn(v, k, indice)

    #NOTE: Lê grafo predefinidos armazenados em arquivos
    pos, M = le_grafo_knn(indice)

    lista_vertices = [0]*len(pos)

    for key, value in pos.items():
        lista_vertices[int(key)] = value

    #print("\nMatriz:")
    #print (M)

    v1 = 0
    v2 = 138

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
    plota_grafo(M, pos, rota1, v1, v2, 1, "Busca em Profundidade")

    ti = time.time()
    rota2 = busca_largura(M, v1, v2)
    dt = time.time() - ti
    print("\nBusca em largura")
    print("   > Rota:", rota2)
    print("   > Distancia: {:.4f}".format(dist_rota(M, rota2)))
    print("   > Tempo: {:.4f}".format(dt))
    plota_grafo(M, pos, rota2, v1, v2, 2, "Busca em Largura")

    ti = time.time()
    rota3 = busca_largura_otimizado(M, v1, v2)
    dt = time.time() - ti
    print("\nBusca em largura otimizada")
    print("   > Rota:", rota3)
    print("   > Distancia: {:.4f}".format(dist_rota(M, rota3)))
    print("   > Tempo: {:.4f}".format(dt))
    plota_grafo(M, pos, rota3, v1, v2, 3, "Busca em Largura Otimizado")

    ti = time.time()
    rota4 = best_first_search(M, v1, v2, lista_vertices, pos)
    dt = time.time() - ti
    print("\nBest first Search")
    print("   > Rota:", rota4)
    print("   > Distancia: {:.4f}".format(dist_rota(M, rota4)))
    print("   > Tempo: {:.4f}".format(dt))
    plota_grafo(M, pos, rota4, v1, v2, 4, "Busca Best First")

    '''ti = time.time()
    rota5 = busca_a(M, v1, v2, lista_vertices, pos)
    dt = time.time() - ti
    print("\nAlgoritmo A")
    print("   > Rota:", rota5)
    print("   > Distancia: {:.4f}".format(dist_rota(M, rota5)))
    print("   > Tempo: {:.4f}".format(dt))
    plota_grafo(M, pos, rota5, v1, v2, 5, "Busca com Algoritmo A")'''

    ti = time.time()
    rota6 = busca_a_estrela(M, v1, v2, lista_vertices, pos)
    dt = time.time() - ti
    print("\nAlgoritmo A*")
    print("   > Rota:", rota6)
    print("   > Distancia: {:.4f}".format(dist_rota(M, rota6)))
    print("   > Tempo: {:.4f}".format(dt))
    plota_grafo(M, pos, rota6, v1, v2, 6, "Busca com Algoritmo A*")

    plt.show()

    return 0

main()