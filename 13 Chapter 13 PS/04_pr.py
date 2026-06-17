def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2.5345585,58522565,5886558,5865458,8541585,882485,552585]

f = list(filter(divisible5, a))
print(f)