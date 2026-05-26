import tkinter as tk
from tkinter import messagebox
from quiz_engine import QuizSession
from scoring import load_scores

# ── Farbpalette (Folie 8 — bg= / fg=) ───────────────────────────────────
FARBE_BG      = "#EFF6FF"   # Sehr helles Blau (Hintergrund)
FARBE_KARTE   = "#FFFFFF"   # Karte
FARBE_KOPF_BG = "#1D4ED8"   # Dunkelblau (Kopfzeile)
FARBE_KOPF_FG = "#FFFFFF"
FARBE_TEXT    = "#1E3A5F"   # Dunkles Blau (Text)
FARBE_SUBTEXT = "#3B82F6"   # Mittleres Blau
                                                                                                                                                                                                                                                                                                                                      
FARBE_BLAU    = "#60A5FA"   # Pastellblau (Hauptbutton)
FARBE_BLAU_H  = "#3B82F6"   # Hover
FARBE_GRAU    = "#93C5FD"   # Helles Pastellblau (Sekundär)
FARBE_GRAU_H  = "#60A5FA"   # Hover
FARBE_ROT     = "#2563EB"   # Kräftiges Blau (Beenden)
FARBE_ROT_H   = "#1D4ED8"   # Hover
FARBE_FG      = "#FFFFFF"

FARBE_RICHTIG = "#16A34A"
FARBE_FALSCH  = "#DC2626"
 

