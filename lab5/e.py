import re
text = r"C:\\pp22\\pp2\\lab5\\row.txt"
with open(text, "r", encoding="utf-8") as file:
    string = file.read().strip()
pattern = "^a.*b$"
result = re.findall(pattern, string)
if result:
    print(result)
else:
    print("Not found") 