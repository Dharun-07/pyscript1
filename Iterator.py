class Iterate():
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.result=0
    def __iter__(self):
        return self 
    def __next__(self):
        if(self.min<=self.max):
            self.result=self.min
            self.min+=1
            return self.result
        else:
            raise StopIteration

for i in Iterate(0,20):
    print(i)