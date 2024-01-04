import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = [root] # Queue
        traverse = [queue.pop(0).data] # List to print at the end
        queue.append(root.left)
        queue.append(root.right)
        while len(queue) > 0:
            root = queue[0]
            if root.left != None:
                queue.append(root.left)
            if root.right != None:
                queue.append(root.right)
            traverse.append(queue.pop(0).data)
        print(*traverse, sep=' ')

#T=int(input())
T = 6
myTree=Solution()
root=None
data_list = [3, 5, 4, 7, 2, 1]
#for i in range(T):
for data in data_list:
    #data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)