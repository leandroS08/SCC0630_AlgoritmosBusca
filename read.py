from matplotlib.pyplot import viridis
import numpy as np
from collections import defaultdict


file = open("pos.txt", "r")
f = open("graph.txt", "r")

contents = file.read()
dictionary = eval(contents)
file.close()

matrix = np.loadtxt('graph.txt', dtype=np.float32)
matrix = matrix.tolist()
n = len(matrix)
print(matrix)

def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > 0:
                adjList[i].append(j)
    return adjList

def printPath(stack):
    for i in range(len(stack) - 1):
        print(stack[i], end = " -> ")
        print(stack[-1])
 
def DFS(vis, x, y, stack):
    stack.append(x)
    if (x == y):
        print(stack)
        print(vis)
        #printPath(stack)
        return
    vis[x] = 1
 
    if (len(lista[x]) > 0):
        for j in lista[x]:
            if (vis[j] == 0):
                DFS(vis, j, y, stack)
                 
    del stack[-1]

def DFSCall(x, y, n, stack):
    vis = [0 for i in range(n + 1)]
    DFS(vis, x, y, stack)


lista = convert(matrix)
print(lista)

stack = []
DFSCall(2, 3, n, stack)