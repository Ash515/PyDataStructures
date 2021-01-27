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
            while n.nref is not None:
                n=n.nref
            while n is not None:
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
                
    def insert_after(self,data,x):
        if(self.head is None):
            print("List is empty")
        else:
            n=self.head
            while(n is not None):
                if(x==n.data):
                    break
                n=n.nref
            if(n is None):
                print("There is no any element found")
            else:
                    new_node=Node(data)
                    new_node.nref=n.nref
                    new_node.pref=n
                    if(n.nref is not None):
                        n.nref.pref=new_node
                    n.nref=new_node
    def insert_before(self,data,x):
        if(self.head is None):
            print("List is empty")
        else:
            n=self.head
            while(n is not None):
                if(x==n.data):
                    break
                n=n.nref
            if(n is None):
                print("There is no any element found")
            else:
                    new_node=Node(data)
                    new_node.pref=n.pref
                
                    new_node.nref=n
                    if(n.pref is not None):
                        n.pref.nref=new_node
                    else:
                        self.head=new_node
                        n.pref=new_node
    def delete_begin(self):
        if(self.head is None):
            print("The list is empty")
            return
        if(self.head.nref is None):
             self.head=None
             print("The list will be empty after deleted the node")
        else:
            self.head=self.head.nref
            self.head.pref=None
                        
                    
                
 

        
        
                   
    
                
dl=doubly()
dl.insert_empty(50) 
dl.insert_begin(40)
dl.insert_begin(30)
dl.insert_begin(20)
dl.insert_end(60)
dl.insert_after(36,30)   #20 ---->30 ---->36 ---->40 ---->50 ---->60 ---->
dl.insert_before(45,20) #20 ---->30 ---->36 ---->40 ---->45 ---->50 ---->60 ---->
dl.delete_begin()
dl.forward()                         #20 ---->30 ---->40 ---->50 ---->60 ---->

















