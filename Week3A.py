from sys import maxsize
from itertools import permutations
v=4
def tsp(graph,s):
        vertex=[]
        for i in range(v):
            if i!=s:
                vertex.append(i)
        a=maxsize
        next=permutations(vertex)
        for i in next:
            current=0
            k=s
            for j in i:
                current+=graph[k][j]
                k=j
            current+=graph[k][j]
            a=min(a,current)
        return a
graph=[
    [1,20,50,16],
    [10,0,30,20],
    [15,35,0,30],
    [20,25,30,0]
]
s=0
print(tsp(graph,s))

#outpu:70
        
