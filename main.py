# import speech_recognition as sr
# import pyttsx3
# from datetime import datetime
# import time


# # -----------------------------
# # TEXT TO SPEECH
# # -----------------------------

# def speak(text):
#     print("Minnu:", text)

#     try:
#         # Create a fresh TTS engine every time
#         engine = pyttsx3.init("sapi5")

#         engine.setProperty("rate", 165)
#         engine.setProperty("volume", 1.0)

#         voices = engine.getProperty("voices")

#         if voices:
#             engine.setProperty("voice", voices[0].id)

#         engine.say(text)
#         engine.runAndWait()

#         engine.stop()

#     except Exception as e:
#         print("TTS Error:", e)


# # -----------------------------
# # SPEECH RECOGNITION
# # -----------------------------

# recognizer = sr.Recognizer()


# def listen():

#     with sr.Microphone() as source:

#         print("\nListening...")

#         recognizer.adjust_for_ambient_noise(
#             source,
#             duration=0.5
#         )

#         try:

#             audio = recognizer.listen(
#                 source,
#                 timeout=5,
#                 phrase_time_limit=8
#             )

#         except sr.WaitTimeoutError:

#             print("No speech detected.")

#             return ""

#     print("Recognizing...")

#     try:

#         command = recognizer.recognize_google(audio)

#         command = command.lower().strip()

#         print("You:", command)

#         return command

#     except sr.UnknownValueError:

#         print("Could not understand audio.")

#         return ""

#     except sr.RequestError as e:

#         print("Speech recognition error:", e)

#         return ""


# # -----------------------------
# # COMMAND HANDLER
# # -----------------------------

# def handle_command(command):

#     command = command.lower().strip()

#     print("Processing command:", command)

#     # Hello Minnu
#     if (
#         "hello minnu" in command
#         or "hello minu" in command
#         or "hi minnu" in command
#         or "hi minu" in command
#     ):

#         speak("Hello! How can I help you?")
#         return True


#     # Time
#     elif "time" in command:

#         current_time = datetime.now().strftime("%I:%M %p")

#         speak(
#             f"The current time is {current_time}"
#         )

#         return True


#     # Date
#     elif "date" in command:

#         current_date = datetime.now().strftime("%d %B %Y")

#         speak(
#             f"Today's date is {current_date}"
#         )

#         return True


#     # Name
#     elif (
#         "your name" in command
#         or "who are you" in command
#     ):

#         speak(
#             "I am Minnu, your personal voice assistant."
#         )

#         return True


#     # Exit
#     elif (
#         "stop" in command
#         or "exit" in command
#         or "goodbye" in command
#     ):

#         speak(
#             "Goodbye! Have a nice day."
#         )

#         return False


#     # Unknown command
#     else:

#         speak(
#             f"I heard you say {command}"
#         )

#         return True


# # -----------------------------
# # MAIN PROGRAM
# # -----------------------------

# def main():

#     speak(
#         "Hello! Your Minnu is ready to assist you. "
#         "Say hello Minnu to start."
#     )

#     time.sleep(1)

#     while True:

#         command = listen()

#         if command:

#             should_continue = handle_command(command)

#             if not should_continue:
#                 break


# # -----------------------------
# # START PROGRAM
# # -----------------------------

# if __name__ == "__main__":
#     main()
import speech_recognition as sr
import pyttsx3

from datetime import datetime

import time


# AI
from brain import ask_ai


# Memory
from memory import (
    add_memory,
    get_memory,
    clear_memory
)


# System control
from system_control import open_application


# Web control
from web_control import (
    google_search,
    youtube_search,
    open_website
)


# System information
from system_info import (
    get_battery,
    get_system_info,
    get_ram
)


# -----------------------------
# TEXT TO SPEECH
# -----------------------------

def speak(text):

    print("Minnu:", text)


    try:

        engine = pyttsx3.init("sapi5")


        engine.setProperty(
            "rate",
            165
        )


        engine.setProperty(
            "volume",
            1.0
        )


        voices = engine.getProperty(
            "voices"
        )


        if voices:

            engine.setProperty(
                "voice",
                voices[0].id
            )


        engine.say(text)

        engine.runAndWait()

        engine.stop()


    except Exception as e:

        print(
            "TTS Error:",
            e
        )


# -----------------------------
# SPEECH RECOGNITION
# -----------------------------

recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:

        print("\nListening...")


        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )


        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )


        except sr.WaitTimeoutError:

            print(
                "No speech detected."
            )

            return ""


    print(
        "Recognizing..."
    )


    try:

        command = recognizer.recognize_google(
            audio
        )


        command = command.lower().strip()


        print(
            "You:",
            command
        )


        return command


    except sr.UnknownValueError:

        print(
            "Could not understand audio."
        )

        return ""


    except sr.RequestError as e:

        print(
            "Speech recognition error:",
            e
        )

        return ""


