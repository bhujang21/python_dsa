

class node:

    def __init__(self,value):

        self.value=value
        self.pointer=None

#insert_start at location 0
#insert_end location at end
#display print the link list

class linklist:
    #length=0
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def insert_start(self,value):
        node_obj=node(value)
        if self.head:
            node_obj.pointer=self.head
            self.head=node_obj
            self.length+=1
        else:
            self.head=node_obj
            self.length+=1
            #node_obj.pointer=None
    
    def insert_end(self,value):
        node_obj=node(value)

        if self.head:
            inc_pointer=self.head
            while inc_pointer.pointer:
                inc_pointer=inc_pointer.pointer
            else:
                inc_pointer.pointer=node_obj
                self.length+=1
                #node_obj.pointer=None
        else:
            self.head=node_obj
            self.length+=1
            #node_obj.pointer=None
    
    def remove_first(self):
        if self.head:
            self.head=self.head.pointer
            self.length-=1
        
    def remove_last(self):
        second_pointer=self.head
        if self.head.pointer:
            first_pointer=self.head
            while first_pointer.pointer:
                #print("getting in while loop")
                second_pointer=first_pointer
                first_pointer=first_pointer.pointer
            else:
                second_pointer.pointer=None
                self.length-=1
        else:
            self.head=self.head.pointer
            self.length-=1

    def display(self):
        if self.head:
            data="""Head->"""
            inc_pointer=self.head
            while inc_pointer.pointer:
                #print("inc_pinter_is",inc_pointer)
                data+=f"{str(inc_pointer.value)}->"
                inc_pointer=inc_pointer.pointer
            else:
                data+=f"{inc_pointer.value}->None"
        else:
            data="Head->None"
        print(data)

    def get_len(self):
        if self.length == 0:
            print("there is no data inside linklist")
        else:
            print(self.length)



ll_obj=linklist()
# ll_obj.insert_start(20)
# ll_obj.insert_start(10)
# ll_obj.insert_end(11)
# ll_obj.insert_end(12)
# ll_obj.display()
# ll_obj.get_len()
# ll_obj.remove_last()
# ll_obj.display()
# ll_obj.get_len()
# ll_obj.remove_first()
ll_obj.display()
ll_obj.get_len()
#ll_obj.remove_first()
#ll_obj.display()
#l_obj.remove_last()
#ll_obj.display()