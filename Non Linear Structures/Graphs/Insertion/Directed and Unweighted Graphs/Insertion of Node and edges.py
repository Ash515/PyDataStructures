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

def add_edges(v1,v2):
    if v1 not in nodes:
        print(v1,"not present in the graph")
    elif v2 not in nodes:
        print(v2,"node not present in the graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)

        graph[index1][index2]=1  #we are taking only directed side 
       




def print_matrix():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()




nodes=[]
graph=[]
node_count=0



add_node("A")  #function calling
add_node("B") 
add_node("C") 
add_node("D")
 
add_edges("A","C")
add_edges("B","D")

print(graph)
print_matrix()

