def unique_elements(a):
    unique_list = []
    for item in a:
        if item not in unique_list:  
            unique_list.append(item)
    return unique_list

user_input = input("Enter elements separated by spaces: ").split()

print(unique_elements(user_input))
