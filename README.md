# English to Hindi Speech Translator

A simple web application that converts English speech/text to Hindi with audio playback.

## 🚀 Features

- **🎤 Voice Input**: Record English speech using browser's Web Speech API
- **✏️ Text Input**: Type or edit English text manually
- **🌐 Translation**: Google Translate API for English → Hindi conversion
- **🔊 Audio Playback**: Hindi speech synthesis
- **📱 Responsive**: Works on desktop and mobile browsers

## 📁 Files

```
speech_translator_website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── run.bat               # Windows startup script
├── run.sh                # Linux/Mac startup script
├── models/               # TTS model files
├── modules/              # Application modules
├── templates/           # HTML templates
└── uploads/            # Temporary files
```

## 🛠️ Quick Start

### Prerequisites
- Python 3.10+
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Run the Application

**Windows:**
```cmd
cd speech_translator_website
run.bat
```

**Linux/Mac:**
```bash
cd speech_translator_website
chmod +x run.sh
./run.sh
```

**Manual:**
```bash
cd speech_translator_website
pip install -r requirements.txt
python app.py
```

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