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
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

def delete_node(v):
    if v not in graph:
        print(v,"nor present")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            for j in list1:
                if v==j[0]:
                    list1.remove(j)
                    break



graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_edge('A','D',10)
add_edge('A','C',20)
add_edge('A','B',30)
add_edge('A','E',50) 
delete_node('C')   # OP=> {'A': [['D', 10], ['B', 30], ['E', 50]], 'B': [['A', 30]], 'D': [['A', 10]], 'E': [['A', 50]]}
print(graph)