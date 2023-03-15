#Stack using Aarys
import ctypes
class Stack:
    def __init__(self):
        self.length=1
        self.n=0
        self.arr=self.__create_arr(self.length)

    def __str__(self):
        result=''
        for i in range(self.n-1,-1,-1):
            result+=f"|{self.arr[i]}|\n"
        if result:
            return result
        else:
            return "None"
    def __del__(self):
        return True
    
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

    def revrse_stack(self):
        if not self.isempty():
            mid=self.n//2
            #print("mid",mid)
            for i in range(mid):
                self.arr[i],self.arr[self.n-1-i]=self.arr[self.n-1-i],self.arr[i]
            return True
        raise ValueError("StackIsEmpty")
    
    def travle(self):
        if self.n>0:
            result=''
            for i in range(self.n-1,-1,-1):
                result+=self.arr[i]
            return result
        return "Array Empty"
    def string_rev(self,string):
        arr=Stack()
        for i in string:
            arr.push(i)
        print(arr.travle())
        del arr
        return True

def rev_string(string):
    obj=Stack()
    result=''
    for i in string:
        obj.push(i)
    for i in range(obj.n-1,-1,-1):
        result+=obj.arr[i]
    return result


s=Stack()

s.string_rev('hello world')
# s.push('e')
# s.push('l')
# s.push('l')
# s.push('0')

# print(s)

print(rev_string("bhujangrao"))
