import ctypes,sys

class my_list:

    def __init__(self):
        self.size=1
        self.elements=0
        self.arr=self.__create_arr(self.size)
    
    def __create_arr(self,size):
        return (size*ctypes.py_object)()

    def __resize_arr(self):
        self.size+=10
        arr=self.__create_arr(self.size+10)
        for i in range(self.elements):
            arr[i]=self.arr[i]
        self.arr=arr
        return True

    def __len__(self):
        #print(self.elements)
        return self.elements

    def __is_positive_inline(self,index):
        return index>=0 and self.elements>index

    def index(self,value):
        if self.elements:
            for i in range(self.elements):
                if self.arr[i]==value:
                    print(i)
                    return i
            raise ValueError("value is not preset")
        raise ValueError("valueis not preset")

    def append(self,value):
        if self.size == self.elements:
            self.__resize_arr()
            # for i in range(self.elements):
            #     arr[i]=self.arr[i]
            self.arr[self.elements]=value
            self.elements+=1
            # self.arr=arr
        else:
            self.arr[self.elements]=value
            self.elements+=1


    def __str__(self):
        result=""
        if self.elements != 0:
            for i in range(self.elements):
                result+=str(self.arr[i])+","
            return "[" + result[:-1] + "]"
        return "[]"
    
    def __del__(self):
        return True
    
    def __delitem__(self,index):
        if self.__is_positive_inline(index):
            self.remove(self.arr[index])
            return True
        raise IndexError("Index out of range")

    def pop(self):
        if self.elements > 0:
            print(self.arr[self.elements-1])
            self.arr[self.elements-1]=ctypes.py_object()
            self.elements-=1
        else:
            raise IndexError("POP from empty list")
    def __size_setter(self,value):
        self.size=value
        return True

    def __elements_setter(self,value=0):
        self.elements=value
        return True

    def find(self,value):
        if self.elements:
            for i in range(self.elements):
                if self.arr[i] == value:
                    print(i)
                    return i
            #print(-1)
            return -1

        #print(-1)
        return -1

    def clear(self):
        self.__size_setter(1)
        self.__elements_setter(0)
        self.arr=self.__create_arr(self.size)
        return True

    def insert(self,pos,value):
        if self.elements == 0 or self.elements < pos :
            self.append(value)
        elif self.size < pos :
            self.__resize_arr()

        for i in range(self.elements,pos,-1):
            self.arr[i]=self.arr[i-1]
        self.arr[pos]=value
        self.elements+=1
        return True

    def remove(self,value):
        if self.elements:
        
            pos=self.find(value)
            if pos<0:
                raise ValueError("my_list.remove(x): X is not in my_list")
            #for i in range(pos+1,self.elements):
            #   self.arr[i-1]=self.arr[i]
            for i in range(pos,self.elements-1):
                self.arr[i]=self.arr[i+1]
            self.arr[self.elements-1]=ctypes.py_object()
            self.elements-=1
        else:       
            raise ValueError("my_list.remove(x): X is not in my_list")
    
    def __getitem__(self,index):
        if self.__is_positive_inline(index):
            print(self.arr[index])
            return self.arr[index]
        raise IndexError("Index is out of range")

    def get_size(self):
        return ctypes.sizeof(self.arr)
    
    def __min__(self):

        if self.elements:
            mini=self.arr[0]
           
            for i in range(1,self.elements):
                if mini > self.arr[i]:
                    mini = self.arr[i]
            return mini
        raise ValueError("min() arg is an empty sequence")
    
  


l=my_list()
x=[2,0,3,1,-1,4,5]
for i in x:
    l.append(i)
# l.append(1)

# l.append(2)


# print(l)
# # l.pop()
# # print(l)
# min(l)
# l.append(3)
# l.append("hello")
# # l.index(2)
# print(l)de


for i in range(2):
    print(i)