def algoritmo_a(M, v1, v2):
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
            linha_aux = []
            for i in range(len(M)):
                linha_aux.append([i, M[vertice][i]])
            
            linha_aux.sort(key=lambda tup: tup[1])
            
            #print("\nLinha:")
            #print(linha_aux)   

            for i in range(len(M)):
                if(linha_aux[i][1] != 0):
                    j = linha_aux[i][0]
                    if(visitados[j] == 0):
                        visitados[j] = 1
                        rotas[j] = rotas[vertice].copy()
                        rotas[j].append(j)
                        fila.append(j)

        #print("\n Visitas:")
        #print(visitados)

        #print("\n Rotas:") 
        #print(rotas)

    return rotas[v2]
