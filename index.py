import speech_recognition as sr

mic = sr.Recognizer()

with sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source)

    print("Let's start! Speak something...")

    audio = mic.listen(source)

    try:
        phrase = mic.recognize_google(audio, language='pt-BR')
        print("You said: " + phrase)

    except sr.UnknownValueError:
        print("oops... something goes wrong.")