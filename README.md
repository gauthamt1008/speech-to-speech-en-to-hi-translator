# English to Hindi Speech Translator

A simple web application that converts English speech/text to Hindi with audio playback.

## 🚀 Features

- **🎤 Voice Input**: Record English speech using browser's Web Speech API
- **✏️ Text Input**: Type or edit English text manually
- **🌐 Translation**: Google Translate API for English → Hindi conversion
- **🔊 Audio Playback**: Hindi speech synthesis using pre-trained models
- **📱 Responsive**: Works on desktop and mobile browsers

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Speech Recognition**: Vosk, Web Speech API
- **Translation**: Google Translate API
- **Text-to-Speech**: gTTS, IndicTrans models
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Ready for local hosting or cloud deployment

##  Project Structure

```
speech_translator_website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── run.sh                # Linux/Mac startup script
├── .gitignore            # Git ignore file
├── models/               # TTS model files
├── modules/              # Application modules
│   ├── stt.py           # Speech-to-text module
│   ├── translator.py    # Translation module
│   └── tts.py           # Text-to-speech module
└── templates/           # HTML templates
    └── index.html       # Main web interface
```

## 🛠️ Quick Start

### Prerequisites
- Python 3.10+
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gauthamt1008/speech-to-speech-en-to-hi-translator.git
   cd speech-to-speech-en-to-hi-translator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   **Note:** The project uses APIs for speech recognition, translation, and text-to-speech, so no local models are required. The `models/` folder is included for potential future offline functionality but is not currently used.

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   Navigate to `http://localhost:5000`

Then open: `http://localhost:5000`

## 🎯 How to Use

### Voice Input:
1. Click **"🎤 Start Voice Input"**
2. Allow microphone access
3. Speak English clearly
4. Click **"🌐 Translate"**
5. Click **"🔊 Play Hindi Audio"**

### Text Input:
1. Click in the English text field
2. Type your English text
3. Click **"🌐 Translate"**
4. Click **"🔊 Play Hindi Audio"**

## 🔧 Troubleshooting

- **No speech recognition**: Use Chrome/Firefox/Safari
- **Microphone blocked**: Allow permissions in browser
- **No audio**: Check speakers and browser settings
- **Translation fails**: Check internet connection

---

**Ready to translate English to Hindi!** 🇮🇳