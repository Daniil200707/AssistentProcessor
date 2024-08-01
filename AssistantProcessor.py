import random
from memory import ShortcutMemory, LongTermMemory
from feelings import *
from threading import Thread

def main():
    """
    Main func
    :return: None
    """
    rose = ShortcutMemory()
    rose2 = LongTermMemory()
    while True:
        chars = listen()
        text = chars[14:-3]
        rose.remember(text)
        print(rose.memory)
        separated_text = rose.get_memory()
        rose2.remember(separated_text)
        print(rose2.memory)

        end = len(rose2.memory) - 1
        end2 = len(rose.memory) - 1

        if len(rose2.memory) > 1:
            Thread(target=say_massage(rose2.memory[random.randint(0, end)]))
        elif len(rose.memory) > 1:
            Thread(target=say_massage(rose.memory[random.randint(0, end2)]))

if __name__ == "__main__":
    main()
