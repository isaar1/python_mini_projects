print("**TEXT SPEAKER")

import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for better voice clarity and quality
engine.setProperty('rate', 120)  # Speed of speech (words per minute)
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)
engine.setProperty('voice', 'english')  # Voice selection

while True:
    # Input the text you want to speak
    text_to_speak = input("Enter text to speak (or 'q' to quit): ")

    if text_to_speak.lower() == 'q':
        break

    # Speak the text
    engine.say(text_to_speak)

    # Wait for the speech to complete
    engine.runAndWait()

# Quit the engine
engine.stop()
