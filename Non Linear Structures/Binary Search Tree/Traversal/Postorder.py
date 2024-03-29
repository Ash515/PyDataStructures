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
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        
        if self.rchild:
            self.rchild.postorder()
        
        print(self.key,end="-----")
   
   
    
   

        

root=BST(30)
list_=[10,20,30,15,20]
for i in list_:
    root.insert(i)

search=[20,30,10,15,45]
for j in search:
    root.search(j)

print("postorder Traversal:")
root.postorder()                   #  postorder Traversal:
                                   #  15-----20-----10-----30-----
                                     
