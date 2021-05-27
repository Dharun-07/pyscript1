class LinkedList:
    def __init__(self,nodes=None):
       self.head=Node(nodes.pop(0))
       self.nodess=[]
       self.nodes=nodes
    def __addfirst__(self,ele):
        self.node=Node(ele)
        self.node.next=self.head
        self.head=self.node
    def __repr__(self):
        self.node=self.head
        for ele in self.nodes:
           self.nodess.append(self.node.data)
           self.node.next=Node(ele)
           self.node=self.node.next
        self.nodess.append(self.node.data)
        self.nodess.append("None")
        self.node="->".join(self.nodess)
        return str(self.nodess)
    def __iter__(self):
        node=self.nodess
        for nod in node:
            yield nod
        
class Node:
    def __init__(self,element):
        self.data=element
        self.next=None
    def __repr__(self):
        return self
    
llist=LinkedList(["1","2","3","4","5"])
print(llist)
for i in llist:print(i)


class LinkedList:
    def __init__(self,nodes=None):
       self.head=Node(nodes.pop(0))
       self.nodess=[]
       self.nodes=nodes
    def addfirst(self,ele):
        self.node=Node(self.nodes[0])
        self.node.next=self.head
        self.head=self.node
        self.head=Node(ele)
        #self.nodes=[self.node.data]+self.nodess
        self.nodess=[]
    def __repr__(self):
        self.node=self.head
        for ele in self.nodes:
           self.nodess.append(self.node.data)
           self.node.next=Node(ele)
           self.node=self.node.next
        self.nodess.append(self.node.data)
        self.node="->".join(self.nodess)
        self.nodes=self.nodess
        return str(self.nodess)
    def __iter__(self):
        node=self.nodess
        for nod in node:
            yield nod
    def __len__(self):
        return len(self.nodess)
        
class Node:
    def __init__(self,element):
        self.data=element
        self.next=None
    def __repr__(self):
        return self
    
llist=LinkedList(["1","2","3","4","5"])
print(llist)
llist.addfirst("10")
llist.addfirst("30")
print(llist)
print(len(llist))
for i in llist:print(i)