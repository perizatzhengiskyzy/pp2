import re
text = "C:\\Users\\User\\OneDrive - АО Казахстанско-Британский Технический Университет\\Документы\\GitHub\\pp2\\lab5\\row.txt"
with open(text, "r",encoding='utf-8') as file:
    string = file.read().strip()
pattern = "[A-Z][a-z]"
result = re.findall(pattern, string)
if result:
    print(result)
else:
    print("Not found") 