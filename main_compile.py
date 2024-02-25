import time
import requests
import sys
import os
import json
import datetime as dt

def start_log():
    with open("logs.txt", "a") as logs:
        today = dt.date.today()
        now = dt.datetime.now().time()
        current_time = now.strftime("%H:%M:%S")
        logs.write(f"\n[{today} {current_time}] Запустился main.exe")
        print("Запустился main.exe")

def send_log(status_code, reason, channel):
    with open("logs.txt", "a") as logs:
        today = dt.date.today()
        now = dt.datetime.now().time()
        current_time = now.strftime("%H:%M:%S")
        
        if status_code == 200:
            logs.write(f"\n[{today} {current_time}] Отправилось сообщение в текстовой канал {channel}")
            print(f"[{today} {current_time}] Отправилось сообщение в текстовой канал {channel}")
        else:
            logs.write(f"\n[{today} {current_time}] Не получилось отправить сообщение в текстовой канал [{channel}] с причиной [{reason}]")
            print(f"[{today} {current_time}] Не получилось отправить сообщение в текстовой канал [{channel}] с причиной [{reason}]")

def compile_code():
    try:
        with open("config.json") as config:
            config_data = json.load(config)
            if len(config_data) == 0:
                raise ValueError("Ошибка: В файле config.json не хватает переменных: token, channel_id")
            else:
                with open("text.txt", "r", encoding="utf-8") as file:
                    message = file.read()
                token = config_data["token"]
                channel_id = config_data["channel_id"] 

        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

        payload = {
            "content" : message
        }

        headers = {
            "Authorization" : token
        }

        start_log()
        while True:
            res = requests.post(url, payload, headers=headers)
            send_log(res.status_code, res.reason, channel_id)
            time.sleep(60)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)
        sys.exit(1)

if __name__ == "__main__":
    compile_code()