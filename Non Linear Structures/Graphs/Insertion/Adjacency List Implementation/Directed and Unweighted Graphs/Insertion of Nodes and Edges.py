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
       


graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_edge('A','D')
add_edge('A','C')
add_edge('A','B')
add_edge('A','E') # E not present in graph

print(graph)