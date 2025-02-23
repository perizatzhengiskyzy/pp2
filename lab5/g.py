import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def find_and_convert(file_path):
    pattern = r"\b[a-z]+_[a-z]+\b"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    print(snake_to_camel(match.group()))
    except FileNotFoundError:
        print("File not found!")

file_path = r"C:\\Users\\User\\OneDrive\\Documents\\GitHub\\pp2\\lab5\\row.txt"
find_and_convert(file_path)
