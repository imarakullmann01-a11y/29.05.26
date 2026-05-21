import tkinter as tk
from tkinter import messagebox
from quiz_engine import QuizSession
from scoring import load_scores

# ── Farbpalette (Folie 8 — bg= und fg= für Widgets) ─────────────────────
FARBE_BG       = "#f0f4f8"
FARBE_KOPF_BG  = "#1e3a5f"
FARBE_KOPF_FG  = "white"
FARBE_BLAU     = "#1976D2"
FARBE_GRAU     = "#546e7a"
FARBE_ROT      = "#c62828"
FARBE_FG       = "white"
FARBE_RICHTIG  = "#2e7d32"
FARBE_FALSCH   = "#c62828"


class QuizApp:
    """
    Hauptklasse der GUI.
    Struktur aus Folie 18 (Klasse kapselt GUI-Logik).
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Python-Quiz")
        self.root.geometry("560x700")
        self.root.config(bg=FARBE_BG)
        self.session = None
        self._is_demo = False
        self._build_ui()
        self._zeige_hauptmenu()

    # ── 1. Widgets einmalig aufbauen ─────────────────────────────────────
    def _build_ui(self):
        """
        Erstellt alle Widgets einmal.
        Styling mit bg= / fg= / font= aus Folie 8.
        Layout mit pack() aus Folie 57–61.
        """
        # Kopfzeile (Folie 8 — bg= / fg=)
        self.lbl_titel = tk.Label(
            self.root,
            text="Python-Quiz",
            font=("Helvetica", 20, "bold"),
            bg=FARBE_KOPF_BG,
            fg=FARBE_KOPF_FG,
            pady=15
        )
        self.lbl_titel.pack(fill="x")

        # Status-Label (Folie 10)
        self.lbl_status = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 10, "italic"),
            bg=FARBE_BG,
            fg=FARBE_GRAU
        )
        self.lbl_status.pack(pady=4)

        # Haupttext / Frage (Folie 10 / 16)
        self.lbl_frage = tk.Label(
            self.root,
            text="",
            wraplength=500,
            justify="left",
            font=("Helvetica", 11),
            bg=FARBE_BG
        )
        self.lbl_frage.pack(padx=25, pady=8)

        # Eingabe-Label
        self.lbl_eingabe = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 10),
            bg=FARBE_BG
        )
        self.lbl_eingabe.pack()

        # Entry + StringVar (Folie 21 / 66–67)
        self.eingabe_var = tk.StringVar()
        self.entry = tk.Entry(
            self.root,
            textvariable=self.eingabe_var,
            width=42,
            font=("Helvetica", 11)
        )
        self.entry.pack(pady=4)

        # 4 Radiobuttons (Folie 40–43)
        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.root,
                text="",
                variable=self.radio_var,
                value=i,
                anchor="w",
                width=50,
                bg=FARBE_BG,
                font=("Helvetica", 10)
            )
            rb.pack(anchor="w", padx=60)
            self.radio_buttons.append(rb)

        # Feedback-Label (Folie 8 — fg= für Farbe)
        self.lbl_feedback = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 10, "bold"),
            bg=FARBE_BG
        )
        self.lbl_feedback.pack(pady=4)

        # Score-Label
        self.lbl_score = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 10),
            bg=FARBE_BG
        )
        self.lbl_score.pack()

        # 5 Buttons (Folie 15–18)
        self.btn1 = tk.Button(
            self.root, text="", width=34,
            font=("Helvetica", 10, "bold"),
            bg=FARBE_BLAU, fg=FARBE_FG,
            command=self._dummy
        )
        self.btn1.pack(pady=5, anchor="w", fill="x", padx=20)

        self.btn2 = tk.Button(
            self.root, text="", width=34,
            font=("Helvetica", 10),
            bg=FARBE_GRAU, fg=FARBE_FG,
            command=self._dummy
        )
        self.btn2.pack(pady=2, anchor="w", fill="x", padx=20)

        self.btn3 = tk.Button(
            self.root, text="", width=34,
            font=("Helvetica", 10),
            bg=FARBE_GRAU, fg=FARBE_FG,
            command=self._dummy
        )
        self.btn3.pack(pady=2, anchor="w", fill="x", padx=20)

        self.btn4 = tk.Button(
            self.root, text="", width=34,
            font=("Helvetica", 10),
            bg=FARBE_GRAU, fg=FARBE_FG,
            command=self._dummy
        )
        self.btn4.pack(pady=2, anchor="w", fill="x", padx=20)

        self.btn5 = tk.Button(
            self.root, text="", width=34,
            font=("Helvetica", 10, "bold"),
            bg=FARBE_ROT, fg=FARBE_FG,
            command=self._dummy
        )
        self.btn5.pack(pady=5, anchor="w", fill="x", padx=20)

    def _dummy(self):
        pass

    def _buttons_leeren(self, von=1, bis=5):
        """Setzt gewählte Buttons auf leer."""
        alle = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5]
        for btn in alle[von - 1:bis]:
            btn.config(text="", command=self._dummy)

    def _radiobuttons_leeren(self):
        """Leert alle Radiobuttons — text='' macht sie unsichtbar."""
        for rb in self.radio_buttons:
            rb.config(text="", command=self._dummy)

    # ── 2. Hauptmenü ─────────────────────────────────────────────────────
    def _zeige_hauptmenu(self):
        """
        Konfiguriert alle Widgets für das Hauptmenü.
        .config() aus Folie 16.
        """
        self.session = None
        self._is_demo = False

        self.lbl_status.config(text="Hauptmenü")
        self.lbl_frage.config(
            text="Willkommen beim Python-Quiz!\nBitte wähle eine Option:"
        )
        self.lbl_eingabe.config(text="")
        self.eingabe_var.set("")
        self._radiobuttons_leeren()
        self.lbl_feedback.config(text="", fg="black")
        self.lbl_score.config(text="")

        # 5 Menüpunkte (Folie 16 — .config())
        self.btn1.config(
            text="1)  Komplettes Quiz  (leicht → mittel → schwer)",
            bg=FARBE_BLAU,
            command=self._zeige_namenseingabe
        )
        self.btn2.config(
            text="2)  Level-Demo  (einzelnes Level auswählen)",
            bg=FARBE_GRAU,
            command=self._zeige_level_demo
        )
        self.btn3.config(
            text="3)  Punktestände anzeigen",
            bg=FARBE_GRAU,
            command=self._zeige_scores
        )
        self.btn4.config(
            text="4)  Regeln anzeigen",
            bg=FARBE_GRAU,
            command=self._zeige_regeln
        )
        self.btn5.config(
            text="5)  Beenden",
            bg=FARBE_ROT,
            command=self.root.quit
        )

    # ── 3. Namenseingabe ─────────────────────────────────────────────────
    def _zeige_namenseingabe(self):
        self.lbl_status.config(text="Komplettes Quiz")
        self.lbl_frage.config(text="Bitte gib deinen Namen ein:")
        self.lbl_eingabe.config(text="Dein Name:")
        self.eingabe_var.set("")
        self._radiobuttons_leeren()
        self.lbl_feedback.config(text="", fg="black")
        self.lbl_score.config(text="")

        self.btn1.config(
            text="Quiz starten",
            bg=FARBE_BLAU,
            command=self._starte_quiz
        )
        self.btn2.config(
            text="Zurück zum Hauptmenü",
            bg=FARBE_GRAU,
            command=self._zeige_hauptmenu
        )
        self._buttons_leeren(von=3, bis=5)

    # ── 4. Quiz starten ──────────────────────────────────────────────────
    def _starte_quiz(self):
        """
        Liest Namen aus Entry (.get() — Folie 24).
        Fehlerrückmeldung per messagebox (Anforderung 5 / Folie 72).
        """
        name = self.eingabe_var.get().strip()

        # Anforderung 5: Fehlerrückmeldung bei ungültiger Eingabe
        if not name:
            messagebox.showerror(
                "Fehler",
                "Bitte gib einen Namen ein!"
            )
            return

        self._is_demo = False
        self.session = QuizSession(name=name)
        self._zeige_frage()

    # ── 5. Level-Demo ────────────────────────────────────────────────────
    def _zeige_level_demo(self):
    
        #Nutzt Radiobuttons für die Level-Auswahl (Folie 40–43).
        #command=lambda gibt Feedback über das gewählte Level (Folie 43).
    
        self.lbl_status.config(text="Level-Demo")
        self.lbl_frage.config(
            text="Gib deinen Namen ein und wähle ein Level:"
        )
        self.lbl_eingabe.config(text="Dein Name:")
        self.eingabe_var.set("")
        self.lbl_feedback.config(text="", fg="black")

    # Radiobuttons für Level-Auswahl
    # command=lambda aktualisiert lbl_score als Rückmeldung (Folie 43)
        self.radio_var.set(0)
        self.lbl_score.config(text="Gewähltes Level: Leicht")

        for i, level in enumerate(["Leicht", "Mittel", "Schwer"]):
            self.radio_buttons[i].config(
                text=level,
                command=lambda l=level: self.lbl_score.config(
                    text=f"Gewähltes Level: {l}"
            )
        )
        self.radio_buttons[3].config(text="", command=self._dummy)

        self.btn1.config(
            text="Level starten",
            bg=FARBE_BLAU,
            command=self._starte_demo
    )
        self.btn2.config(
            text="Zurück zum Hauptmenü",
            bg=FARBE_GRAU,
            command=self._zeige_hauptmenu
    )
        self._buttons_leeren(von=3, bis=5)
      

    def _starte_demo(self):
        """Startet das gewählte Demo-Level."""
        name = self.eingabe_var.get().strip()

        # Anforderung 5: Fehlerrückmeldung
        if not name:
            messagebox.showerror(
                "Fehler",
                "Bitte gib einen Namen ein!"
            )
            return

        levels = ["leicht", "mittel", "schwer"]
        level_key = levels[self.radio_var.get()]
        self._is_demo = True
        self.session = QuizSession(name=name, start_level=level_key)
        self._zeige_frage()

    # ── 6. Frage anzeigen ────────────────────────────────────────────────
    def _zeige_frage(self):
        """
        Aktualisiert Widgets per .config() (Folie 16).
        Radiobuttons + lambda → schreiben Antwort ins Entry (Folie 43/66).
        """
        if self.session.quiz_beendet:
            self._zeige_quiz_ende()
            return

        frage = self.session.aktuelle_frage
        nr, gesamt = self.session.frage_nummer

        self.lbl_status.config(
            text=f"Level: {self.session.aktuelles_level.upper()} "
                 f"| Frage {nr}/{gesamt}"
        )
        self.lbl_frage.config(text=frage.text)
        self.lbl_feedback.config(text="", fg="black")
        self.lbl_score.config(
            text=f"Aktuelle Punkte: {self.session.aktuelle_punkte}"
        )
        self.eingabe_var.set("")

        # Fragetyp: Multiple Choice
        if frage.qtype == "mc":
            self.lbl_eingabe.config(text="Wähle eine Antwort:")
            for i, option in enumerate(frage.auswahl):
                label = chr(ord("a") + i)
                # Klick → schreibt Buchstaben ins Entry
                # lambda aus Folie 43 / StringVar.set() aus Folie 66
                self.radio_buttons[i].config(
                    text=f"{label})  {option}",
                    command=lambda l=label: self.eingabe_var.set(l)
                )
            self.radio_var.set(-1)

        # Fragetyp: Ja/Nein
        elif frage.qtype == "yn":
            self.lbl_eingabe.config(text="Wähle eine Antwort:")
            self.radio_buttons[0].config(
                text="Ja",
                command=lambda: self.eingabe_var.set("ja")
            )
            self.radio_buttons[1].config(
                text="Nein",
                command=lambda: self.eingabe_var.set("nein")
            )
            for rb in self.radio_buttons[2:]:
                rb.config(text="", command=self._dummy)
            self.radio_var.set(-1)

        # Fragetyp: Text oder Code
        elif frage.qtype in ("text", "code"):
            self.lbl_eingabe.config(text="Deine Antwort:")
            self._radiobuttons_leeren()

        # Buttons für Quiz-Modus
        self.btn1.config(
            text="Antwort bestätigen",
            bg=FARBE_BLAU,
            command=self._antwort_pruefen
        )
        self.btn2.config(
            text="Quiz abbrechen",
            bg=FARBE_ROT,
            command=self._abbrechen
        )
        self._buttons_leeren(von=3, bis=5)

    # ── 7. Antwort prüfen ────────────────────────────────────────────────
    def _antwort_pruefen(self):
        """
        Prüft Antwort via QuizSession.
        Feedback per .config() + fg= (Folie 8/16).
        Fehlerrückmeldung bei leerer Eingabe (Anforderung 5).
        """
        antwort = self.eingabe_var.get().strip()

        # Anforderung 5: Fehlerrückmeldung
        if not antwort:
            messagebox.showwarning(
                "Keine Eingabe",
                "Bitte gib eine Antwort ein oder wähle eine Option!"
            )
            return

        ist_richtig, _, feedback = self.session.antwort_geben(antwort)

        # Feedback per .config() + fg= Folie 8
        if ist_richtig:
            self.lbl_feedback.config(
                text=f"Richtig!  {feedback}",
                fg=FARBE_RICHTIG
            )
        else:
            self.lbl_feedback.config(
                text=f"Falsch!  {feedback}",
                fg=FARBE_FALSCH
            )

        self.lbl_score.config(
            text=f"Aktuelle Punkte: {self.session.aktuelle_punkte}"
        )

        if self.session.level_fertig:
            self.btn1.config(
                text="Level abschliessen",
                command=self._level_abschliessen
            )
        else:
            self.btn1.config(
                text="Nächste Frage",
                command=self._zeige_frage
            )

    # ── 8. Level abschliessen ────────────────────────────────────────────
    def _level_abschliessen(self):
        """
        Zeigt Ergebnis-Dialog (Anforderung 3 — messagebox Folie 72).
        Im Demo-Modus: zurück zum Hauptmenü.
        """
        bestanden, punkte = self.session.level_abschliessen()

        if bestanden:
            messagebox.showinfo(
                "Level bestanden!",
                f"Glückwunsch! Du hast das Level bestanden.\n"
                f"Punkte in diesem Level: {punkte}"
            )
        else:
            messagebox.showwarning(
                "Nicht bestanden",
                f"Zu viele Fehler. Das Level wird wiederholt.\n"
                f"Punkte in diesem Level: {punkte}"
            )

        # Demo: nur ein Level — zurück zum Hauptmenü
        if self._is_demo:
            messagebox.showinfo(
                "Demo beendet",
                f"Der Demo-Modus ist abgeschlossen.\n"
                f"Punkte werden nicht gespeichert."
            )
            self._zeige_hauptmenu()
            return

        self._zeige_frage()

    # ── 9. Quiz-Ende ─────────────────────────────────────────────────────
    def _zeige_quiz_ende(self):
        """
        Abschluss-Bildschirm mit Dialog (Folie 72 — messagebox).
        """
        self.session.speichern()

        self.lbl_status.config(text="Quiz abgeschlossen!")
        self.lbl_frage.config(
            text=f"Herzlichen Glückwunsch, {self.session.name}!\n"
                 f"Du hast alle Level erfolgreich abgeschlossen."
        )
        self.lbl_eingabe.config(text="")
        self.eingabe_var.set("")
        self._radiobuttons_leeren()
        self.lbl_feedback.config(text="", fg="black")
        self.lbl_score.config(
            text=f"Gesamtpunkte: {self.session.gesamt_punkte}"
        )

        # Abschluss-Dialog (Anforderung 3)
        messagebox.showinfo(
            "Quiz abgeschlossen!",
            f"Punktestand gespeichert:\n"
            f"{self.session.name}  →  {self.session.gesamt_punkte} Punkte"
        )

        self.btn1.config(
            text="Nochmal spielen",
            bg=FARBE_BLAU,
            command=self._zeige_hauptmenu
        )
        self.btn2.config(
            text="Punktestände anzeigen",
            bg=FARBE_GRAU,
            command=self._zeige_scores
        )
        self.btn3.config(
            text="Beenden",
            bg=FARBE_ROT,
            command=self.root.quit
        )
        self._buttons_leeren(von=4, bis=5)

    # ── 10. Punktestände ─────────────────────────────────────────────────
    def _zeige_scores(self):
        """
        Punktestände per messagebox anzeigen (Folie 72).
        """
        scores = load_scores()

        if not scores:
            messagebox.showinfo(
                "Punktestände",
                "Noch keine Punktestände gespeichert."
            )
            return

        sortiert = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        text = "Punktestände:\n\n"
        for rang, (name, punkte) in enumerate(sortiert, start=1):
            text += f"{rang}.  {name}:  {punkte} Punkte\n"

        messagebox.showinfo("Punktestände", text)

    # ── 11. Regeln ───────────────────────────────────────────────────────
    def _zeige_regeln(self):
        """
        Regeln per messagebox anzeigen (Folie 72).
        """
        messagebox.showinfo(
            "Regeln",
            "Das Quiz besteht aus drei Levels: leicht, mittel, schwer.\n\n"
            "Fragetypen:\n"
            "  • Multiple Choice (a, b, c, d)\n"
            "  • Ja/Nein\n"
            "  • Kurze Textantwort\n"
            "  • Eine Zeile Python-Code\n\n"
            "Ein Level gilt als bestanden, wenn mehr als die Hälfte\n"
            "der Fragen richtig beantwortet werden.\n\n"
            "Am Ende wird dein Punktestand gespeichert."
        )

    # ── 12. Quiz abbrechen ───────────────────────────────────────────────
    def _abbrechen(self):
        """
        Bestätigungsdialog (Anforderung 3 — askyesno Folie 72).
        """
        if messagebox.askyesno(
            "Quiz abbrechen",
            "Möchtest du das Quiz wirklich abbrechen?"
        ):
            self._zeige_hauptmenu()


# ── Einstiegspunkt ───────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()