# -----------------------------
# COMMAND HANDLER
# -----------------------------

def handle_command(command):

    command = command.lower().strip()


    print(
        "Processing:",
        command
    )


    # -----------------------------
    # GREETING
    # -----------------------------

    if (
        "hello minnu" in command
        or "hello minu" in command
        or "hi minnu" in command
        or "hi minu" in command
        or "hey minnu" in command
        or "hey minu" in command
    ):

        speak(
            "Hello! How can I help you?"
        )

        return True


    # -----------------------------
    # TIME
    # -----------------------------

    if "time" in command:

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )


        speak(
            f"The current time is {current_time}"
        )


        return True


    # -----------------------------
    # DATE
    # -----------------------------

    if "date" in command:

        current_date = datetime.now().strftime(
            "%d %B %Y"
        )


        speak(
            f"Today's date is {current_date}"
        )


        return True


    # -----------------------------
    # NAME
    # -----------------------------

    if (
        "your name" in command
        or "who are you" in command
    ):

        speak(
            "I am Minnu, your personal AI voice assistant."
        )


        return True


    # -----------------------------
    # CLEAR MEMORY
    # -----------------------------

    if (
        "clear memory" in command
        or "forget everything" in command
    ):

        clear_memory()


        speak(
            "I cleared our conversation memory."
        )


        return True


    # -----------------------------
    # OPEN APPLICATIONS
    # -----------------------------

    if "open notepad" in command:

        response = open_application(
            "notepad"
        )

        speak(response)

        return True


    if "open calculator" in command:

        response = open_application(
            "calculator"
        )

        speak(response)

        return True


    if (
        "open file explorer" in command
        or "open explorer" in command
    ):

        response = open_application(
            "explorer"
        )

        speak(response)

        return True


    if "open chrome" in command:

        response = open_application(
            "chrome"
        )

        speak(response)

        return True


    if (
        "open vs code" in command
        or "open visual studio code" in command
    ):

        response = open_application(
            "vscode"
        )

        speak(response)

        return True


    # -----------------------------
    # GOOGLE SEARCH
    # -----------------------------

    if "search google for" in command:

        query = command.replace(
            "search google for",
            "",
            1
        ).strip()


        if query:

            response = google_search(
                query
            )

            speak(response)


        return True


    # -----------------------------
    # YOUTUBE SEARCH
    # -----------------------------

    if "search youtube for" in command:

        query = command.replace(
            "search youtube for",
            "",
            1
        ).strip()


        if query:

            response = youtube_search(
                query
            )

            speak(response)


        return True


    # -----------------------------
    # WEBSITES
    # -----------------------------

    if "open youtube" in command:

        response = open_website(
            "youtube"
        )

        speak(response)

        return True


    if "open google" in command:

        response = open_website(
            "google"
        )

        speak(response)

        return True


    if "open github" in command:

        response = open_website(
            "github"
        )

        speak(response)

        return True


    if "open gmail" in command:

        response = open_website(
            "gmail"
        )

        speak(response)

        return True


    # -----------------------------
    # BATTERY
    # -----------------------------

    if (
        "battery" in command
        or "battery percentage" in command
    ):

        response = get_battery()

        speak(response)

        return True


    # -----------------------------
    # RAM
    # -----------------------------

    if (
        "ram" in command
        or "memory usage" in command
    ):

        response = get_ram()

        speak(response)

        return True


    # -----------------------------
    # SYSTEM INFORMATION
    # -----------------------------

    if (
        "system information" in command
        or "computer information" in command
        or "computer specifications" in command
    ):

        response = get_system_info()

        speak(response)

        return True


    # -----------------------------
    # EXIT
    # -----------------------------

    if (
        "stop" in command
        or "exit" in command
        or "goodbye" in command
    ):

        speak(
            "Goodbye! Have a nice day."
        )

        return False


    # -----------------------------
    # GEMINI AI
    # -----------------------------

    # print(
    #     "Sending question to Gemini..."
    # )


    # conversation = get_memory()


    # answer = ask_ai(
    #     command,
    #     conversation
    # )


    # print(
    #     "Gemini:",
    #     answer
    # )


    # speak(answer)


    # # Save conversation
    # add_memory(
    #     command,
    #     answer
    # )


    # return True
    # -----------------------------
    # GEMINI AI
    # -----------------------------

    print(
        "Sending question to Gemini..."
    )

    answer = ask_ai(command)

    print(
        "Gemini:",
        answer
    )

    speak(answer)

    add_memory(
        command,
        answer
    )

    return True


# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():

    speak(
        "Hello! Your Minnu is ready to assist you. "
        "You can ask me questions or give me commands."
    )


    time.sleep(1)


    while True:

        command = listen()


        if command:

            should_continue = handle_command(
                command
            )


            if not should_continue:

                break


# -----------------------------
# START
# -----------------------------

if __name__ == "__main__":

    main()