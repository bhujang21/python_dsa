
class Queue():
    "building queue ds that except length of queue as arrgunment"

    def __init__(self,length):
        self.length=length
        self.data=[]

    def enqueue(self,input_data):
        if self.length>len(self.data):
            self.data.append(input_data)
            print("data is enqueued in queue")
        else:
            print("size of Queue is full cannot Enqueued data")
        
    def dequeue(self):
        if len(self.data)>=1:
            print("queued data is",self.data.pop(0))
        else:
            print("queue is empty no data to dequeue")

    def size(self):
        print("size of Queue is",self.length)
        return self.length
    def __len__(self):

        print("available data length is ",len(self.data))
        return len(self.data)

    def Print(self):
        for i in self.data:
            print(i,end=" ")

    def bulk_enqueue(self,*args):
        size_avalable=self.length-len(self.data)
        if len(args)<=size_avalable:
            for i in args:
                self.data.append(i)
        else:
            print("Size is not available available size is",size_avalable)
    def bulk_dequeue(self,input_data):
        data_available=len(self.data)
        if data_available>int(input_data):
            for i in range(input_data):
                print("data is dequeue",self.data.pop(0))
        else:
            print("data in not available in queue by qiven length",input_data," availabe length of data is ",len(self.data))


que=Queue(5)
que.bulk_enqueue("a","b","c","d","e")
que.bulk_dequeue(2)
que.enqueue("z")
que.Print()
que.dequeue()
print(len(que))
que.size()
que.Print()