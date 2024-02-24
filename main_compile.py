import time
import requests
import sys
import json
import datetime as dt

def start():
    with open("logs.txt", "a") as logs:

        today = dt.date.today()
        now = dt.datetime.now().time()
        current_time = now.strftime("%H:%M:%S")

        logs.write(f"\n[{today} {current_time}] Запустился main.py")

def send(status_code, reason, channel):
    with open("logs.txt", "a") as logs:
        today = dt.date.today()
        now = dt.datetime.now().time()
        current_time = now.strftime("%H:%M:%S")
        
        if status_code == 200:
            today = dt.date.today()
            now = dt.datetime.now().time()
            current_time = now.strftime("%H:%M:%S")

            logs.write(f"\n[{today} {current_time}] Отправилось сообщение в текстовой канал {channel}")
        
        else:
            today = dt.date.today()
            now = dt.datetime.now().time()
            current_time = now.strftime("%H:%M:%S")

            logs.write(f"\n[{today} {current_time}] Не получилось отправить сообщение в текстовой канал {channel} {reason}")

def set_all_variables():
    token = input("Введите токен: ")
    channel_id = input("Введите ID канала: ")

    with open("config.json", "r+") as config:
        config_data = json.load(config)

        if len(config_data) != 0:
            config_data["token"] = token
            config_data["channel_id"] = channel_id

            config.seek(0)

        config.truncate()

        json.dump(config_data, config)

    print("Переменные успешно установлены в файле config.json.")
    sys.exit(1)
if len(sys.argv) != 2 or sys.argv[1] != "--setall":
    with open("config.json") as config:
        config_data = json.load(config)
        if len(config_data) == 0:
            print("Ошибка: В файле config.json не хватает переменных: token, channel_id, message.")
            print("Используйте скрипт с аргументом --setall для установки переменных.")
            sys.exit(1)
        else:
            with open("text.txt", "r", encoding="utf-8") as file:
                message = file.read()
            token = config_data["token"]
            channel_id = config_data["channel_id"]
            
else:
    set_all_variables()

url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

payload = {
    "content" : message
}

headers = {
    "Authorization" : token
}

if __name__ == "__main__":
    start()
    while True:
        res = requests.post(url, payload, headers=headers)
        send(res.status_code, res.reason, channel_id)
        time.sleep(60)