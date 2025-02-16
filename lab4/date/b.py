from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Вчера:", yesterday.date())
print("Сегодня:", today.date())
print("Завтра:", tomorrow.date())