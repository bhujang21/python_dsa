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
            while traval.next != None:
                temp+=f"{traval.data}->"
                traval=traval.next
            temp+=f"{traval.data}->None"
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
            

l=LL()
#
l.insert_start(20)
# l.insert_start(10)
# l.insert_start(30)

# l.insert_start(50)
# l.insert_start(10)


# print(len(l))

#
# l.append("hello")

# print(l)

# l.remove_start()

print(l)

l.remove_by_value(40)

print(l)
