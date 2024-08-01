import vosk
import sounddevice as sd
import soundfile as sf

def listen():  # Слушает пользователя
    """
    Listen user
    :return: listening result
    """
    print("Говорите")
    audio_data2 = sd.rec(int(16000 * 8), 16000, channels=1)
    sd.wait()

    # Сохраните записанные аудио-данные в файл
    sf.write("../recorded_audio.wav", audio_data2, 16000)

    # Загрузите записанные аудио-данные из файла
    audio_data2, sample_rate = sf.read("../recorded_audio.wav")
    print(f"Вы сказали: {audio_data2}")

    model = vosk.Model("feelings/vosk-model-small-ru-0.22")

    recognizer = vosk.KaldiRecognizer(model, 16000)
    with open("../recorded_audio.wav", "rb") as audio_file:
        # Чтение аудиофайла и распознавание речи
        audio_data = audio_file.read()
        recognizer.AcceptWaveform(audio_data)

    # Получение результатов распознавания
    result = recognizer.FinalResult()
    print(result)
    return result
