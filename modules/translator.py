"""
Translation module using Google Translate API
"""
import os
import requests
from urllib.parse import quote

def translate_text(text):
    """
    Translate English text to Hindi using Google Translate API directly
    """
    try:
        if not text or not text.strip():
            return text

        # Clean and prepare the text
        text = text.strip()

        # Use Google Translate API directly (most reliable)
        base_url = "https://translate.googleapis.com/translate_a/single"
        params = {
            'client': 'gtx',
            'sl': 'en',  # source language: English
            'tl': 'hi',  # target language: Hindi
            'dt': 't',   # return translated text
            'q': text    # the text to translate
        }

        # Make the request
        response = requests.get(base_url, params=params, timeout=15)

        if response.status_code == 200:
            result = response.json()
            if result and len(result) > 0 and len(result[0]) > 0:
                translated = result[0][0][0]
                try:
                    print(f"Translated: '{text}' -> '{translated}'")
                except UnicodeEncodeError:
                    print(f"Translated: '{text}' -> [Hindi text - {len(translated)} characters]")
                return translated
            else:
                print("Translation API returned empty result")
                return text
        else:
            print(f"Translation API error: {response.status_code}")
            return text

    except requests.exceptions.RequestException as e:
        print(f"Network error during translation: {e}")
        return text
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def translate_text_fallback(text):
    """
    Alternative translation method (keeps original functionality)
    """
    return text

def translate_text_fallback(text):
    """
    Alternative translation method using different service
    """
    try:
        # This could use other translation services
        # For now, return the original text
        return text
    except Exception as e:
        print(f"Fallback translation error: {e}")
        return text