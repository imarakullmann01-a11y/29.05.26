from quiz_engine import QuizSession
from scoring import load_scores


# ── Hilfsfunktion: Eingabe für eine Frage holen ─────────────────────────────
def _eingabe_holen(frage) -> str:
    SONDERBEFEHLE = ("!punkte", "!restart")

    if frage.qtype == "mc":
        for i, opt in enumerate(frage.auswahl):
            print(f"  {chr(ord('a') + i)}) {opt}")
        max_letter = chr(ord("a") + len(frage.auswahl) - 1)
        while True:
            antwort = input(f"Deine Antwort (a-{max_letter}): ").strip().lower()
            if antwort in SONDERBEFEHLE:
                return antwort
            if len(antwort) == 1 and "a" <= antwort <= max_letter:
                return antwort
            print(f"Bitte eine gültige Option (a-{max_letter}) eingeben.")

    elif frage.qtype == "yn":
        while True:
            antwort = input("Deine Antwort (ja/nein): ").strip().lower()
            if antwort in SONDERBEFEHLE:
                return antwort
            if antwort in ("ja", "j", "nein", "n"):
                return antwort
            print("Bitte 'ja' oder 'nein' eingeben.")

    elif frage.qtype == "code":
        print("Bitte gib eine einzelne Python-Codezeile ein.")
        return input("Code: ").strip()

    else:
        return input("Deine Antwort: ").strip()


# ── Komplettes Quiz ──────────────────────────────────────────────────────────
def play_quiz():
    name = input("Bitte gib deinen Namen ein: ").strip()
    if not name:
        name = "Gast"

    scores = load_scores()
    bisherige = scores.get(name, 0)
    if bisherige > 0:
        print(f"\nWillkommen zurück, {name}! Bisheriger Punktestand: {bisherige} Punkte.")
    else:
        print(f"\nHallo {name}, viel Erfolg!")

    session = QuizSession(name=name)

    while not session.quiz_beendet:
        print(f"\n{'='*50}")
        print(f"LEVEL: {session.aktuelles_level.upper()}")
        print("=" * 50)

        while not session.level_fertig:
            frage = session.aktuelle_frage
            nr, gesamt = session.frage_nummer
            print(f"\nFrage {nr}/{gesamt}: {frage.text}")

            antwort = _eingabe_holen(frage)

            if antwort == "!punkte":
                print(f"Aktueller Punktestand: {session.aktuelle_punkte} Punkte")
                continue

            if antwort == "!restart":
                session.neustart()
                print("\n🔁 Neustart wird ausgeführt...")
                break

            ist_richtig, _, feedback = session.antwort_geben(antwort)
            print(f"{'✅' if ist_richtig else '❌'} {feedback}")

        if session.level_fertig:
            bestanden, punkte = session.level_abschliessen()
            if bestanden:
                print(f"\n🎉 Level '{session.LEVELS[session.level_index - 1]}' bestanden! +{punkte} Punkte")
            else:
                print(f"\n❌ Zu viele Fehler. Level wird wiederholt.")

    print(f"\n{'='*50}")
    print(f"Quiz abgeschlossen! Gesamtpunkte: {session.gesamt_punkte}")
    print("=" * 50)
    session.speichern()
    print(f"💾 Punktestand gespeichert: {name} → {session.gesamt_punkte} Punkte")


# ── Level-Demo ───────────────────────────────────────────────────────────────
def single_level_demo():
    while True:
        print(f"\n{'='*50}")
        print("LEVEL-DEMO – EINZELNES LEVEL SPIELEN")
        print("=" * 50)
        print("1) Leicht")
        print("2) Mittel")
        print("3) Schwer")
        print("4) Zurück ins Hauptmenü")
        choice = input("> ").strip()

        level_map = {"1": "leicht", "2": "mittel", "3": "schwer"}

        if choice == "4" or choice == "":
            print("Zurück ins Hauptmenü...")
            break
        if choice not in level_map:
            print("Bitte eine gültige Option (1–4) eingeben.")
            continue

        level_key = level_map[choice]
        session = QuizSession(name="Demo", start_level=level_key)

        print(f"\n{'='*50}")
        print(f"LEVEL-DEMO: {level_key.upper()}")
        print("=" * 50)

        while not session.level_fertig:
            frage = session.aktuelle_frage
            nr, gesamt = session.frage_nummer
            print(f"\nFrage {nr}/{gesamt}: {frage.text}")

            antwort = _eingabe_holen(frage)

            if antwort == "!punkte":
                print(f"Punkte in diesem Level: {session.level_punkte}")
                continue

            ist_richtig, _, feedback = session.antwort_geben(antwort)
            print(f"{'✅' if ist_richtig else '❌'} {feedback}")

        print(f"\nLevel abgeschlossen! Erreichte Punkte: {session.level_punkte}")
        print("Hinweis: Im Demo-Modus werden keine Punktestände gespeichert.")
        input("\nDrücke Enter um fortzufahren...")


# ── Punktestände ─────────────────────────────────────────────────────────────
def show_scores():
    scores = load_scores()
    print(f"\n{'='*50}")
    print("PUNKTESTÄNDE")
    print("=" * 50)
    if not scores:
        print("Noch keine Punktestände gespeichert.")
    else:
        sortiert = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for rang, (name, punkte) in enumerate(sortiert, start=1):
            print(f"{rang}. {name}: {punkte} Punkte")
    print("=" * 50)
    input("\nDrücke Enter um fortzufahren...")


# ── Regeln ───────────────────────────────────────────────────────────────────
def show_rules():
    print(f"\n{'='*50}")
    print("REGELN")
    print("=" * 50)
    print("- Das Quiz besteht aus drei Schwierigkeitsstufen: leicht, mittel und schwer.")
    print("- In jedem Level werden die Fragen zufällig gemischt.")
    print("- Es gibt verschiedene Fragetypen:")
    print("      • Multiple Choice (a, b, c, d)")
    print("      • Ja/Nein-Fragen")
    print("      • kurze Textantworten")
    print("      • eine Zeile Python-Code")
    print("- Für jede richtige Antwort erhältst du eine bestimmte Punktzahl.")
    print("- Ein Level gilt als bestanden, wenn du mehr als die Hälfte der Fragen richtig beantwortest.")
    print("- Am Ende eines Durchlaufs wird dein Punktestand gespeichert.")
    print("")
    print("Zusätzliche Befehle während des Quiz:")
    print("- !punkte   → zeigt deinen aktuellen Punktestand")
    print("- !restart  → bricht das Quiz ab und startet neu")
    print("=" * 50)
    input("\nDrücke Enter um fortzufahren...")


# ── Hauptmenü ────────────────────────────────────────────────────────────────
def main_menu():
    while True:
        print(f"\n{'='*50}")
        print("PYTHON-QUIZ – HAUPTMENÜ")
        print("=" * 50)
        print("1) Komplettes Quiz (leicht → mittel → schwer)")
        print("2) Level-Demo (einzelnes Level auswählen)")
        print("3) Punktestände anzeigen")
        print("4) Regeln anzeigen")
        print("5) Beenden")
        choice = input("> ").strip()

        if choice == "1":
            play_quiz()
        elif choice == "2":
            single_level_demo()
        elif choice == "3":
            show_scores()
        elif choice == "4":
            show_rules()
        elif choice == "5" or choice == "":
            print("\nDanke fürs Spielen! 👋")
            break
        else:
            print("Bitte eine gültige Option eingeben.")


if __name__ == "__main__":
    main_menu()