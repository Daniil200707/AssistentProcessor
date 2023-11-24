import vosk
import pyttsx3
import os
import webbrowser
import subprocess
import sounddevice as sd
import soundfile as sf
import random
import options as op

engine = pyttsx3.init()

def program_exit(process_name):  # Выключает программы
    os.system(f"taskkill /f /im {process_name}")


def open_https(https):  # Открывает сайты
    try:
        webbrowser.open(https)
    except TypeError:
        print("сайт не найден")

def open_program(program, checkbox="o"):  # Открывает программы
    if checkbox == "o":
        os.system(f"start {program}")
    elif checkbox == "s":
        subprocess.Popen(["explorer", program])
    else:
        print("CheckBoxError: You entered an incorrect checkbox value")


def open_inc_program(program, program_name):  # Открывает программы по их ярлыку
    try:
        os.startfile(program)
    except FileNotFoundError:
        speak(f"Я не нашла {program_name}")

def listen():  # Слушает пользователя
    print("Говорите")
    audio_data2 = sd.rec(int(16000 * 8), 16000, channels=1)
    sd.wait()

    # Сохраните записанные аудио-данные в файл
    sf.write("recorded_audio.wav", audio_data2, 16000)

    # Загрузите записанные аудио-данные из файла
    audio_data2, sample_rate = sf.read("recorded_audio.wav")
    print(f"Вы сказали: {audio_data2}")

    model = vosk.Model("vosk-model-small-ru-0.22")

    recognizer = vosk.KaldiRecognizer(model, 16000)
    with open("recorded_audio.wav", "rb") as audio_file:
        # Чтение аудиофайла и распознавание речи
        audio_data = audio_file.read()
        recognizer.AcceptWaveform(audio_data)

    # Получение результатов распознавания
    result = recognizer.FinalResult()
    print(result)
    return result


def speak(text):  # Создаёт голос
    engine.say(text)
    engine.runAndWait()
    print(text)

def create_password():
    list_of_symbols = ["`", "~", "1", "!", "2", "@", "3", "#", "4", "$", "5", "%", "6", "^", "7", "&", "8", "*", "9",
                       "(", "0", ")", "-", "_", "=", "+", "q", "Q", "w", "W", "e", "E", "r", "R", "t", "T", "y", "Y",
                       "u", "U", "i", "I", "o", "O", "p", "P", "[", "{", "]", "}", "a", "A", "s", "S", "d", "D", "f",
                       "F", "g", "G", "h", "H", "j", "J", "k", "K", "l", "L", ";", ":", "\'", "\"", "\\", "|", "z",
                       "Z", "x", "X", "c", "C", "v", "V", "b", "B", "n", "N", "m", "M", ",", "<", ".", ">", "/",  "?"]
    empty_line = ""
    for i in range(8):
        empty_line += list_of_symbols[random.randint(0, 94)]
    print("Пароль:" + empty_line)
    return empty_line

