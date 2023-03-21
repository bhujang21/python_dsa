
class node:
     def __init__(self,value):

         self.value=value
         self.pointer=None

class LinkList:

    def __init__(self):

        self.head=None
        self.tail=None
    
    def insert_start(self,value):
        obj=node(value)
        if self.head is not None:
            obj.pointer=self.head
            self.head=obj
            #self.tail=obj
        else:
            self.head=obj
            self.tail=obj
    def insert_end(self,value):
        obj=node(value)
        if self.tail is not None:
            self.tail.pointer=obj
            self.tail=obj
        else:
            self.tail=obj
            self.head=obj

    def display(self):
        if self.head is not None:
            inc=self.head
            data='Head->'
            while inc.pointer:
                data+=f"{inc.value}->"
                inc=inc.pointer
            else:
                data+=f"{inc.value}->None"
        else:
            data="Head->None<-Tail"
        print(data)

ll_obj=LinkList()
#ll_obj.insert_start(22)
#ll_obj.insert_end(10)
#ll_obj.insert_end(55)
#ll_obj.insert_end(51)
#ll_obj.insert_start(101)
ll_obj.display()