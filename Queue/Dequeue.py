import collections
q=collections.deque()
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.append(50)   #deque([30, 20, 10, 50])
q.popleft()         #deque([20, 10])
q.pop()                #deque([20])
print(q)
