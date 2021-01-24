class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class doubly:
    def __init__(self):
        self.head=None

    def forward(self):
        n=self.head
        if(n is None):
            print("List is empty, you cant do any forward traversal")
        else:
            while n is not None:
                print(n.data,'---->',end="")
                n=n.nref
    def reverse(self):
        n=self.head
        if(n is None):
            print("List is empty, you cant do any backward traversal")
        else:
            while n.nref is None:
                n=n.nref
            while n is None:
                print(n.data,'---->',end="")
                n=n.pref
    def insert_empty(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
        else:
            print("List is not empty!!!")
    def insert_begin(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
            
    def insert_end(self,data):
        new_node=Node(data)
        n=self.head
        if(n is None):
            n=new_node
        else:
            while n.nref is not None:
                n=n.nref
            if(n.nref is None):
                n.nref=new_node
                new_node.pref=n
                
dl=doubly()
dl.insert_empty(10)
dl.insert_begin(20)
dl.insert_begin(30)
dl.insert_end(40)
dl.forward()
dl.reverse()


#output 
#30 ---->20 ---->10 ---->40 ---->











