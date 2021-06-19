import matplotlib.pyplot as plt
import networkx as nx

def main():

    randGraph()

def randGraph():

    G = nx.erdos_renyi_graph(10, 3)

    fig = plt.figure(facecolor="w")
    node_positions = nx.spring_layout(G, scale=10)
    print(node_positions)

    positions = { node: (int(pos[0]),int(pos[1])) for node,pos in node_positions.items() }

    ax = fig.add_subplot(111)
    nx.draw_networkx(G,alpha=0.6,node_size=30, pos= positions, with_labels=True, font_size=8, edge_color="b", ax=ax)

    #Adicionado para printar eixos x e y
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    ax.grid()
    plt.show()

main()