import speech_recognition as sr
import re
import pyttsx3

name = ''

def engineAnswer(answer):
    engine.say(answer)
    engine.runAndWait()
    print(answer)

while(True):
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        engine = pyttsx3.init()
        
        # engine.setProperty('voice', 'com.apple.speech.synthesis.voice.luciana') # for portuguese

        mic.adjust_for_ambient_noise(source)

        print("Let's start! Speak something...")

        audio = mic.listen(source)

        try:
            phrase = mic.recognize_google(audio, language='en-US')

            print("You said: " + phrase)

            if (re.search(r'\b' + "bye-bye" + r'\b', format(phrase))):
                engineAnswer('See you soon!')
                break

            elif (re.search(r'\b' + "hello" + r'\b', format(phrase))):
                engineAnswer('Hi there!')

            elif (re.search(r'\b' + "help" + r'\b', format(phrase))):
                engineAnswer('Something related to helping.')

            elif (re.search(r'\b' + "my name is" + r'\b', format(phrase))):
                t = re.search("my name is (.*)", format(phrase))
                if t:
                    name = t.group(1)
                    engineAnswer("Your name is " + name)


            elif (re.search(r'\b' + "what is my name" + r'\b', format(phrase))):
                if name:
                   engineAnswer("Your name is " + name)

                else:
                    engineAnswer("I don't know your name. Please, tell me.")

            elif (re.search(r'\b' + "thank you" + r'\b', format(phrase))):
                engineAnswer("You're welcome!")

        except sr.UnknownValueError:
            print("oops... something goes wrong.")