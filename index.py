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

            # Goodbye command
            if re.search(r'\b(bye|goodbye|see you|bye-bye|take care)\b', phrase, re.IGNORECASE):
                engineAnswer('See you soon!')
                break

            # Greeting command
            elif re.search(r'\b(hello|hi|hey|hi there)\b', phrase, re.IGNORECASE):
                engineAnswer('Hi there!')

            # Help command
            elif re.search(r'\b(help|assist|need help)\b', phrase, re.IGNORECASE):
                engineAnswer('How can I help you today?')

            # Save user's name
            elif re.search(r'\b(my name is|i am|call me)\b', phrase, re.IGNORECASE):
                t = re.search(r"(my name is|i am|call me)\s+(.*)", phrase, re.IGNORECASE)
                if t:
                    name = t.group(2)
                    engineAnswer(f"Your name is {name}")

            # Ask user's name
            elif re.search(r'\b(what is my name|what’s my name|tell me my name)\b', phrase, re.IGNORECASE):
                if name:
                    engineAnswer(f"Your name is {name}")
                else:
                    engineAnswer("I don't know your name. Please, tell me.")

            # Thank you command
            elif re.search(r'\b(thank you|thanks|thanks a lot|thank you very much)\b', phrase, re.IGNORECASE):
                engineAnswer("You're welcome!")

        except sr.UnknownValueError:
            print("Oops... something went wrong.")
