
# Kümmert sich um das Speichern und Laden des Punktestands
# in einer JSON-Datei (scores.json).


import json
import os

SCORE_FILE = "scores.json"  # Name der Datei für die Punktestände


def load_scores():
    """
    Lädt die Punktestände aus der JSON-Datei.
    Gibt ein Dictionary {name: punkte} zurück.
    """
    if not os.path.exists(SCORE_FILE):
        return {}

    try:
        with open(SCORE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # Falls die Datei beschädigt ist oder nicht gelesen werden kann
        return {}


def save_scores(scores):
    """
    Speichert das Dictionary scores in der JSON-Datei.
    """
    with open(SCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)
