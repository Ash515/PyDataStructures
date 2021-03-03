import queue
q=queue.PriorityQueue()
q.put(20)
q.put(10)
q.put(30)#[20,10,30]
q.get() #20
q.get() #10
