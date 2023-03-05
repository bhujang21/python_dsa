class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LL:
    def __init__(self):
        self.head=None
        self.n=0
    
    def __str__(self):
        temp="Head->"
        if self.head != None:
            traval=self.head
            while traval != None:
                temp+=f"{traval.data}->"
                traval=traval.next
            temp+=f"None"
            return temp
        temp+="None"
        return temp

    def __len__(self):
        return self.n

    def insert_start(self,value):
        node=Node(value)
        if self.head != None:
            node.next=self.head
            self.head=node
            self.n+=1
            return True
        self.head = node
        self.n+=1
        return True

    def insert(self,pos,value):
        node=Node(value)
        if (self.head != None) and (0<pos < self.n):
            travle=self.head
            temp=0
            while (travle.next != None) and (temp<pos-1):
                print(travle.data)
                travle=travle.next
                temp+=1
            node.next=travle.next
            travle.next=node
            self.n+=1
            return True
        
        elif (self.head != None) and (pos == 0):
            self.insert_start(value)
            return True
        self.append(value)
        return True        
    
    def append(self,value):
        node = Node(value)
        if self.head != None:
            travel=self.head
            while travel.next != None:
                travel=travel.next
            travel.next=node
            self.n+=1
            return True
        self.head=node
        self.n+=1
        return True

    def remove_start(self):
        if self.head != None:
            self.head=self.head.next
            self.n-=1
            return True
        raise ValueError("LL.remove_start() Linklist should not be empty")

    def __get_node(self,value):
        number=1
        if self.head:
            travel=self.head
            while number<=self.n:
                if travel.data == value:
                    return number
                number+=1
                travel=travel.next
            return False
        return False

    def remove_by_value(self,value):
        pos=self.__get_node(value)
        if pos == 1:
            if self.head.next:
                self.head=self.head.next
                self.n-=1
                return True
            self.head = None
            self.n-=1
            return True
        elif pos>1:
            first=self.head
            second=None
            for i in range(1,pos):
                second=first
                first=first.next
            second.next=first.next
            self.n-=1
            return True
        raise ValueError("value is not in LL")
    """
    def remove_by_value(self,value):
        if self.head != None:
            if self.n > 1:
                if self.head.data == value:
                    self.head=self.head.next
                    self.n-=1
                    return True
                travel=self.head.next
                second_travel=self.head.next
                # while travel.next != None:
                while travel.next != None:
                    if travel.data == value:
                        # travel=travel.next
                        #####second_travel=travel.next
                        ####travel=travel.next
                        # self.n-=1
                        raise ValueError("value not in LL")
                    second_travel=travel.next
                    travel=travel.next
                second_travel=travel.next
                self.n-=1 
                return True
            elif self.n ==1 and self.head.data == value:
                self.head = None
                self.n-=1
                return True
            raise ValueError("value is not present")

        raise ValueError("LL.remove_by_value should not be empty")"""

    def pop(self):
        if self.head != None and self.n > 1:
            travle=self.head
            second_travle=None
            while travle.next != None :
                second_travle=travle
                travle=travle.next
            second_travle.next=None
            self.n-=1
            print(travle.data)
            return True
        elif self.n == 1:
            print(self.head.data)
            self.head=None
            self.n-=1
            return True
        raise ValueError("LL.pop() Linklist should not be empty")
            

# l=LL()
# #
# l.insert_start(10)
# l.insert_start(20)
# l.insert_start(30)
# l.insert_start(40)
# # l.insert_start(10)


# print(len(l))

#
# l.append("hello")

# print(l)

# l.remove_start()

# print(l)

# l.remove_by_value(40)

# print(l)

