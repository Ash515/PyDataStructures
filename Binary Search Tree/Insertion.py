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
        

root=BST(30)
list_=[10,20,30,15,20]
for i in list_:
    root.insert(i)

