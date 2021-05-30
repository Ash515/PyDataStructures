import queue
q=queue.PriorityQueue()
q.put(20)
q.put(10)
q.put(30)#[20,10,30]
q.get() #20
q.get() #10

#indexing with priority queue

qu=[]
qu.append((1,"Ashwin"))
qu.append((2,"Arjun"))
qu.append((3,"Hari"))
print(q)

#[(3,"Hari"),(2,"Arjun"),(3,"Ashwin"))]
