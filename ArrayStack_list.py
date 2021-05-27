class ArrayStack():
    def __init__(self):
        self.l=list()
        self.top=0
    def __len__(self):
        return self.top
    def push (self,ele):
        self.l.append(ele)
        self.top+=1
    def is_element(self):
        return self.top>0
    def pop(self):
        if(not self.is_element()):
            pass
        self.top-=1
        return self.l.pop()
    def top(self):
        if(not self.is_element()):
            raise Empty('stack is empty')
        return self.l[-1]
a=ArrayStack()
print(len(a))
a.push(10)
print(len(a))
print(a.pop())
print(a.is_element())
