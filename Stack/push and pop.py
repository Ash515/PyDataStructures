stack=[]

def push():
    
    if(len(stack)==n):
        print("Stack overflows")
    else:
        element= input("Enter the element")
        stack.append(element)
        print(stack)
def pop():
    if not stack:
        print("Stack is Empty")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)
n=int(input("Enter the total no:"))
while True:
    print("Select the operation 1.push 2.pop 3.quit")
    choice=int(input())
    if(choice==1):
        push()
    elif (choice==2):
        pop()
    elif choice==3:
        break
    else:
        print("Entyer the correct option")
    
    
