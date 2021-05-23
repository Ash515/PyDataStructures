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
                
            
dl=doubly()
dl.forward()
dl.reverse()

#output
#List is empty, you cant do any forward traversal
#List is empty, you cant do any backward traversal











