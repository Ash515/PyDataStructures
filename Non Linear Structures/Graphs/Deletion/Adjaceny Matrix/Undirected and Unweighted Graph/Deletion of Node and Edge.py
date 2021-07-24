'''
For both unweighted and weighted graph deletion of edges are same method 
'''


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

def add_edges(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"not present in the graph")
    elif v2 not in nodes:
        print(v2,"node not present in the graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)

        graph[index1][index2]=cost
        graph[index2][index1]=cost

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"not in graph")
    else:
        index1=nodes.index(v)
        node_count= node_count-1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

# Deletion of Edges        
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"not present in graph")
    elif v2 not in nodes:
        print(v2,"not present in graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)

        graph[index1][index2]=0
        graph[index2][index1]=0




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
 
add_edges("A","C",10)
add_edges("A","D",20)

delete_edge("A","B")
delete_edge("C","D")
print("After deleting")
print_matrix()


