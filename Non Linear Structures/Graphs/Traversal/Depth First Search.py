def add_node(v):
    if v in graph:
        print(v,"already present")
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1," not present in graph")
    elif v2 not in graph:
        print(v2,"not present in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"not present in graph")
    elif v2 not in graph:
         print(v2,"not present in graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

def DFS(node,visited,graph):
    if node not in graph:
        print(node,"not presented in graph")
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)


        


visited=set()
graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_edge('A','D')
add_edge('A','C')
add_edge('C','D')
add_edge('C','E') 
DFS("A",visited,graph)
print(graph)



       

