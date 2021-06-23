def busca_largura(M, v1, v2):
    fila = []
    visitados = [ 0 for i in range(len(M)) ]
    rotas = [ [] for i in range(len(M))]
    for i in range(len(M)):
        rotas[i].append(v1)

    fila.append(v1)
    visitados[v1] = 1

    while len(fila) > 0:
        #print("\n Fila:")
        #print(fila)

        vertice = fila.pop(0)

        if(M[vertice][v2] != 0):
            visitados[v2] = 1
            rotas[v2] = rotas[vertice].copy()
            rotas[v2].append(v2)
            fila.append(v2)
            break
        else:
            for i in range(len(M)):
                if(M[vertice][i] != 0):
                    if(visitados[i] == 0):
                        visitados[i] = 1
                        rotas[i] = rotas[vertice].copy()
                        rotas[i].append(i)
                        fila.append(i)

    #print("\n Visitas:")
    #print(visitados)

    #print("\n Rotas:") 
    #print(rotas)

    return rotas[v2]