if __name__ == "__main__":
    sound = True
    while True:
        command = listen()  # Сюда попадает комманда от пользователя

        if sound:
            if "блокнот" in command:
                os.system("notepad.exe")
                speak("Открываю блокнот.")
            elif "вайбер" in command:
                if "открой" in command:
                    speak("Открываю Viber")
                    open_inc_program("C:/Users/Валюша/Desktop/Viber", "вайбер")
                elif "закрой" in command:
                    speak("Закрываю Viber")
                    program_exit("Viber.exe")
            elif "включи" in command:
                if "беззвучный" in command:
                    speak("Включаю беззвучный режим!")
                    sound = False
            elif "выход" in command:
                speak("До свидания!")
                exit()
            elif "гугл" in command:
                if "ютуб" in command:
                    if "открой" in command:
                        speak("Открываю Google YouTube")
                        open_inc_program("C:/Users/Валюша/Desktop/Google YouTube", "ютуб")
                elif "хром" in command:
                    if "открой" in command:
                        speak("Открываю Google Chrome")
                        open_inc_program("C:/Users/Валюша/Desktop/Google Chrome", "гул хром")
                    elif "закрой" in command:
                        speak("Закрываю Google Chrome")
                        program_exit("chrome.exe")
            elif "зум" in command:
                if "открой" in command:
                    speak("Открываю Zoom")
                    open_program(r'C:\Users\Валюша\AppData\Roaming\Zoom\bin\Zoom.exe', "зум")
                elif "закрой" in command:
                    speak("Закрываю Zoom")
                    program_exit("Zoom.exe")
            elif "игрушку" in command:
                if "открой" in command:
                    speak("Открываю powder toy")
                    open_inc_program("C:/Users/Валюша/Desktop/The powder toy", "порошковая игрушка")
                elif "закрой" in command:
                    speak("Закрываю powder toy")
                    program_exit("Powder.exe")
            elif "наклейки" in command:
                if "открой" in command:
                    speak("Открываю Погоду")
                    open_inc_program("C:/Users/Валюша/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch/"
                                     "Наліпки", "наклейки")
            elif "открой" in command:
                open_https(op.open_command(command))
            elif "параметры" in command:
                op.start()
            elif "погоду" in command:
                if "открой" in command:
                    speak("Открываю Погоду")
                    open_inc_program("C:/Users/Валюша/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch/"
                                     "Погода", "погода")
            elif "придумай" in command:
                if "пароль" in command:
                    speak("Пароль:" + create_password())
            elif "холст" in command:
                if "открой" in command:
                    speak("Открываю Canva")
                    open_inc_program("C:/Users/Валюша/Desktop/Canva", "канва")
                elif "закрой" in command:
                    speak("Закрываю Canva")
                    program_exit("Canva.exe")
            else:
                speak("Я Вас не поняла!")
        else:
            if "блокнот" in command:
                print(os.system("notepad.exe"))
                os.system("notepad.exe")
                print("Открываю блокнот.")
            elif "вайбер" in command:
                if "открой" in command:
                    print("Открываю Viber")
                    open_inc_program("C:/Users/Валюша/Desktop/Viber", "вайбер")
                elif "закрой" in command:
                    print("Закрываю Viber")
                    program_exit("Viber.exe")
            elif "выключи" in command:
                if "беззвучный" in command:
                    print("Выключаю беззвучный режим!")
                    sound = True
            elif "выход" in command:
                print("До свидания!")
                exit()
            elif "гугл" in command:
                if "ютуб" in command:
                    if "открой" in command:
                        print("Открываю Google YouTube")
                        open_inc_program("C:/Users/Валюша/Desktop/Google YouTube", "ютуб")
                elif "хром" in command:
                    if "открой" in command:
                        print("Открываю Google Chrome")
                        open_inc_program("C:/Users/Валюша/Desktop/Google Chrome", "гул хром")
                    elif "закрой" in command:
                        print("Закрываю Google Chrome")
                        program_exit("chrome.exe")
            elif "зум" in command:
                if "открой" in command:
                    print("Открываю Zoom")
                    open_program(r'C:\Users\Валюша\AppData\Roaming\Zoom\bin\Zoom.exe', "зум")
                elif "закрой" in command:
                    print("Закрываю Zoom")
                    program_exit("Zoom.exe")
            elif "игрушку" in command:
                if "открой" in command:
                    print("Открываю powder toy")
                    open_inc_program("C:/Users/Валюша/Desktop/The powder toy", "порошковая игрушка")
                elif "закрой" in command:
                    print("Закрываю powder toy")
                    program_exit("Powder.exe")
            elif "наклейки" in command:
                if "открой" in command:
                    print("Открываю Погоду")
                    open_inc_program("C:/Users/Валюша/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch/"
                                     "Наліпки", "наклейки")
            elif "открой" in command:
                print("Открываю")
                open_https(op.open_command(command))
            elif "параметры" in command:
                print("Открываю параметры")
                op.start()
            elif "погоду" in command:
                if "открой" in command:
                    print("Открываю Погоду")
                    open_inc_program("C:/Users/Валюша/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch/"
                                     "Погода", "погода")
            elif "придумай" in command:
                if "пароль" in command:
                    print("Пароль:" + create_password())
            elif "холст" in command:
                if "открой" in command:
                    print("Открываю Canva")
                    open_inc_program("C:/Users/Валюша/Desktop/Canva", "канва")
                elif "закрой" in command:
                    print("Закрываю Canva")
                    program_exit("Canva.exe")
            else:
                print("Я Вас не поняла!")
