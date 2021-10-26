from datetime import datetime
import requests

username = input("Введите свое имя: ")

print("\nTask 1")

current_time = datetime.now().hour

if 0 <= current_time <= 4:
    print(f"Доброй ночи, {username}!")
elif 5 <= current_time <= 9:
    print(f"Доброе утро, {username}!")
elif 10 <= current_time <= 16:
    print(f"Добрый день, {username}!")
else:
    print(f"Добрый вечер, {username}!")

print("\nTask 2")

response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
current_time = response.json()["datetime"][11:13]
if current_time.startswith("0"):
    current_time = current_time[-1]
current_time = int(current_time)

if 0 <= current_time <= 4:
    print(f"Доброй ночи, {username}!")
elif 5 <= current_time <= 9:
    print(f"Доброе утро, {username}!")
elif 10 <= current_time <= 16:
    print(f"Добрый день, {username}!")
else:
    print(f"Добрый вечер, {username}!")






