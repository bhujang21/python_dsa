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
    def custom_travle(self):
        
        if self.n > 0:
            result=""
            for i in range(self.n):
                result+=self.arr[i]
            print(result)
            return True
        print()

    def undo(self):
        if self.n!=0:
            self.n-=1
            return self.custom_travle()
        return self.custom_travle()

    def redo(self):
        try:
            self.arr[self.n]
            self.n+=1
            return self.custom_travle()
        except:
            self.custom_travle()

    
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

def undo_redo(string,pattern):
    obj=Stack()
    for i in string:
        obj.push(i)
    count=obj.n
    for i in pattern:
        if i.lower() == "u":
            if obj.n != 0:
                obj.n-=1
                obj.custom_travle()
            else:
                obj.custom_travle()
        elif i.lower() == 'r':
            if obj.n<count:
                obj.n+=1
                obj.custom_travle()
            else:
                obj.custom_travle()
    return True
s=Stack()
######undo_redo("bhujang","uur")
#s.string_rev('hello world')
# s.push('e')
# s.push('l')
# s.push('l')
# s.push('0')

# print(s)

# print(rev_string("bhujangrao"))
string="bhujang"
for i in string:
    s.push(i)
print(s.n)
s.undo()
s.push("99")
s.redo()
print("after one redo",s.n)
