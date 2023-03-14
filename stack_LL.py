# stack by using LinkList

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:

    def __init__(self):

        self.top=None
        self.n=0

    def __str__(self):
        if self.top:
            result=""
            travle=self.top
            while travle:
                result+=f"|{travle.data}|\n"
                travle=travle.next
            return result
        return "None"

    def isempty(self):
        return self.top == None

    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node
        self.n+=1
        return 

    def pop(self):

        if not self.isempty():
            #print(self.top.data)
            self.top=self.top.next
            self.n-=1
            return True
        raise ValueError("StackIsEmpty")

    def peak(self):

        if not self.isempty():
            print("Peak is",self.top.data)
            return True
        raise ValueError("StackIsEmpty")

    def stack_reverse(self):
        """reversing stack in-place"""

        if not self.isempty():
            travle=self.top
            second=travle.next
            while second:
                c=second.next
                second.next=travle
                travle,second=second,c
            self.top.next=None
            self.top=travle
            return True
        raise ValueError("StackIsEmpty")

s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
print(s)
s.stack_reverse()
print(s)
s.pop()
s.pop()
s.pop()
print(s)