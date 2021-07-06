'''
In python Dictionaries are useful for making hashtables
We can create a hash function in various methods
here we are going to see how to change a given key into hashing based on ASCII
characters.
'''


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
    
    def add(self,key,val):  # adding value to the key in a dictionary
        f=self.get_hash(key)
        self.array[f]=val
    
    def get(self,key):
        g=self.get_hash(key)
        return self.array[g]



      

t=HashTable()
print(t.get_hash('october 6'))
t.add('october 6',250)
t.array

get_val=t.get('october 6')
print(get_val)

