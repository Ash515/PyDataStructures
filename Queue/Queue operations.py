queue=[]
def enqueue():
    element=input("Enter the element")
    queue.append(element)
    print(queue)

def dequeue():
    queue.pop()
    print(queue)

def display():
    print(queue)

while True:
    print("Enter your choice 1.Add 2.Delete 3.See 4.exit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Please enter a valid option ")
