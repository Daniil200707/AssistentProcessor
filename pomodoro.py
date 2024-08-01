# Version: 0.9
import time
import pyttsx3
import webbrowser
import tkinter as tk
import plyer
import asyncio
import yaml

start = True
cycle = 0

def on_exit(root):
    global start
    root.destroy()
    start = False
    show_notification("Помодоро", "Программа закончила свою работу!")
    say_massage("Программа закончила свою работу!")

def stop():
    global start
    global cycle
    start = False
    cycle_dict = {"cycles": cycle}

    with open("data.yaml", "w") as cycle_file:
        yaml.dump(cycle_dict, cycle_file)

def continue_timer(website_var, websites):
    global start
    start = True
    pomodoro_cycle(website_var, websites)

def show_notification(title, message):
    plyer.notification.notify(message=message,
                              app_name='AssistantProcessor',
                              app_icon='images/processor.ico',
                              title=title)

def say_massage(massage):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # установите скорость речи по вашему желанию
    engine.setProperty('volume', 1)  # установите громкость речи по вашему желанию
    engine.say(massage)
    engine.runAndWait()

# Функция для таймера
def pomodoro_timer(minutes):
    global start
    seconds = minutes * 60

    while start and seconds:
        mins, secs = divmod(seconds, 60)
        timer_var.set('{:02d}:{:02d}'.format(mins, secs))
        result_label.update()
        seconds -= 1
        time.sleep(1)
    say_massage("Время вышло!")


def async_time(minutes_int):
    pomodoro_timer(minutes_int)

# Функция для выполнения одного цикла методики помидора
def pomodoro_cycle(w_var, web):
    global start
    global cycle

    with open("data.yaml", 'r') as f:
        data = yaml.safe_load(f)

    for i in range(data["cycles"]):
        if start:
            # Открытие выбранного веб-сайта
            cycle = (i - data["cycles"]) * -1

            if cycle % 2 != 0:
                selected_website = list(web.values())[w_var.get()]
                webbrowser.open_new(selected_website)

                show_notification("Помодоро", "Работаем...")
                say_massage("Работаем...")
                async_time(25)

            else:
                show_notification("Помодоро", "Перемена!")
                say_massage("Перемена!")
                pomodoro_timer(5)

    if start:
        show_notification("Помодоро", "Работа завершена!")
        say_massage("Работа завершена, пора отдохнуть от компьютера и если есть посуда помыть её!")
    else:
        print(True)

def start_program(website_var, websites):
    with open("data.yaml", "w") as file:
        yaml.dump({"cycles": 7, "work": True}, file)

    pomodoro_cycle(website_var, websites)

def main():
    global timer_var
    global result_label
    global start

    websites = {
        'Математика': 'https://pidruchnyk.com.ua/1154-matematyka-10-klas-ister.html',
        'Физика': 'https://lib.imzo.gov.ua/wa-data/public/site/books2/pidruchnyky-10-klas-2018/21-fizyka-10-klas/fizyka-10kl-bar%E2%80%99yahtar-ranok.pdf',
        'Другие учебники': 'https://drive.google.com/drive/folders/16lc7ICbzmtVg3bHLSTftyF7oJfZ_aRY4',
        # добавьте другие веб-сайты по вашему желанию
    }

    root = tk.Tk()
    root.title("Методика помидора")
    root.iconbitmap("images/processor.ico")
    root.geometry("200x300")

    timer_var = tk.StringVar()
    timer_label = tk.Label(root, textvariable=timer_var, font=('Helvetica', 48))
    timer_label.pack()

    result_text = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_text, font=('Helvetica', 12), wraplength=500, justify=tk.LEFT)
    result_label.pack()

    website_var = tk.IntVar()

    for idx, site in enumerate(websites, start=0):
        radio = tk.Radiobutton(root, text=site, variable=website_var, value=idx)
        radio.pack(anchor=tk.W)

    start_button = tk.Button(root, text="Старт", command=lambda: start_program(website_var, websites))
    start_button.pack()

    stop_button = tk.Button(root, text="Стоп", command=stop)
    stop_button.pack()

    continue_button = tk.Button(root, text="Продолжить", command=lambda: continue_timer(website_var, websites))
    continue_button.pack()

    root.protocol("WM_DELETE_WINDOW", lambda: on_exit(root))
    root.mainloop()

if __name__ == "__main__":
    main()