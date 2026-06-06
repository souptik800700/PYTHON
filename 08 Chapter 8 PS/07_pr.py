l = ["Harry", "Rohan"]

def rem(l, word):
    for item in l:
        l.remove(word)
        return l

print(rem(l,"Rohan"))
