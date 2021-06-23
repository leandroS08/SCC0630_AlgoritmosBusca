from sklearn.neighbors import kneighbors_graph

def grafos_fixos(arg):
    lista_vertices = []

    if arg == 1:
        v = 9
        k = 3

        lista_vertices.append([0,0])
        lista_vertices.append([0,2])
        lista_vertices.append([0,4])
        lista_vertices.append([2,0])
        lista_vertices.append([2,2])
        lista_vertices.append([2,4])
        lista_vertices.append([4,0])
        lista_vertices.append([4,2])
        lista_vertices.append([4,4])

        M = kneighbors_graph(lista_vertices, k, mode='distance', include_self=False)

        return lista_vertices, v, k, M.toarray()