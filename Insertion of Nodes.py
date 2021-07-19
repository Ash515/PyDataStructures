def add_node(v):
    if v in graph:
        print(v,"not present in graph")
    else:
        graph[v]=[]

graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
print(graph)