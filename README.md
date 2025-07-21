# DiagnoSpeak
### _Talk. Show. Know._

**DiagnoSpeak** is an experimental AI-powered virtual doctor assistant that understands medical concerns through **voice** and **image**, analyzes them using **LLaMA via Groq**, and responds in a Elevenlabs generated **human voice**.

>  **Disclaimer**: This tool is intended strictly for educational or research purposes and must not be used for real medical diagnostics or treatment.

---

## Features

- Voice input from the user
- Image analysis of medical concerns (e.g., acne)
- AI-generated medical opinion based on voice and image
- Voice-based response using ElevenLabs/gTTS(Google Text-to-Speech)
- Uses LLM models: Whisper (Groq) & LLaMA-4 (Meta)

---

## Project Structure


## Installation

1. **Clone the repository**

```
git clone https://github.com/imaduddin27/DiagnoSpeak
cd DiagnoSpeak
```

2. **Create and activate virtual environment**

```
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**

```
pip install -r requirements.txt
```

4. **Set up your .env file**
```
# .env
ELEVEN_API_KEY=your_elevenlabs_api_key
GROQ_API_KEY=your_groq_api_key
```

## How It Works

1. The user **speaks their concern** using the microphone.

2. The user **uploads an image** (e.g., a skin condition etc.).

3. The app processes the inputs:
   - **Converts voice to text** using **Whisper (via Groq)**
   - **Analyzes the image** using **LLaMA 4 (Meta)**
   - **Generates a medical-style response** based on both inputs
   - **Converts the text response to voice** using **ElevenLabs** or **gTTS**

4. The final output includes:
   - The **transcribed speech**
   - The **AI doctor's diagnostic response**
   - The **spoken audio reply**

## Running the App
```
python app.py
```

## Notes

 - Make sure your machine has a microphone and speaker access.
 - This is a prototype and should not be relied on for any clinical usage.
 - Audio playback support may vary based on OS (Windows, macOS, Linux).



## Required System Dependencies

For this project to work properly, you'll need to install **FFmpeg** and **PortAudio** on your system.

### Installation Instructions

#### macOS
```bash
# 1. Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install dependencies
brew install ffmpeg portaudio
```

#### Linux (Debian/Ubuntu)
```bash
# Update package list and install dependencies
sudo apt update && sudo apt install -y ffmpeg portaudio19-dev
```

#### Windows

**FFmpeg**:
1. Download from [ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract the ZIP file
3. Add the `bin` folder to your system PATH:
   - Right-click "This PC" → Properties → Advanced system settings
   - Environment Variables → Select "Path" → Edit
   - Add new path to the `bin` folder (e.g., `C:\ffmpeg\bin`)

**PortAudio**:
1. Download from [portaudio.com/download.html](http://www.portaudio.com/download.html)
2. Run the installer and follow the instructions

>  **Note**: After installation on Windows, you may need to restart your system for PATH changes to take effect.




