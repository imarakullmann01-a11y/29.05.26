import random
from questions import create_fragen
from scoring import load_scores, save_scores


class QuizSession:
    """
    Verwaltet den kompletten Spielzustand.
    Kein print, kein input – nur Logik.
    """

    LEVELS = ["leicht", "mittel", "schwer"]

    def __init__(self, name: str = "Demo", start_level: str = "leicht"):
        self.name = name
        self.alle_fragen = create_fragen()
        self.level_index = self.LEVELS.index(start_level)
        self.gesamt_punkte = 0
        self._lade_level()

    # ── internes Setup ──────────────────────────────────────────────
    def _lade_level(self):
        fragen = self.alle_fragen[self.aktuelles_level][:]
        random.shuffle(fragen)
        self._fragen = fragen
        self._frage_index = 0
        self.level_punkte = 0
        self.richtige = 0

    # ── Properties ─────────────────────────────────────────────────
    @property
    def aktuelles_level(self) -> str:
        return self.LEVELS[self.level_index]

    @property
    def aktuelle_punkte(self) -> int:
        """Gesamt + laufende Levelpunkte."""
        return self.gesamt_punkte + self.level_punkte

    @property
    def aktuelle_frage(self):
        if self._frage_index < len(self._fragen):
            return self._fragen[self._frage_index]
        return None

    @property
    def level_fertig(self) -> bool:
        return self._frage_index >= len(self._fragen)

    @property
    def level_bestanden(self) -> bool:
        return self.richtige > len(self._fragen) / 2

    @property
    def quiz_beendet(self) -> bool:
        return self.level_index >= len(self.LEVELS)

    @property
    def frage_nummer(self) -> tuple[int, int]:
        """Gibt (aktuelle_nr, gesamt) zurück – z.B. (3, 10)."""
        return self._frage_index + 1, len(self._fragen)

    # ── Aktionen ────────────────────────────────────────────────────
    def antwort_geben(self, antwort: str) -> tuple[bool, int, str]:
        """Wertet die Antwort aus und aktualisiert den Zustand."""
        frage = self.aktuelle_frage
        ist_richtig, punkte, feedback = frage.check_answer(antwort)
        if ist_richtig:
            self.richtige += 1
        self.level_punkte += punkte
        self._frage_index += 1
        return ist_richtig, punkte, feedback

    def level_abschliessen(self) -> tuple[bool, int]:
        """
        Schließt das aktuelle Level ab.
        Gibt (bestanden, punkte_dieses_levels) zurück.
        Bestanden → nächstes Level laden.
        Nicht bestanden → Level wiederholen.
        """
        punkte = self.level_punkte
        bestanden = self.level_bestanden
        if bestanden:
            self.gesamt_punkte += punkte
            self.level_index += 1
            if not self.quiz_beendet:
                self._lade_level()
        else:
            self._lade_level()
        return bestanden, punkte

    def neustart(self):
        """Setzt das Quiz komplett zurück."""
        self.level_index = 0
        self.gesamt_punkte = 0
        self._lade_level()

    def speichern(self):
        """Speichert den Punktestand des Spielers."""
        scores = load_scores()
        scores[self.name] = self.gesamt_punkte
        save_scores(scores)