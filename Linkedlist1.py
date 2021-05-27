class LinkedList:
    def __init__(self):
        self.head=None
    def __repr__(self):
        node=self.head
        nodes=[]
        while(node.next is not None):
            nodes.append(node.data)
            node=node.next
        nodes.append(node.data)
        nodes.append("None")
        node="->".join(nodes)
        return node
class Node:
    def __init__(self,element):
        self.data=element
        self.next=None
    def __repr__(self):
        return self
llist=LinkedList()
node1=Node("1")
node2=Node("2")
node3=Node("3")
node4=Node("4")
llist.head=node1
node1.next=node2
node2.next=node3
node3.next=node4
print(llist)