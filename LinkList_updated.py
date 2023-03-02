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
        if (self.head != None) and (pos < self.n):
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

l=LL()
# l.insert_start(20)
# l.insert_start(10)
# l.insert_start(30)
# l.insert_start(40)
# l.insert_start(50)
# l.insert_start(10)
print(l)

# print(len(l))

l.insert(0,"inserted")
# l.append("hello")

print(l)