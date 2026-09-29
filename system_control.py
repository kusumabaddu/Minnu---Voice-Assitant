import subprocess
import os


def open_application(app):

    if app == "notepad":

        subprocess.Popen("notepad.exe")

        return "Opening Notepad."


    elif app == "calculator":

        subprocess.Popen("calc.exe")

        return "Opening Calculator."


    elif app == "explorer":

        subprocess.Popen("explorer.exe")

        return "Opening File Explorer."


    elif app == "chrome":

        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expandvars(
                r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
            )
        ]


        for path in chrome_paths:

            if os.path.exists(path):

                subprocess.Popen(path)

                return "Opening Google Chrome."


        return "I couldn't find Google Chrome."


    elif app == "vscode":

        try:

            subprocess.Popen("code")

            return "Opening Visual Studio Code."

        except:

            return "I couldn't open Visual Studio Code."


    return "I don't know how to open that application."