from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Project Report: English to Hindi Speech Translator', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Page 1: Overview
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Project Overview", 0, 1)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, "This is a simple web application built with Flask that converts English speech or text to Hindi with audio playback. It utilizes browser's Web Speech API for voice input, Google Translate API for translation, and text-to-speech synthesis for Hindi audio output.")

pdf.ln(10)
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Key Features", 0, 1)
pdf.set_font("Arial", size=12)
features = [
    "- Voice Input: Record English speech using browser's Web Speech API",
    "- Text Input: Type or edit English text manually",
    "- Translation: Google Translate API for English to Hindi conversion",
    "- Audio Playback: Hindi speech synthesis",
    "- Responsive: Works on desktop and mobile browsers"
]
for feature in features:
    pdf.cell(0, 10, feature, 0, 1)

pdf.ln(10)
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Architecture", 0, 1)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, "The application is structured as follows:\n- app.py: Main Flask application handling routes and logic\n- modules/: Contains STT, translator, and TTS modules\n- models/: Pre-trained models for speech processing\n- templates/: HTML templates for the web interface\n- uploads/: Temporary storage for uploaded files")

# Page 2: Installation and Usage
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Installation", 0, 1)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, "Prerequisites:\n- Python 3.10+\n- Modern web browser (Chrome, Firefox, Safari, Edge)\n\nSteps:\n1. Navigate to the project directory\n2. Install dependencies: pip install -r requirements.txt\n3. Run the application: python app.py\n4. Open http://localhost:5000 in your browser")

pdf.ln(10)
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Usage", 0, 1)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, "Voice Input:\n1. Click 'Start Voice Input'\n2. Allow microphone access\n3. Speak English clearly\n4. Click 'Translate'\n5. Click 'Play Hindi Audio'\n\nText Input:\n1. Type English text in the field\n2. Click 'Translate'\n3. Click 'Play Hindi Audio'")

pdf.ln(10)
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Troubleshooting", 0, 1)
pdf.set_font("Arial", size=12)
issues = [
    "- No speech recognition: Use Chrome/Firefox/Safari",
    "- Microphone blocked: Allow permissions in browser",
    "- No audio: Check speakers and browser settings",
    "- Translation fails: Check internet connection"
]
for issue in issues:
    pdf.cell(0, 10, issue, 0, 1)

pdf.output("project_report.pdf")