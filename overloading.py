class Num():
    def __init__(self,num):
        self.num=str(num)
    def __str__(self):
        return self.num
    def __add__(self,other):
        return int(self.num)+int(other.num)
    def __lt__(self,other):
        return int(self.num)<int(other.num)
    def __len__(self):
        return len(self.num)
    def __radd__(self,other):
        return str(int(self.num)+int(other))
    def __iadd__(self,other):
        return (int(self.num)+other)
    
num=Num(100000)
mun=Num(15)
nun=num+mun
print(num<mun)
print(len(num))
print(dir(num))
num+=10
print(10+num)

