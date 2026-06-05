

def sum_natural_number(n):
    if(n==1):
        return 1
    return sum_natural_number(n-1) + n

print(sum_natural_number(3))