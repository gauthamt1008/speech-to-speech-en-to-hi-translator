"""
Text-to-Speech module using Google TTS API with pyttsx3 fallback
"""
import os
from gtts import gTTS
import pyttsx3

def text_to_speech(text, output_file, original_text=None):
    """
    Convert text to speech using Google TTS and save to file
    """
    try:
        if not text or not text.strip():
            print("No text provided for TTS")
            return False

        # Clean and prepare the text
        text = text.strip()

        # Try Google Translate TTS API directly (more reliable for Hindi)
        try:
            print(f"Generating Hindi TTS for: {text}")

            # Use Google Translate TTS API directly
            import requests
            from urllib.parse import quote

            # URL encode the text
            encoded_text = quote(text.encode('utf-8'))

            # Google Translate TTS URL
            tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_text}&tl=hi&total=1&idx=0&textlen={len(text)}&client=tw-ob"

            # Download the audio
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            response = requests.get(tts_url, headers=headers, timeout=15)

            if response.status_code == 200:
                with open(output_file, 'wb') as f:
                    f.write(response.content)

                # Verify the file was created and has content
                if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                    print(f"Google Translate TTS saved to: {output_file}")
                    return True

        except Exception as google_tts_error:
            print(f"Google Translate TTS failed: {google_tts_error}")

        # Fallback to gTTS if Google Translate TTS fails
        try:
            print("Trying gTTS Hindi fallback...")

            # Create Google TTS instance for Hindi
            tts = gTTS(text=text, lang='hi', slow=False)
            tts.save(output_file)

            # Verify Hindi TTS worked
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                print(f"gTTS Hindi TTS saved to: {output_file}")
                return True

        except Exception as gtts_error:
            print(f"gTTS Hindi TTS failed: {gtts_error}")

        # Try pyttsx3 for Hindi TTS (better Unicode support)
        try:
            print("Trying pyttsx3 Hindi TTS...")
            engine = pyttsx3.init()

            # Set Hindi voice if available
            voices = engine.getProperty('voices')
            hindi_voice = None
            for voice in voices:
                if 'hindi' in voice.name.lower() or 'hi' in voice.name.lower():
                    hindi_voice = voice
                    break

            if hindi_voice:
                engine.setProperty('voice', hindi_voice.id)
            else:
                # Use system default if no Hindi voice
                pass

            engine.setProperty('rate', 180)  # Speed
            engine.save_to_file(text, output_file)
            engine.runAndWait()

            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                print(f"pyttsx3 Hindi TTS saved to: {output_file}")
                return True

        except Exception as pyttsx3_error:
            print(f"pyttsx3 Hindi TTS failed: {pyttsx3_error}")

        # Final fallback to English TTS if Hindi fails
        try:
            print("Trying English TTS fallback...")

            # Use the original English text for TTS if available
            # This gives users the English pronunciation of their input
            fallback_text = original_text if original_text else "Translation completed successfully."

            tts = gTTS(text=fallback_text, lang='en', slow=False)
            tts.save(output_file)

            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                print(f"English TTS fallback saved to: {output_file}")
                return True

        except Exception as english_error:
            print(f"English TTS fallback also failed: {english_error}")

        print("TTS file was not created or is empty")
        return False

    except Exception as e:
        print(f"TTS error: {e}")
        return False

def text_to_speech_english(text, output_file):
    """
    Convert English text to speech (fallback)
    """
    try:
        if not text or not text.strip():
            return False

        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(output_file)

        return os.path.exists(output_file) and os.path.getsize(output_file) > 0

    except Exception as e:
        print(f"English TTS error: {e}")
        return False

def get_supported_languages():
    """
    Get list of supported languages
    """
    return ['hi', 'en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ja', 'ko', 'zh']

def get_audio_duration(text, lang='hi'):
    """
    Estimate audio duration based on text length
    """
    # Rough estimation: ~150 characters per minute for Hindi
    chars_per_minute = 150 if lang == 'hi' else 200
    estimated_minutes = len(text) / chars_per_minute
    return max(1, int(estimated_minutes * 60))  # At least 1 second