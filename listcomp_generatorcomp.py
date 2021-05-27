'''list comprehension vs generator comprehension'''
import timeit
import sys
print(timeit.timeit('''a=["10" for i in range(10)]'''))
print(timeit.timeit('''b=("10" for i in range(10))'''))
print(timeit.timeit('''c=["10"]*10'''))
print(timeit.timeit('''b=("10" for i in range(10))'''))
["10" for i in range(10)]
print(sys.getsizeof(b))
print(sys.getsizeof(a))

