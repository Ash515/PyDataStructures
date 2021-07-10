def add_node(v):
    global node_count
    if v in nodes:
        print("Node already exists")
    else:
        node_count+=1
        nodes.append(v)

        for n in graph:
            n.append(0)
        
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def print_matrix():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()




nodes=[]
graph=[]
node_count=0

print("Before Inserting:")
print(nodes)
print(graph)

add_node("A")  #function calling
add_node(" B") 
print("After Inserting")
print(nodes)
print_matrix()
