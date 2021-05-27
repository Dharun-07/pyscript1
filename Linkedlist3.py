class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
    def Print_node(self):
        self.node=self.head
        if(self.head==None):
            print(";inked list is empty")
        else:
            n=self.head
            while(n is not None):
                if(n.next==None):self.tail=n
                print(n.data)
                n=n.next
    def add_begin(self,data):
            node=Node(data)
            node.next=self.head
            self.head=node
    def add_last(self,data):
        node=Node(data)
        self.tail.next=node
        self.tail=node

class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None
    def __repr__(self):
        return self

lt=LinkedList()
n1=Node(1);lt.head=n1
n2=Node(2);n1.next=n2
n3=Node(3);n2.next=n3
lt.add_begin(4)
lt.add_begin(5)
lt.Print_node()
lt.add_last(6)


lt.Print_node()