class my_ll:
    """this is updated 
    link list class"""

    def __init__(self):
        self.head=None
        self.n=0
    
    def __str__(self):
        """print your list list when hit print() on object"""
        if self.head:
            result=""
            travel=self.head
            while travel:
                result+=f"{travel.data}->"
                travel=travel.next
            result+="None"
            return result
        return "None"
    
    def __len__(self):
        """gives you length of your linklist"""
        return self.n

    def __getitem__(self,index):
        """
        if pos<self.n:
            counter=pos
            travle=self.head
            while 0<counter<=pos:
                travle=travle.next
                counter-=1
            #print(travle.data)
            return travle.data
        raise IndexError("Index is out of bound")"""
        pos=0
        travle=self.head
        while travle:
            if pos == index:
                return travle.data
            travle=travle.next
            pos+=1
        raise IndexError("Index is out of range")
    
    def __delitem__(self,index):
        if index < self.n:
            if index == 0 :
                self.head=self.head.next
                self.n-=1
                return True
            counter=1
            travle=self.head
            while counter != index:
                travle=travle.next
                counter+=1
            travle.next=travle.next.next
            return True
        raise IndexError("Index out of range")
    def __update_head(self,nod):
        self.head=nod
        self.n+=1
        return True
    
    def __travle_node(self,nod):
        travle=self.head
        while travle.next:
            travle=travle.next
        travle.next=nod
        self.n+=1
        return True
    def __get_pos(self,value):
        counter=0
        if self.head:
            travle=self.head
            while travle:
                if travle.data == value:
                    return counter
                counter+=1
                travle=travle.next
            return -1
        return -1   
    def index(self,value):
        travle=self.head
        pos=0
        while travle:
            if travle.data == value:
                print(pos)
                return pos
            travle=travle.next
            pos+=1
        raise ValueError("Value is not in Linklist")

    def insert_head(self,value):
        """inserting data at head point"""
        node=Node(value)
        node.next=self.head
        self.__update_head(node)
        return True

    def append(self,value):
        """inserting data at tail of linklist
        like appending data in list
        also you can use below function
        node=Node(value)
        if self.head:
            self.__travle_node(node)
            return True
        self.__update_head(node)
        return True
        """
        node=Node(value)
        if self.head:
            travle=self.head
            while travle.next:
                travle=travle.next
            travle.next=node
            self.n+=1
            return True
        self.head=node
        self.n+=1
        return True

    def insert(self,index,value):
        """insert given value in mention index(left side ofprevious data)
        if index is big it will append the data as well if LL is empty it will
        append the data"""
        node=Node(value)
        pos=0
        travle=self.head
        second_var=None
        while travle:
            if index==0:
                self.insert_head(value)
                return True
            if pos == index:
                node.next=travle
                second_var.next=node
                self.n+=1
                return True
            second_var=travle
            travle=travle.next
            pos+=1
        self.append(value)
        return True

    def insert_r(self,index,value):
        """insert the data at right side of given index number
        like if pass 2 index it will add it to 3 index in case if 
        empty list or big index it will append the value"""
        node=Node(value)
        pos=0
        travle=self.head
        while travle:
            if pos == index:
                node.next=travle.next
                travle.next=node
                self.n+=1
                return True
            travle=travle.next
            pos+=1
        self.append(value)
        return True

    def add_before(self,value,new_value):
        """Add the data before the given value it will search
        the given value and if found add new_value on left/before side"""
        if self.head:
            if self.head.data == value:
                self.insert_head(new_value)
                return True
            node=Node(new_value)
            travle=self.head
            while travle.next:
                if travle.next.data == value:
                    node.next=travle.next
                    travle.next=node
                    self.n+=1
                    return True
                travle=travle.next
            raise ValueError("Value not in link-list")
        raise ValueError("Value not in link-list")

    def add_after(self,value,new_value):
        """Add the data after the given value it will search
        the given value and if found add new_value after the found value"""
        if self.head:
            node=Node(new_value)
            travle=self.head
            while travle:
                if travle.data == value:
                    node.next=travle.next
                    travle.next=node
                    self.n+=1
                    return True
                travle=travle.next
            raise ValueError("Value not in link-list")
        raise ValueError("Value not in link-list")

    # def add_after(self,value,new_value):
    #     node=Node(new_value)
    #     travle=self.head
    #     while travle:
    #         if travle.data == value:
    #             node.next=travle.next
    #             travle.next=node
    #             self.n+=1
    #             return True
    #         travle=travle.next
    #     raise ValueError("Value is not in link-list")

    def clear(self):
        """clear the link-list"""
        self.head=None
        self.n=0
        return True
            
    def remove_head(self):
        if self.head:
            self.head=self.head.next
            self.n-+1
            return True
        raise ValueError("LinkList is Empty")

    def remove(self,value):
        if self.head:
            if self.head.data == value:
                self.head=self.head.next
                self.n-=1
                return True
            elif self.head.next:
                travle=self.head
                while travle.next:
                    if travle.next.data == value:
                        travle.next=travle.next.next
                        self.n-=1
                        return True
                    travle=travle.next
                raise ValueError("remove(x) X not in linklist")
        raise ValueError("Link-list is empty")


    def pop(self):
        if self.head:
            if self.head.next:
                travle=self.head
                while travle.next.next:
                    travle=travle.next
                print(travle.next.data)
                travle.next=None
                self.n-=1
                return True
            print(self.head.data)
            self.head=None
            self.n-=1
            return True
        raise ValueError('Link-list is empty')

    def remove_2(self,value):
        if self.head:
            pos=self.__get_pos(value)
            print("this is POS",pos)
            if pos==0:
                self.head=self.head.next
                self.n-=1
                return True
            elif pos>0:
                travle=self.head
                second_travle=None
                for i in range(pos):
                    second_travle=travle
                    travle=travle.next
                second_travle.next=travle.next
                self.n-=1
                return True
            raise ValueError("remove_2(X) X not found")
        raise ValueError("Link-list is empty") 

    def find(self,value):
        self.index(value)
        return True 



        
    
a=my_ll()

a.insert_head(20)
a.insert_head(30)
a.insert_head(10)
a.append('append')
# # print(a.n)
a.insert_r(4,"OO")
print(a)
a.add_after(1,100)
# a.insert(0,20)
print(a)