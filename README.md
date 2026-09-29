# 🎙️ Minnu – AI Voice Assistant

Minnu is a Python-based personal AI voice assistant that allows users to interact with their laptop using natural voice commands. It combines **Speech Recognition, Google Gemini AI, and Text-to-Speech** to listen, understand, process, and respond to users through voice.

## ✨ Features

* 🎤 **Voice Input** – Converts spoken commands into text using SpeechRecognition.
* 🧠 **AI-Powered Responses** – Uses Google Gemini API to answer general questions.
* 🔊 **Text-to-Speech** – Responds to users using the Windows SAPI5 voice engine.
* ⏰ **Time & Date** – Provides the current time and date.
* 👤 **Assistant Identity** – Can introduce itself as Minnu.
* 💻 **Application Control** – Can open applications such as:

  * Notepad
  * Calculator
  * Google Chrome
  * Visual Studio Code
  * File Explorer
* 🌐 **Web Assistance** – Designed to support web searches and online commands.
* 🧠 **Conversation Memory** – Project structure supports storing previous interactions.
* 🛑 **Voice Exit Commands** – Can stop when the user says commands such as "exit", "stop", or "goodbye".
* 🔐 **Secure API Configuration** – Gemini API credentials are stored using environment variables.

## 🛠️ Technologies Used

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Core programming language       |
| SpeechRecognition | Voice-to-text conversion        |
| PyAudio           | Microphone input                |
| pyttsx3           | Text-to-speech                  |
| Google Gemini API | AI-powered responses            |
| google-genai      | Gemini Python SDK               |
| python-dotenv     | Environment variable management |
| psutil            | System information              |
| Windows SAPI5     | Voice output                    |

## 📁 Project Structure

```text
voiceassitant/
│
├── venv/                   # Python virtual environment
│
├── main.py                 # Main assistant program
├── brain.py                # Gemini AI integration
├── memory.py               # Conversation memory
├── system_control.py       # Laptop/application control
├── web_control.py          # Web-related commands
├── system_info.py          # System information
├── test_brain.py           # Gemini API testing
│
├── .env                    # API key (DO NOT upload)
├── .gitignore              # Git ignored files
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## ⚙️ Requirements

Before running Minnu, make sure you have:

* Windows 10/11
* Python 3.10+
* Working microphone
* Speakers/headphones
* Internet connection
* Google Gemini API key

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/voiceassitant.git
```

Go to the project directory:

```bash
cd voiceassitant
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

You should see:

```text
(venv) PS C:\...\voiceassitant>
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, you can install the main dependencies with:

```powershell
python -m pip install SpeechRecognition pyttsx3 PyAudio google-genai python-dotenv psutil
```

## 🔑 Gemini API Setup

Minnu uses the Google Gemini API for AI-powered conversations.

Create your Gemini API key using:

**Google AI Studio:** https://aistudio.google.com/

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

### ⚠️ Security

Never upload your API key to GitHub.

Your `.gitignore` should contain:

```text
venv/
.env
__pycache__/
*.pyc
```

## 🧠 Gemini Configuration

The AI functionality is handled by `brain.py`.

Example:

```python
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def ask_ai(question):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )

    return response.text
```

## ▶️ Running Minnu

Make sure the virtual environment is active:

```powershell
.\venv\Scripts\Activate.ps1
```

Then run:

```powershell
python main.py
```

Minnu will start with a message similar to:

```text
Minnu: Hello! Your Minnu is ready to assist you.
You can ask me questions or give me commands.
```

You can then speak naturally.

### Example Commands

```text
"What is Python?"
"What is machine learning?"
"What is the meaning of Joshika?"
"What is the current time?"
"What is today's date?"
"What is your name?"
"Open Notepad"
"Open Calculator"
"Open Chrome"
"Open VS Code"
"Exit"
```

## 🔄 How Minnu Works

```text
             🎤 User Voice
                   │
                   ▼
          Speech Recognition
                   │
                   ▼
             Voice Command
                   │
                   ▼
          ┌─────────────────┐
          │ Command Handler │
          └────────┬────────┘
                   │
          ┌────────┴─────────┐
          │                  │
          ▼                  ▼
   Local Commands       AI Questions
          │                  │
          │                  ▼
          │           Google Gemini
          │                  │
          └────────┬─────────┘
                   ▼
             Text Response
                   │
                   ▼
            Text-to-Speech
                   │
                   ▼
                🔊 Minnu
```

## 🧪 Testing Gemini

Before running the complete assistant, you can test the Gemini connection:

```powershell
python test_brain.py
```

A successful test should return an AI-generated response.

## 🔮 Future Improvements

Planned improvements for Minnu include:

* 🎙️ Natural female neural voice
* 🗣️ Improved wake-word detection
* 🧠 Better conversational memory
* 🌐 Google and YouTube search
* 📂 File and folder management
* 💻 More Windows system controls
* 🔋 Battery and system monitoring
* 📧 Email assistance
* 📅 Calendar integration
* 🌦️ Weather information
* 🖥️ Graphical User Interface (GUI)
* 🚀 Start Minnu automatically with Windows
* 📦 Package Minnu as a standalone Windows application
* 🌍 Multilingual voice interaction

## 🎯 Project Goals

The main goal of Minnu is to build a practical AI assistant that combines:

* Voice interaction
* Generative AI
* Automation
* System control
* Natural language processing

The project is also designed as a learning project to understand how **AI APIs, Python automation, speech recognition, and text-to-speech technologies** can be integrated into a single application.

## 👩‍💻 Author

**Kusuma**

B.Tech Graduate | Python | AI | Web Development

## 📌 Project Status

🚧 **Actively Developing**

Minnu is currently capable of:

* Listening to voice commands
* Converting speech to text
* Answering questions using Gemini AI
* Speaking responses
* Executing basic laptop commands

More features are being added progressively.

## 📄 License

This project is created for educational and portfolio purposes.
