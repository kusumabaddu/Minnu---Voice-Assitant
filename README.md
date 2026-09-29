# Minnu---Voice-Assitant
# 🎙️ Minnu – AI Voice Assistant

**Minnu** is a Python-based AI voice assistant designed to interact with users through **voice commands and natural language conversations**. It combines speech recognition, text-to-speech, and Google's Gemini AI to provide an interactive assistant experience.

## 🚀 Features

* 🎤 **Voice Recognition** – Converts spoken commands into text.
* 🤖 **AI-Powered Conversations** – Uses Google Gemini AI to answer general questions.
* 🔊 **Text-to-Speech** – Responds to users using a clear voice.
* ⏰ **Time & Date** – Provides the current time and date.
* 👤 **User Interaction** – Can respond to basic personal commands.
* 🛑 **Voice Exit Command** – Allows users to stop the assistant using voice commands.
* 🔐 **Environment Variables** – Securely manages the Gemini API key using `.env`.
* 🐍 **Python Virtual Environment** – Uses a virtual environment for dependency management.

## 🛠️ Technologies Used

* **Python 3.12**
* **Google Gemini API**
* **SpeechRecognition**
* **Pyttsx3**
* **Google GenAI**
* **python-dotenv**
* **SAPI5 Speech Engine**

## 📂 Project Structure

```text
voiceassitant/
│
├── main.py
├── .env
├── requirements.txt
├── README.md
└── venv/
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/voiceassitant.git
cd voiceassitant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Never upload your `.env` file or API key to GitHub.

### 6. Run Minnu

```bash
python main.py
```

## 💬 Example Interaction

```text
Minnu: Hello! Your Minnu is ready to assist you.

Listening...

You: Hello Minnu

Minnu: Hello! How can I help you?

You: What is Python?

Minnu: Python is a high-level programming language...
```

## 🔮 Future Improvements

* 🌐 Web search integration
* 🎵 Music and media control
* 💻 System/application control
* 🌦️ Weather information
* 🗣️ Support for multiple languages
* 👩 Clearer and more natural female voice
* 🧠 Improved conversational memory
* 🖥️ Graphical User Interface (GUI)

## 🎯 Learning Outcomes

This project helped me gain practical experience in:

* Python programming
* API integration
* Generative AI and LLM integration
* Speech recognition
* Text-to-speech technology
* Environment variable management
* Python virtual environments
* Building an AI-based application

## 👩‍💻 Author

**Kusuma**

This project was developed as a personal learning project to explore **Python, Artificial Intelligence, APIs, and voice-based applications**.
