def square(n):
    for i in range(1,n+1):
        yield i*i
n=int(input("enter a number : "))
a = square(n)
for i in a :
    print(i)