from itertools import permutations

def print_permutations():
    user_input = input("Enter a string: ")
    perm = permutations(user_input)
    
    for p in perm:
        print(''.join(p))

if __name__ == "__main__":
    print_permutations()         