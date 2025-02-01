def histogram(lst):
    for i in lst:
        print("*" * int(i))

user_input = input("Enter the numbers: ").split()  
histogram(user_input)
