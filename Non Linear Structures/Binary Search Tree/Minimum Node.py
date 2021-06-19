class BST():
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    
    def insert(self,data):
        if self.key is None:  # Checks the Node is empty or not if empty key = given data
            self.key=data
            return 
        
        if self.key==data:    # checks wheather the given data is equal to key if true it will return i.e ignores
            return 
        
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
     
    def search(self,data):       # Search method
        if self.key==data:       # if node is equal to key it returns message
            print("Node is present !")
            return
        
        if self.key>data:        #if value is lesser than key then it goes with LST(left sub tree)
            if self.lchild:      # if already a left child is present it will goes with recursion
                self.lchild.search(data)   #recursive method
            else:
                print("Node is not present ")
        
        else:                     #if value is greater than key then it goes with RST(Right sub tree)
            if self.rchild:        # if already a left child is present it will goes with recursion
                self.rchild.search(data)    #recursive method
            else:
                print("Node is not present")
    
    def preorder(self):
        
        print(self.key,end="-----")
        if self.lchild:
            self.lchild.preorder()
        
        if self.rchild:
            self.rchild.preorder()
    
    #Deletion
    def deletion(self,data,cur):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild=self.lchild.deletion(data,cur)
            else:
                print("Node not found in LST")
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.deletion(data,cur)
            else:
                print("Ther is no node found in RST")
        else:
            if self.lchild is None:
                temp=self.rchild
                if(data==cur):
                    self.key=temp.key
                    self.rchild=temp.rchild
                    self.lchild=temp.lchild
                    temp=None
                    return

                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                if(data==cur):
                    self.key=temp.key
                    self.rchild=temp.rchild
                    self.lchild=temp.lchild
                    temp=None
                    return
                self=None
                return temp
            node=self.rchild
            while self.lchild:
                node=self.lchild
            self.key=node.key
            self.rchild=self.rchild.deletion(data,cur)
        return self
    def min_node(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("Minimum node in this tree is: ",current.key)
    
    def max_node(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("Maximum node present in the given tree is:",current.key)
            

   
def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
       

root=BST(30)
list_=[10,20,30,15,20]
for i in list_:
    root.insert(i)

print("Pre-order Traversal:")   #Pre-order Traversal:
root.preorder()                 # 30-----10-----20-----15-----
print()
root.min_node()
root.max_node()

root.preorder()               
