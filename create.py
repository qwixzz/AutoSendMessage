import json
import sys
import time

def set_all_variables():
    try:
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

        print("Переменные успешно установлены в файле config.json.")
        time.sleep(5)
        sys.exit(1)

    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)
        sys.exit(1)

set_all_variables()