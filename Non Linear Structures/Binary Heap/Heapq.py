'''
Implementation of the binary heap by using heapq module
'''
import heapq
#Pushing elements
a=[]
heapq.heappush(a,10)
heapq.heappush(a,20)
heapq.heappush(a,30)
print(a)   #[10, 20, 30]

#Deleting elements
heapq.heappop(a) 
print(a) #[20, 30]

# heappushpop() ---> push()--->pop()
b=[1,2,3,4,5]
heapq.heappushpop(b,6)
print(b) #[2, 4, 3, 6, 5] it automatically forms a min-heap structure

# heapify()  ---> used to form a heap structure in the given list.

c=[10,3,5,8,6]
heapq.heapify(c)
print(c)  #[3, 6, 5, 8, 10] forms a default min-heap structure.

# heapreplace() ---> pop()-->push()
d=[1,2,3,4,5]
heapq.heapreplace(d,6)
print(d)  #[2, 4, 3, 6, 5] deletes 1 and inserts 6 then formed min-heap structure

#nsmallest return the smallest numbers
e=[1,2,3,4,5,6]
small=heapq.nsmallest(2,e)
print(small)  #[1, 2]

#nlargest returns largest numbers
f=[1,2,3,4,5,6]
large=heapq.nlargest(2,f)
print(large)  #[6, 5]




