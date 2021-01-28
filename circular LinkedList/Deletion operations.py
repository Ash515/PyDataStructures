class Node():
    def __init__(self,data):
        self.data=data
        self.ref=None
class Circular():
    def __init__(self):
        self.head=None
        self.tail=None
    def __Print__(self):
        if(self.head is None):
            print("There is no node found!")
        else:
            n=self.head
            while (n is not None):
                print(n.data,"----->",end="")
                n=n.ref
                
    def add_begin(self,data):
           new_node=Node(data)
           new_node.ref=self.head
           self.head=new_node
           self.tail=new_node
           
    def add_end(self,data):
        
       n=self.head
       new_node=Node(data)
       if(n is None):
           self.head=new_node
       else:
           while n.ref is not None:
               n=n.ref
           if(n.ref is None):
               n.ref=new_node
               self.tail=n.ref
    def add_middle(self,data,x):
        if(self.head is None):
            print("There is no node found!")
        else:
            n=self.head
            while (n is not None):
                if(x==n.data):
                    break
                n=n.ref
            if(n is None):
                print("ther is no value foud")
            else:
                new_node=Node(data)
               
                new_node.ref=n.ref
                n.ref=new_node
                
    def add_before(self,data,x):
         if(self.head is None):
             print("there is empty linkedlist")
             return
         if(self.head):
             n=self.head
             while(n.ref is not None):
                 if(n.ref.data==x):
                     break
                 n=n.ref
             if(n.ref is None):
                print("There is no any element")
             else:
                new_node=Node(data)
                
                new_node.ref=n.ref
                n.ref=new_node
    def delete_begin(self):
        if(self.head is None):
             print("there is empty linkedlist")
             
        else:
            self.head=self.head.ref

    def delete_end(self):
        if(self.head is None):
            print("There is no any node found")
        else:
            n=self.head
            while(n.ref.ref is not None):
                n=n.ref
            if(n.ref.ref is None):
                n.ref=None
            return 
                
    def delete_by_val(self,x):
         if(self.head is None):
             print("there is empty linkedlist")
             return
         n=self.head
         if(n==x):
            n=n.ref
            return
         while(n.ref is not None):
            if(n.ref.data==x):
                break
            n=n.ref
         if(n.ref is None):
            print("There is no data found to delete")
         else:
            n.ref=n.ref.ref


            
            
        
               
                
                
            
            
                
         
                
        
                
            
       
            
            
            
cl=Circular()
cl.add_begin(10)
cl.add_begin(15)
cl.add_begin(20)
cl.add_end(30)
cl.add_before(45,15)
cl.add_middle(25,30)
cl.delete_begin()
cl.delete_end()
cl.delete_by_val(15)
cl.__Print__()


