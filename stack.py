
class stack():
    """Implementation on stack DS in python have do send length or size during call
    methods are available as Push,Pop,Peek"""

    def __init__(self,length):
        """inilization of class stack have to send one arrugnment during calling 
        stack class is length"""

        self.length=length
        self.data=[]

    def Push(self,input_data):
        if len(self.data)<self.length:
            self.data.append(input_data)
        else:
            print("stack is overflowed we cannnot add given number in stack")

    def Peek(self):
        if len(self.data)>=1:
            print("peek value is ",self.data[-1])
        else:
            print("There is no data in stack")

    def Pop(self):
        if len(self.data)>=1:
            print("data is pop out ",self.data.pop(-1))
        else:
            print("There is no data to pop out")

    def is_underflow(self):
        if len(self.data)<self.length:
            print("True")
            return True
        else:
            print("False")
            return False

    def Print(self):
        for i in self.data[::-1]:
            print(i)

    def __len__(self):

        return len(self.data)
    
    def size(self):
        print("size of stack is ",self.length)
        return self.length



st=stack(5)
st.Push(1)
st.Push(2)
st.Push(3)
#st.Push(4)
#st.Pop()
#st.Pop()
#st.Peek()
print(st.size())

#st.Print()
        