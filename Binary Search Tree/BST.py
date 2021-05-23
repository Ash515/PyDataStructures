class BST():
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

root=BST(50)  #root node
print(root.key)
print(root.lchild)
print(root.rchild)
print("=======")
root.lchild=BST(30)    # left node
print(root.lchild.key)
print(root.lchild.lchild)
print(root.lchild.rchild)
print("=======")
root.lchild.lchild=BST(15)   # left child of the left node
root.lchild.rchild=BST(35)
print(root.lchild.lchild.key)
print(root.lchild.rchild.key)


