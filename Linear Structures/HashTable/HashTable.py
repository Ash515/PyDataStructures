class HashTable():
    def __init__(self):
        self.Max=100
        self.array=[None for i in range(self.Max)]
    
    def get_hash(self,key):
        h=0
        for i in key:
            s=ord(i)
            h+=s
            return h % self.Max
      

t=HashTable()
print(t.get_hash('march 6'))
