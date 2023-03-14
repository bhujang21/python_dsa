#Stack using Aarys
import ctypes
class Stack:
    def __init__(self):
        self.length=1
        self.n=0
        self.arr=self.__create_arr(self.length)

    def __str__(self):
        result=""
        for i in range(self.n-1,-1,-1):
            result+=f"|{self.arr[i]}|\n"
        if result:
            return result
        else:
            return "None"
    
    def __create_arr(self,size):
        return (size*ctypes.py_object)()

    def __resize_arr(self):
        self.length+=5
        arr=self.__create_arr(self.length)
        for i in range(self.n):
            arr[i]=self.arr[i]
        self.arr=arr
        return True

    def isempty(self):
        return self.n == 0

    def push(self,value):
        if self.n<self.length:
            self.arr[self.n]=value
            self.n+=1
            return True
        
        self.__resize_arr()
        self.arr[self.n]=value
        self.n+=1
        return True

    def pop(self):
        if not self.isempty():
            self.arr[self.n-1]=ctypes.py_object()
            self.n-=1
            return True
        raise ValueError("StackIsEmpty")

    def peak(self):
        if not self.isempty():
            print(self.arr[self.n-1])
            return self.arr[self.n-1]
        raise ValueError("StackIsEmpty")



s=Stack()
#print(s)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)
s.pop()
s.pop()
s.peak()

print(s)