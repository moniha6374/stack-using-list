stack=[]
def push():
    m=int(input())
    stack.append(m)
    print(stack)
def pop():
    e=stack.pop()
    print(e)
    print(stack)
def peek():
    print(stack[-1])
n=int(input())
while True:
    c=int(input())
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        peek()
    elif c==4:
        print("exit")
    else:
        print("invalid input")
