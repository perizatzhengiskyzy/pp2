import re
def replace_characters(text):
    pattern = r'[ ,\.]'
    new_text = re.sub(pattern, ':', text)
    return new_text
input_text = "Hello, world. How are you doing today?"
result = replace_characters(input_text)
print("Result:", result)