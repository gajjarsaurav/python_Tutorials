a = 344

def corn():
    b=23
    print(a)

def fudge():
    print(b)        # here it'll generate an error because b is having different scope

corn()
fudge()
