import datetime as dt

def start():
    with open("logs.txt", "a", encoding="utf-8") as logs:

        today = dt.date.today()
        now = dt.datetime.now().time()
        current_time = now.strftime("%H:%M:%S")

        logs.write(f"\n[{today} {current_time}] Запустился main.py")

def send(status_code, reason, channel):
    with open("logs.txt", "a", encoding="utf-8") as logs:
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