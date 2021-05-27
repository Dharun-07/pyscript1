def iterator(min=0,max=10):
    while(True):
        if(min<=max):
            yield(min)
            min+=1
    else:
        raise StopIteration
for i in iterator(0,20):
    print(i)