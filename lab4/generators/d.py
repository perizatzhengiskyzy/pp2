def squares(a,b):
    for i in range(a, b+1):
        yield i*i
n=int(input("enter a "))
m=int(input("enter b "))
a = squares(n,m)
for i in a :
    print(i)