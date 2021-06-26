def busca_largura(M, inicio, fim):
    fila = []
    visitados = [ 0 for i in range(len(M)) ]
    rotas = [ [] for i in range(len(M))]
    for i in range(len(M)):
        rotas[i].append(inicio)

    fila.append(inicio)
    visitados[inicio] = 1

    while len(fila) > 0:
        #print("\n Fila:")
        #print(fila)

        vertice = fila.pop(0)

        if(M[vertice][fim] != 0):
            visitados[fim] = 1
            rotas[fim] = rotas[vertice].copy()
            rotas[fim].append(fim)
            fila.append(fim)
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

    return rotas[fim]


def busca_largura_otimizado(M, inicio, fim):
    fila = []
    visitados = [ 0 for i in range(len(M)) ]
    rotas = [ [] for i in range(len(M))]
    for i in range(len(M)):
        rotas[i].append(inicio)

    fila.append(inicio)
    visitados[inicio] = 1

    while len(fila) > 0:
        #print("\n Fila:")
        #print(fila)

        vertice = fila.pop(0)

        if(M[vertice][fim] != 0):
            visitados[fim] = 1
            rotas[fim] = rotas[vertice].copy()
            rotas[fim].append(fim)
            fila.append(fim)
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

    return rotas[fim]