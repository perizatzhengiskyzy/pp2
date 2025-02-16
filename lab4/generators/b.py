def even(n):
    for i in range(0, n+1, 2):
        yield i
n=int(input("enter a number :"))
a = even(n)
for i in a :
    print(i)