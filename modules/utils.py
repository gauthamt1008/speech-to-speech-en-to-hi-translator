import os
import json
from datetime import datetime

def save_history(english_text, hindi_text):
    """
    Save translation to history file
    """
    try:
        # Get the history file path relative to the web app
        current_dir = os.path.dirname(os.path.abspath(__file__))
        history_file = os.path.join(current_dir, '..', 'history.json')

        # Load existing history
        history = []
        if os.path.exists(history_file):
            try:
                with open(history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            except:
                history = []

        # Add new entry
        entry = {
            'timestamp': datetime.now().isoformat(),
            'english': english_text,
            'hindi': hindi_text
        }
        history.append(entry)

        # Keep only last 100 entries
        if len(history) > 100:
            history = history[-100:]

        # Save to file
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

        print(f"History saved: {english_text} -> {hindi_text}")

    except Exception as e:
        print(f"Error saving history: {e}")

def get_history(limit=50):
    """
    Get translation history
    """
    try:
        # Get the history file path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        history_file = os.path.join(current_dir, '..', 'history.json')

        if not os.path.exists(history_file):
            return []

        with open(history_file, 'r', encoding='utf-8') as f:
            history = json.load(f)

        # Return last 'limit' entries in reverse order (newest first)
        return history[-limit:][::-1]

    except Exception as e:
        print(f"Error loading history: {e}")
        return []

def clear_history():
    """
    Clear all translation history
    """
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        history_file = os.path.join(current_dir, '..', 'history.json')

        if os.path.exists(history_file):
            os.remove(history_file)

        print("History cleared")
        return True

    except Exception as e:
        print(f"Error clearing history: {e}")
        return False

def get_stats():
    """
    Get usage statistics
    """
    try:
        history = get_history(1000)  # Get all history

        stats = {
            'total_translations': len(history),
            'last_translation': history[0] if history else None,
            'average_text_length': sum(len(entry.get('english', '')) for entry in history) / len(history) if history else 0
        }

        return stats
    except Exception as e:
        print(f"Error getting stats: {e}")
        return {'total_translations': 0}

    except Exception as e:
        print(f"Error getting stats: {e}")
        return {'total_translations': 0}