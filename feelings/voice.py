import pyttsx3

def say_massage(massage):
    """
    The AI voice
    :param massage: text for voicing
    :return: AI voice
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # установите скорость речи по вашему желанию
    engine.setProperty('volume', 1)  # установите громкость речи по вашему желанию
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Anatol")
    engine.say(massage)
    engine.runAndWait()

if __name__ == "__main__":
    say_massage("Привіт, як справи у тебе")
