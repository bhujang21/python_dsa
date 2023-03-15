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
    def __del__(self):
        return True

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

    def travle(self):
        if self.top:
            tra=self.top
            result=''
            while tra:
                result+=tra.data
                tra=tra.next
            return result
        return "Stack Empty"

    def string_rev(self,value):
        obj=Stack()
        for i in value:
            obj.push(i)
        print(obj.travle())
        del obj
        return True


def string_rev(value):
    obj=Stack()
    for i in value:
        obj.push(i)
    print(obj.travle())
    return True

string_rev("bhujang")
s=Stack()
s.string_rev("hello world")
# s.push('e')
# s.push('l')
# s.push('l')
# s.push('o')
#s.push(6)
#print(s)
# s.stack_reverse()
# print(s)
# s.pop()
# s.pop()
# s.pop()
