from datetime import datetime, timedelta

today = datetime.now()
five_days_ago = today - timedelta(days=5)

print("5 дней назад:", five_days_ago.date())