def down(n):
    for i in range(n , 0 , -1):
        yield i
n=int(input("enter a number :"))
a=down(n)
for i in a:
    print(i)