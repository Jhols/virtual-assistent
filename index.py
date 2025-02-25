import speech_recognition as sr
import re

name = ''

while(True):
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)

        print("Let's start! Speak something...")

        audio = mic.listen(source)

        try:
            phrase = mic.recognize_google(audio, language='en-US')

            print("You said: " + phrase)

            if (re.search(r'\b' + "bye-bye" + r'\b', format(phrase))):
                print('See you soon!')
                break

            elif (re.search(r'\b' + "help" + r'\b', format(phrase))):
                print('Something related to helping.')

            elif (re.search(r'\b' + "my name is" + r'\b', format(phrase))):
                t = re.search("my name is (.*)", format(phrase))
                if t:
                    name = t.group(1)
                    print("Your name is " + name)

            elif (re.search(r'\b' + "what is my name" + r'\b', format(phrase))):
                if name:
                    print("Your name is " + name)
                else:
                    print("I don't know your name. Please, tell me.")

            elif (re.search(r'\b' + "thank you" + r'\b', format(phrase))):
                print("You're welcome!")

        except sr.UnknownValueError:
            print("oops... something goes wrong.")