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

def delete_node(v):
    if v not in graph:
        print(v, "not present in graph")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)

       


graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_edge('A','D')
add_edge('A','C')
add_edge('A','B')
add_edge('B','A')
add_edge('B','C')
add_edge('B','D')
delete_node('B')      #OP => {'A': ['D', 'C', 'B'], 'C': ['A'], 'D': ['A'], 'E': []}
print(graph)