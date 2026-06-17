
from functools import reduce
a = [1,2.5345585,58522565,5886558,5865458,8541585,882485,552585]

def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, a))
    