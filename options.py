from tkinter import *
import json

def open_command(command):
    with open("commands.json", "r", encoding="utf-8-sig") as command_file:
        command_dictionary = json.load(command_file)
    command_list = command.split("\"")
    string_command = command_list[3]
    string_list = string_command.split()
    for element in string_list:
        if element in command_dictionary:
            return command_dictionary[element]

def save_settings():
    with open("commands.json", "r") as json_file:
        json_dictionary = json.load(json_file)
    set_key = name_entry.get()
    set_value = url_entry.get()
    json_dictionary[set_key] = set_value

    out_label['text'] = f'{set_key}: {set_value}'

    with open("commands.json", "w", encoding="utf-8") as json_file:
        json.dump(json_dictionary, json_file, ensure_ascii=False, indent=4)

root = Tk()
root['bg'] = "#ffffff"
root.title("parameters")
root.geometry("500x400")

url_label = Label(text="Введите адресс сайта:")
url_label.pack(anchor="nw")

url_entry = Entry()
url_entry.pack(anchor="n")

name_label = Label(text="Введите команду в одно слово:")
name_label.pack(anchor="nw")

name_entry = Entry()
name_entry.pack(anchor="n")

save_button = Button(command=save_settings, text="сохранить")
save_button.pack(anchor="se")

out_label = Label(text="")
out_label.pack(anchor="nw")

def start():
    root.mainloop()

if __name__ == "__main__":
    # start()
    print(open_command('{"text" : "открой объект"}'))
