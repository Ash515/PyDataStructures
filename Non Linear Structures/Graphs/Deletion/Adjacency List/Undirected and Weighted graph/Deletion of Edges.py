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

def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"not present in graph")
    elif v2 not in graph:
         print(v2,"not present in graph")
    else:
        temp1=[v1,cost]
        temp2=[v2,cost]
        if temp2 in graph[v1]:
            graph[v1].remove(temp2)
            graph[v2].remove(temp1)
   

graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_edge('A','D',10)
add_edge('A','C',20)
add_edge('A','B',30)
add_edge('C','D',50) 
delete_edge('C','D',50)   # OP=> {'A': [['D', 10], ['B', 30], ['E', 50]], 'B': [['A', 30]], 'D': [['A', 10]], 'E': [['A', 50]]}
print(graph)