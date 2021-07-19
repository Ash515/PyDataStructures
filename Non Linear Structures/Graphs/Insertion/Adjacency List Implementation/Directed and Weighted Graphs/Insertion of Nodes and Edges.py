def add_node(v):
    if v in graph:
        print(v,"already present")
    else:
        graph[v]=[]

def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1," not present in graph")
    elif v2 not in graph:
        print(v2,"not present in graph")
    else:
        list1=[v2,cost]
        graph[v1].append(list1)
      


graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_edge('A','D',10)
add_edge('A','C',20)
add_edge('A','B',30)
add_edge('A','E',50) # E not present in graph

print(graph)