from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import os
import io
import base64
from werkzeug.utils import secure_filename
import tempfile
import json
from datetime import datetime

# Import our translation modules
from modules.stt import record_and_transcribe
from modules.translator import translate_text
from modules.tts import text_to_speech

app = Flask(__name__)
CORS(app)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Get text from either form data or JSON
        english_text = ""

        if request.is_json:
            data = request.get_json()
            english_text = data.get('text', '').strip()
        else:
            english_text = request.form.get('text', '').strip()

        # If no text provided, check for audio file
        if not english_text:
            if 'audio' in request.files:
                audio_file = request.files['audio']
                if audio_file.filename != '':
                    # Save uploaded audio file
                    filename = secure_filename(audio_file.filename)
                    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    audio_file.save(audio_path)

                    # Process the audio file
                    english_text = record_and_transcribe(audio_path)

                    # Clean up audio file
                    os.remove(audio_path)

        if not english_text:
            return jsonify({'error': 'No text or audio provided'}), 400

        # Translate to Hindi
        hindi_text = translate_text(english_text)

        if not hindi_text:
            return jsonify({'error': 'Translation failed'}), 500

        # Generate speech
        audio_output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp3')
        success = text_to_speech(hindi_text, audio_output_path, english_text)

        if not success:
            return jsonify({'error': 'Speech generation failed'}), 500

        # History functionality removed

        # Read the generated audio file
        with open(audio_output_path, 'rb') as f:
            audio_data = f.read()

        # Convert to base64 for web transmission
        audio_b64 = base64.b64encode(audio_data).decode('utf-8')

        # Clean up audio file
        os.remove(audio_output_path)

        return jsonify({
            'english_text': english_text,
            'hindi_text': hindi_text,
            'audio_data': audio_b64,
            'audio_format': 'mp3'
        })

    except Exception as e:
        print(f"Translation error: {e}")
        return jsonify({'error': str(e)}), 500

# History functionality removed

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)