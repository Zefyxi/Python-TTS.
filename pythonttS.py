# Requires: pip install pyttsx3

import pyttsx3

def text_to_speech():
    while True:
        text = input("Enter text (or type 'exit' to quit): ")
        if text.lower() == "exit":
            break
        engine = pyttsx3.init()  
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    text_to_speech()
