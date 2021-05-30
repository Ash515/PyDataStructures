class Node():
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList():
    def __init__(self):
        self.head=None
    def Print_ll(self):
        n=self.head
        if n is None:
            print("LinkedList is empty")
        else:
            while n is not None:
                print(n.data)
                n=n.ref
ll=LinkedList()
ll.Print_ll()