class QuizApp:
    """
    Hauptklasse der GUI.
    Struktur aus Folie 18 (Klasse kapselt GUI-Logik).
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Python-Quiz")
        self.root.geometry("580x720")
        self.root.config(bg=FARBE_BG)
        self.session = None
        self._is_demo = False
        self._build_ui()
        self._zeige_hauptmenu()

    # ── Hover-Hilfsfunktion (bind() — Folie 42) ─────────────────────────
    def _hover(self, btn, normal, hell):
        btn.bind("<Enter>", lambda e: btn.config(bg=hell))
        btn.bind("<Leave>", lambda e: btn.config(bg=normal))

    # ── Button-Hilfsmethoden ─────────────────────────────────────────────
    def _btn_blau(self, btn, text, command):
        btn.config(text=text, command=command,
                   bg=FARBE_BLAU, fg=FARBE_FG,
                   pady=8, activebackground=FARBE_BLAU_H)
        self._hover(btn, FARBE_BLAU, FARBE_BLAU_H)

    def _btn_grau(self, btn, text, command):
        btn.config(text=text, command=command,
                   bg=FARBE_GRAU, fg=FARBE_FG,
                   pady=8, activebackground=FARBE_GRAU_H)
        self._hover(btn, FARBE_GRAU, FARBE_GRAU_H)

    def _btn_rot(self, btn, text, command):
        btn.config(text=text, command=command,
                   bg=FARBE_ROT, fg=FARBE_FG,
                   pady=8, activebackground=FARBE_ROT_H)
        self._hover(btn, FARBE_ROT, FARBE_ROT_H)

    # ── Widgets einmalig aufbauen ────────────────────────────────────────
    def _build_ui(self):
        """
        Layout: pack() — Folie 57–61.
        Farben: bg= / fg= — Folie 8.
        Flat-Buttons: relief= / bd= — Folie 62.
        Hover: bind() — Folie 42.
        Karte: Frame — Folie 18.
        """

        # Kopfzeile
        self.lbl_titel = tk.Label(
            self.root,
            text="Python-Quiz",
            font=("Helvetica", 22, "bold"),
            bg=FARBE_KOPF_BG,
            fg=FARBE_KOPF_FG,
            pady=18
        )
        self.lbl_titel.pack(fill="x")

        self.lbl_untertitel = tk.Label(
            self.root,
            text="Teste dein Python-Wissen",
            font=("Helvetica", 10),
            bg=FARBE_KOPF_BG,
            fg="#010408",
            pady=4
        )
        self.lbl_untertitel.pack(fill="x")

        # Status-Streifen (volle Breite)
        self.lbl_status = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 10, "bold"),
            bg="#DB2777",
            fg="white",
            pady=6
        )
        self.lbl_status.pack(fill="x")

        # Karte (Frame — Folie 18, expand=YES — Folie 61)
        self.karte = tk.Frame(
            self.root,
            bg=FARBE_KARTE,
            padx=30,
            pady=20
        )
        self.karte.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # Trennlinie
        tk.Label(
            self.karte,
            text="",
            bg=FARBE_KARTE,
            height=1
        ).pack(fill="x", pady=(0, 12))

        # Fragetext (Folie 10 / 16)
        self.lbl_frage = tk.Label(
            self.karte,
            text="",
            wraplength=490,
            justify="left",
            font=("Helvetica", 12),
            bg=FARBE_KARTE,
            fg=FARBE_TEXT
        )
        self.lbl_frage.pack(anchor="w", pady=(0, 12))

        # Eingabe-Label
        self.lbl_eingabe = tk.Label(
            self.karte,
            text="",
            font=("Helvetica", 10, "bold"),
            bg=FARBE_KARTE,
            fg=FARBE_TEXT
        )
        self.lbl_eingabe.pack(anchor="w")

        # Entry + StringVar (Folie 21 / 66–67)
        self.eingabe_var = tk.StringVar()
        self.entry = tk.Entry(
            self.karte,
            textvariable=self.eingabe_var,
            width=44,
            font=("Helvetica", 11),
            relief="flat",
            bd=2,
            bg="#F8FAFC"
        )
        self.entry.pack(anchor="w", pady=(4, 12))

        # 4 Radiobuttons (Folie 40–43)
        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.karte,
                text="",
                variable=self.radio_var,
                value=i,
                anchor="w",
                font=("Helvetica", 10),
                bg=FARBE_KARTE,
                fg=FARBE_TEXT,
                selectcolor=FARBE_KARTE,
                activebackground=FARBE_KARTE
            )
            rb.pack(anchor="w", padx=10, pady=2)
            rb.pack_forget()  
            self.radio_buttons.append(rb)


        # Feedback-Label (Folie 8 — fg= für Farbe)
        self.lbl_feedback = tk.Label(
            self.karte,
            text="",
            font=("Helvetica", 10, "bold"),
            bg=FARBE_KARTE
        )
        self.lbl_feedback.pack(anchor="w", pady=(8, 2))

        # Score-Label
        self.lbl_score = tk.Label(
            self.karte,
            text="",
            font=("Helvetica", 10),
            bg=FARBE_KARTE,
            fg=FARBE_SUBTEXT
        )
        self.lbl_score.pack(anchor="w", pady=(0, 12))

        # Zweite Trennlinie
        tk.Label(
            self.karte,
            text="",
            bg=FARBE_KARTE,
            height=1
        ).pack(fill="x", pady=(0, 12))

        # 5 Buttons (Folie 15–18, relief= Folie 62)
        btn_basis = dict(
            font=("Helvetica", 10, "bold"),
            fg=FARBE_FG,
            relief="flat",
            bd=0,
            pady=8,
            cursor="hand2"
        )

        self.btn1 = tk.Button(self.karte, **btn_basis, bg=FARBE_BLAU)
        self.btn1.pack(fill="x", pady=3)

        self.btn2 = tk.Button(self.karte, **btn_basis, bg=FARBE_GRAU)
        self.btn2.pack(fill="x", pady=3)

        self.btn3 = tk.Button(self.karte, **btn_basis, bg=FARBE_GRAU)
        self.btn3.pack(fill="x", pady=3)

        self.btn4 = tk.Button(self.karte, **btn_basis, bg=FARBE_GRAU)
        self.btn4.pack(fill="x", pady=3)

        self.btn5 = tk.Button(self.karte, **btn_basis, bg=FARBE_ROT)
        self.btn5.pack(fill="x", pady=3)

    def _dummy(self):
        pass

    def _buttons_leeren(self, von=1, bis=5):
        """Macht Buttons unsichtbar (weiß auf weiß, kein Hover)."""
        alle = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5]
        for btn in alle[von - 1:bis]:
            btn.config(
                text="", command=self._dummy,
                bg=FARBE_KARTE, fg=FARBE_KARTE,
                pady=1, activebackground=FARBE_KARTE
            )
            btn.bind("<Enter>", lambda e: None)
            btn.bind("<Leave>", lambda e: None)

    def _radiobuttons_leeren(self):
        for rb in self.radio_buttons:
            rb.pack_forget()

# ── Hauptmenü (Seite 1: Namenseingabe) ──────────────────────────────
    def _zeige_hauptmenu(self):
        self.session = None
        self._is_demo = False
        self.lbl_status.config(text="Startseite")
        self.lbl_frage.config(text="Willkommen!")
        self.lbl_eingabe.config(text="")
        self.eingabe_var.set("")
        self.entry.config(fg="grey")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "Name eingeben")
        self.entry.bind("<FocusIn>", self._clear_placeholder)
        self.entry.bind("<FocusOut>", self._set_placeholder)
        self.entry.pack(anchor="w", pady=(4, 12))
        self._radiobuttons_leeren()
        self.lbl_feedback.config(text="", fg="black")
        self.lbl_score.config(text="")

        self._btn_blau(self.btn1, "Weiter →", self._name_bestaetigen)
        self._buttons_leeren(von=2, bis=5)

    def _clear_placeholder(self, event):
        if self.entry.get() == "Name eingeben":
            self.entry.delete(0, tk.END)
            self.entry.config(fg=FARBE_TEXT)

    def _set_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, "Name eingeben")
            self.entry.config(fg="grey")

    def _name_bestaetigen(self):
        name = self.eingabe_var.get().strip()
        if not name or name == "Name eingeben":
            messagebox.showerror("Fehler", "Bitte gib deinen Namen ein!")
            return
        self._zeige_optionen(name)

    # ── Hauptmenü (Seite 2: Optionen) ───────────────────────────────────
    def _zeige_optionen(self, name):
        self.lbl_frage.config(text=f"Willkommen, {name}!")
        self.lbl_eingabe.config(text="")
        self.entry.pack_forget()
        self.lbl_score.config(text="Wähle eine Option um zu starten:")
        self.lbl_feedback.config(text="", fg="black")

        self._btn_blau(self.btn1, "1)  Komplettes Quiz  (leicht → mittel → schwer)", self._zeige_namenseingabe)
        self._btn_grau(self.btn2, "2)  Level-Demo  (einzelnes Level auswählen)",      self._zeige_level_demo)
        self._btn_grau(self.btn3, "3)  Punktestände anzeigen",                         self._zeige_scores)
        self._btn_grau(self.btn4, "4)  Regeln anzeigen",                               self._zeige_regeln)
        self._btn_rot (self.btn5, "5)  Beenden",                                       self.root.quit)

        for btn in [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5]:
            btn.pack_forget()
            btn.pack(anchor="center", pady=3, ipadx=80)
            btn.config(width=40)

    # ── Namenseingabe ────────────────────────────────────────────────────
    def _zeige_namenseingabe(self):
        name = self.lbl_frage.cget("text").replace("Willkommen, ", "").replace("!", "")
        self._is_demo = False
        self.session = QuizSession(name=name)
        self._zeige_frage()

        self._btn_blau(self.btn1, "Quiz starten",       self._starte_quiz)
        self._btn_grau(self.btn2, "Zurück",             self._zeige_hauptmenu)
        self._buttons_leeren(von=3, bis=5)

    # ── Quiz starten ─────────────────────────────────────────────────────
    def _starte_quiz(self):
        name = self.eingabe_var.get().strip()
        if not name:
            messagebox.showerror("Fehler", "Bitte gib einen Namen ein!")
            return
        self._is_demo = False
        self.session = QuizSession(name=name)
        self._zeige_frage()

    # ── Level-Demo ───────────────────────────────────────────────────────
    def _zeige_level_demo(self):
        self.lbl_status.config(text="  Level-Demo")
        self.lbl_frage.config(
            text="Gib deinen Namen ein und wähle ein Level:"
        )
        self.lbl_eingabe.config(text="Dein Name:")
        self.eingabe_var.set("")
        self.lbl_feedback.config(text="", fg="black")

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

        self._btn_blau(self.btn1, "Level starten", self._starte_demo)
        self._btn_grau(self.btn2, "Zurück",        self._zeige_hauptmenu)
        self._buttons_leeren(von=3, bis=5)

    def _starte_demo(self):
        name = self.lbl_frage.cget("text").replace("Willkommen, ", "").replace("!", "")
        levels = ["leicht", "mittel", "schwer"]
        level_key = levels[self.radio_var.get()]
        self._is_demo = True
        self.session = QuizSession(name=name, start_level=level_key)
        self._zeige_frage()

    # ── Frage anzeigen ───────────────────────────────────────────────────
    def _zeige_frage(self):
        if self.session.quiz_beendet:
            self._zeige_quiz_ende()
            return

        frage = self.session.aktuelle_frage
        for rb in self.radio_buttons:          # ← neu
            rb.pack(anchor="w", padx=10, pady=2, before=self.lbl_feedback)
        nr, gesamt = self.session.frage_nummer

        self.lbl_status.config(
            text=f"  Level: {self.session.aktuelles_level.upper()} "
                 f"| Frage {nr}/{gesamt}"
        )
        self.lbl_frage.config(text=frage.text)
        self.lbl_eingabe.config(text="")
        self.entry.pack_forget()
        self.lbl_feedback.config(text="", fg="black")
        self.lbl_score.config(
            text=f"Aktuelle Punkte: {self.session.aktuelle_punkte}"
        )
        self.eingabe_var.set("")

        if frage.qtype == "mc":
            self.lbl_eingabe.config(text="Wähle eine Antwort:")
            for i, option in enumerate(frage.auswahl):
                label = chr(ord("a") + i)
                self.radio_buttons[i].config(
                    text=f"{label})  {option}",
                    command=lambda l=label: self.eingabe_var.set(l)
                )
            self.radio_var.set(-1)

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
                rb.pack_forget()
            self.radio_var.set(-1)

        elif frage.qtype in ("text", "code"):
            self.lbl_eingabe.config(text="Deine Antwort:")
            self.entry.pack(anchor="w", pady=(4, 12), before=self.lbl_feedback)
            self._radiobuttons_leeren()

        self._btn_blau(self.btn1, "Antwort bestätigen", self._antwort_pruefen)
        self._btn_rot(self.btn2, "Quiz abbrechen", self._abbrechen)
        self._buttons_leeren(von=3, bis=5)

    # ── Antwort prüfen ───────────────────────────────────────────────────
    def _antwort_pruefen(self):
        antwort = self.eingabe_var.get().strip()
        if not antwort:
            messagebox.showwarning(
                "Keine Eingabe",
                "Bitte gib eine Antwort ein oder wähle eine Option!"
            )
            return

        ist_richtig, _, feedback = self.session.antwort_geben(antwort)

        if ist_richtig:
            self.lbl_feedback.config(
                text=f" {feedback}", fg=FARBE_RICHTIG
            )
        else:
            self.lbl_feedback.config(
                text=f"{feedback}", fg=FARBE_FALSCH
            )

        self.lbl_score.config(
            text=f"Aktuelle Punkte: {self.session.aktuelle_punkte}"
        )

        if self.session.level_fertig:
            self._btn_blau(self.btn1, "Level abschliessen", self._level_abschliessen)
        else:
            self._btn_blau(self.btn1, "Nächste Frage", self._zeige_frage)

    # ── Level abschliessen ───────────────────────────────────────────────
    def _level_abschliessen(self):
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
                f"Punkte: {punkte}"
            )

        if self._is_demo:
            messagebox.showinfo(
                "Demo beendet",
                "Der Demo-Modus ist abgeschlossen.\n"
                "Punkte werden nicht gespeichert."
            )
            self._zeige_hauptmenu()
            return

        self._zeige_frage()

    # ── Quiz-Ende ────────────────────────────────────────────────────────
    def _zeige_quiz_ende(self):
        self.session.speichern()

        self.lbl_status.config(text="  Quiz abgeschlossen!")
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

        messagebox.showinfo(
            "Quiz abgeschlossen!",
            f"Punktestand gespeichert:\n"
            f"{self.session.name}  →  {self.session.gesamt_punkte} Punkte"
        )

        self._btn_blau(self.btn1, "Nochmal spielen",     self._zeige_hauptmenu)
        self._btn_grau(self.btn2, "Punktestände",        self._zeige_scores)
        self._btn_rot (self.btn3, "Beenden",             self.root.quit)
        self._buttons_leeren(von=4, bis=5)

    # ── Punktestände ─────────────────────────────────────────────────────
    def _zeige_scores(self):
        scores = load_scores()
        if not scores:
            messagebox.showinfo(
                "Punktestände", "Noch keine Punktestände gespeichert."
            )
            return
        sortiert = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        text = "Punktestände:\n\n"
        for rang, (name, punkte) in enumerate(sortiert, start=1):
            text += f"{rang}.  {name}:  {punkte} Punkte\n"
        messagebox.showinfo("Punktestände", text)

    # ── Regeln ───────────────────────────────────────────────────────────
    def _zeige_regeln(self):
        messagebox.showinfo(
            "Regeln",
            "Das Quiz besteht aus drei Levels: leicht, mittel, schwer.\n\n"
            "Fragetypen:\n"
            "  • Multiple Choice (a, b, c, d)\n"
            "  • Ja / Nein\n"
            "  • Kurze Textantwort\n"
            "  • Eine Zeile Python-Code\n\n"
            "Ein Level gilt als bestanden, wenn mehr als die Hälfte\n"
            "der Fragen richtig beantwortet werden.\n\n"
            "Am Ende wird dein Punktestand gespeichert."
        )

    # ── Quiz abbrechen ───────────────────────────────────────────────────
    def _abbrechen(self):
        if messagebox.askyesno(
            "Quiz abbrechen",
            "Möchtest du das Quiz wirklich abbrechen?"
        ):
            name = self.session.name if self.session else ""
        self._zeige_optionen(name)


# ── Einstiegspunkt ───────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
