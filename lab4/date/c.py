from datetime import datetime

now = datetime.now().replace(microsecond=0)
print("Без микросекунд:", now)