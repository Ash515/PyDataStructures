class Node():
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList():
    def __init__(self):
        self.head=None
    def Print(self):
        n=self.head
        if n is None:
            print("Empty List")
        else:
            while n is not None:
                print( n.data,end=" ")
                n=n.ref
            
    def Add(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
ll=LinkedList()
ll.Add(10)
ll.Add(20)
ll.Add(30)
ll.Print()

        
