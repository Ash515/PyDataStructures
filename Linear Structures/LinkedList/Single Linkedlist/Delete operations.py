class Node():
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList():
    def __init__(self):
        self.head=None
    def __Print__(self):
        n=self.head
        if(n is None):
                print("List is Empty")
        while n is not None:
            print(n.data,"---->",end="")
            n=n.ref
            
    def  Add_in_front(self,data):
        n=self.head
        node=Node(data)
        node.ref=n
        self.head=node

    def Add_end(self,data):
        new_node=Node(data)
        n=self.head
        if n is None:
            n=new_node
        else:
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

            
    def Add_after_node(self,data,x):
        new_node=Node(data)
        n=self.head
        while n is not None:
            if(x==n.data):
                break
            n=n.ref
        if(n is None):
            print("Node is not Present")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
            
    def Add_before(self,data,y):
        if(self.head is None):
            print("Linked list is empty")
            return
        if(self.head.data==y):
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==y:
                break
            n=n.ref
        if( n.ref is None):
            print("Node is not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

            
    def delete_begin(self):
        if self.head is None:
            print("Node is empty")
        else:
            self.head=self.head.ref
            
    def delete_end(self):
        if self.head is None:
            print("Node is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            if(n.ref.ref is None):
                n.ref=None
                
     def delete_anywere(self,x):
        if self.head is None:
            print("Node is empty")
            return
        n=self.head
        if(x==n.data):
            n=self.head.ref
            return
        while n.ref is not None:
            if(x==n.ref.data):
                break  
            n=n.ref
        if(n.ref is None):
            print("No node found at that data")
        else:
            n.ref=n.ref.ref
            
                
ll.linkedlist()             
ll.Add_in_front(10)
ll.Add_in_front(20)
ll.Add_in_front(30)
ll.Add_in_front(50)
ll.delete_begin()
ll.delete_end()
ll.delete_anywere(10)

















        

        
    
                
            

            
            

            
            
                
            
    

         
                
                
            
            
                 
            
ll=LinkedList()
ll.Add_in_front(10)
ll.Add_in_front(7)
ll.Add_in_front(50)





ll.__Print__()
       
        
