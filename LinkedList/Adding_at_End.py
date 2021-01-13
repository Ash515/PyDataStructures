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
                print( n.data,"--->",end=" ")
                n=n.ref
            
    def Add_at_begining(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def Add_at_end(self,data):
        new_node=Node(data)
        n=self.head
        if n is None:
                      n=new_node
        else:
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
            
ll=LinkedList()
ll.Add_at_begining(10)
ll.Add_at_begining(20)
ll.Add_at_end(100)
ll.Add_at_begining(30)
ll.Print()

        
