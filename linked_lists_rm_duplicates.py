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
        #Write your code here
        current = head
        if head.next == None:
            return head
        else:
            if head.data == head.next.data:
                current.next = current.next.next
                return self.removeDuplicates(head.next.next)
            else:
                return self.removeDuplicates(head.next)
            return head

mylist= Solution()
#T=int(input())
T = 6
head=None
data_list = [1, 2, 2, 3, 3, 4]
#for i in range(T):
for data in data_list:
    #data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head)