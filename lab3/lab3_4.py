def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

prime_numbers = filter_prime(numbers)
print(prime_numbers)