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
    def deletion(self,data):
        if self.key is None:
            print("This is empty tree...")
        if(data<self.key):
            if self.lchild:
                self.lchild=self.lchild.deletion(data)
            else:
                print("There is no element present in LST")
        elif(data>self.key):
            if self.rchild:
                self.rchild=self.rchild.deletion(data)
            else:
                print("No element present in RST")
        else: 
            if self.lchild is None:  #0 child and 1 child cases
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            
            node = self.rchild      # case for having 2 children
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.deletion(node.key)
        return self

        

root=BST(30)
list_=[10,20,30,15,20]
for i in list_:
    root.insert(i)

print("Pre-order Traversal:")   #Pre-order Traversal:
root.preorder()                 # 30-----10-----20-----15-----
print()
root.deletion(20)  
print("\nAfter Deletion:")      #After Deletion:
root.preorder()                 # 30-----10-----15-----
