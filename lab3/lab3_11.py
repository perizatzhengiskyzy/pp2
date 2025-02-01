def palindrome():
    a = input("Enter a string: ")
    b = a[::-1]
    if a == b:
        return "The string is a palindrome"
    else:
        return "The string is not a palindrome"

print(palindrome())       