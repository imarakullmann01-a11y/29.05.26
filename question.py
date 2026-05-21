import re


class Question:
    def __init__(self, text, qtype, punkte, auswahl=None, richtig_index=None, richtig_text=None):
        """
        text          : Fragetext (str)
        qtype         : Fragetyp ("mc", "yn", "text", "code")
        punkte        : Punkte für richtige Antwort (int)
        auswahl       : Liste der Antwortmöglichkeiten (nur bei "mc")
        richtig_index : Index der richtigen Antwort (nur bei "mc")
        richtig_text  : richtige Antwort als Text (bei "yn", "text", "code")
        """
        self.text = text
        self.qtype = qtype
        self.punkte = punkte
        self.auswahl = auswahl or []
        self.richtig_index = richtig_index
        self.richtig_text = richtig_text

    def check_answer(self, antwort: str) -> tuple[bool, int, str]:
        """
        Reine Logik – kein print, kein input.
        Gibt (ist_richtig, punkte, feedback_text) zurück.
        """
        antwort = antwort.strip()

        if self.qtype == "mc":
            chosen = ord(antwort.lower()[0]) - ord("a")
            if chosen == self.richtig_index:
                return True, self.punkte, "Richtig!"
            correct_letter = chr(ord("a") + self.richtig_index)
            return False, 0, f"Falsch! Richtige Antwort: {correct_letter}) {self.auswahl[self.richtig_index]}"

        elif self.qtype == "yn":
            normalized = "ja" if antwort.lower().startswith("j") else "nein"
            if normalized == (self.richtig_text or "").strip().lower():
                return True, self.punkte, "Richtig!"
            return False, 0, f"Falsch! Richtige Antwort: {self.richtig_text}"

        elif self.qtype == "text":
            if antwort.lower() == (self.richtig_text or "").strip().lower():
                return True, self.punkte, "Richtig!"
            return False, 0, f"Falsch! Richtige Antwort: {self.richtig_text}"

        elif self.qtype == "code":
            normalize = lambda s: re.sub(r"\s+", "", s).lower()
            if normalize(antwort) == normalize(self.richtig_text or ""):
                return True, self.punkte, "Richtig!"
            return False, 0, f"Falsch! Eine mögliche Lösung: {self.richtig_text}"

        return False, 0, "Unbekannter Fragetyp."