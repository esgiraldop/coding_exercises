class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        current = head
        values = []
        next_current = current.next
        values.append(current.data)
        while next_current != None:
            while current.data == next_current.data:
                next_current = next_current.next
                if next_current == None:
                    break
            if next_current == None:
                break
            values.append(next_current.data)
            current = next_current
            next_current = current.next

        if current.data != values[-1]:
            values.append(current.data)

        head = None
        for value in values:
            head = self.insert(head, value)

        return head

mylist= Solution()
#T=int(input())
#T = 6
#T = 7
head=None
#data_list = [1, 2, 2, 3, 3, 4]
data_list = [1, 1, 1, 1, 1, 1, 1]
#for i in range(T):
for data in data_list:
    #data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head)