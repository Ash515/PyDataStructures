'''
Heap in priority representation
'''
import heapq
list_=[(1,"Python"),(2,"JAVA"),(3,"C++")]
heapq.heapify(list_)
print(list_)

for i in range(len(list_)):
    print(heapq.heappop(list_))

'''
Output
(1, 'Python')
(2, 'JAVA')
(3, 'C++')
'''