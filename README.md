Projektdokumentation Python-Quiz GUI
Kurs: WIIMBIT25A | DHBW Mannheim | SoSe 2026
Team: Imara, Lea , Annika, Mehmet
1. Projektübersicht
Im Rahmen der Vorlesung Fortgeschrittene Programmierung haben wir unser
bestehendes CLI-basiertes Python-Quiz um eine grafische Benutzeroberfläche (GUI)
erweitert. Ziel war es, die Anwendung vollständig über eine tkinter-Oberfläche
bedienbar zu machen, ohne die bestehende Programmlogik grundlegend zu verändern.
Das Projekt wurde im Team erstellt, auf GitHub hochgeladen und abschließend präsentiert.
2. Teamstruktur und Rollenverteilung
Die Rollenverteilung im Team orientierte sich an den empfohlenen Rollen aus der
Aufgabenstellung:
• Lea - Lead Developer: Verantwortlich für die technische Integration von GUI
und Logik, Refrakturierung von quiz_engine.py und question.py sowie Pflege der
GitHub-Struktur.
• Imara - GUI-Entwicklung: Entwurf und Implementierung von
Fensterstruktur, Widgets, Layout und Design (Farbpalette, Schriftart, Seitenfluss).
• Mehmet - Testing: Sicherstellung dass bestehende Funktionen weiterhin
funktionieren, Ergänzung von Tests für neue Logik.
• Annika - Präsentation: Vorbereitung der Projektvorstellung.
3. Architektur und Dateistruktur
Bevor wir mit der GUI begonnen haben, haben wir zunächst die bestehende main.py
angepasst. Ziel war eine saubere Trennung von Darstellung und Logik:
• quiz_engine.py - Spielzustand, Levelwechsel, Punkteberechnung
• question.py - Fragelogik, kein print/input mehr
• questions.py - Fragedaten (unverändert)
• scoring.py - JSON-Lesen/-Schreiben (unverändert)
• cli.py - CLI-Schicht (ersetzt main.py)
• gui.py - GUI-Schicht (neu entwickelt)
4. Beschreibung der Oberfläche
Die GUI besteht aus einem einzigen Fenster, das sich je nach Spielzustand dynamisch
aktualisiert. Wir haben bewusst auf mehrere separate Fenster verzichtet und stattdessen alle Inhalte über .config() aktualisiert.
Seitenfluss
• Startseite - Namenseingabe mit Platzhalter-Text (Name eingeben)
• Hauptmenu - 5 Optionen: Komplettes Quiz, Level-Demo, Punktestände, Regeln,
Beenden
• Quiz / Level-Demo - Fragen nacheinander, Antworttyp bestimmt Eingabemethode
• Ergebnis-Dialoge - Rückmeldung nach jeder Frage (richtig/falsch)
• Abschluss - Punktestand wird gespeichert, Dialog informiert den Spieler
Design
Das Design wurde von einem blauen, klassischen Stil zu einem modernen Pink-Design
weiterentwickelt. Die Schriftart wurde auf Comic Sans MS umgestellt.
• Hintergrund: zartes Rosa (#FFF0F5)
• Kopfzeile / Buttons: kräftiges Pink (#E91E8C)
• Text: dunkles Lila-Pink (#4A0030)
• Karte: hellrosa (#FFE4EF)
Besonderheit: Radiobuttons und Entry
Für Multiple-Choice-Fragen verwenden wir Radiobutton-Widgets. Ein Klick schreibt den
Buchstaben automatisch per command=lambda in das Entry-Feld. Für Text- und
Code-Fragen ist das Entry-Feld direkt aktiv. Dieses Feature ermöglicht es, mit nur einem
Eingabefeld alle Fragetypen abzudecken.
5. GitHub-Workflow
Das Projekt wurde über GitHub und Teams Calls bearbeitet. Der Workflow umfasste
regelmäßige Commits, Push/Pull-Zyklen zur Synchronisierung im Team sowie die
Auflösung von Merge-Konflikten.

6. Was gut lief
• Refrakturierung der Logik: Die Trennung von question.py in Logik und Darstellung
verlief reibungslos.
• Farbgestaltung und Hover-Effekte: Modernes, flaches Design mit bg=/fg= und bind().
• GitHub-Workflow: Stabiler Commit/Push/Pull-Rhythmus trotz immer wieder aufkommender Schwierigkeiten.

7. Probleme und Lösungen
Problem 1: Git-Konfiguration und Merge-Konflikte
Vor dem ersten Commit fehlte die Git-Konfiguration (user.name und user.email). Commits schlugen mit der Meldung 'Please tell me who you are' fehl. Zusätzlich entstanden Merge-Konflikte durch __pycache__-Dateien die fälschlicherweise getrackt wurden.
Lösung: git config --global user.name/email im Terminal gesetzt. __pycache__ über
git rm --cached entfernt und .gitignore angelegt. Merge-Konflikte mit git checkout
--theirs aufgelöst.
Problem 2: Layout beim Seitenwechsel
Beim Wechsel zwischen Screens mit unterschiedlichen Inhalten verschoben sich Widgets durch pack_forget() / pack().
Lösung: Einführung von _build_screen(), die bei jedem Seitenwechsel alle
dynamischen Widgets vollständig entfernt und in fester Reihenfolge neu packt:
[Entry?] -> [Radiobuttons?] -> Feedback -> Score -> Buttons.
Problem 3: Blockierende Schleifen
Die ursprüngliche play_level()-Funktion lief als for-Schleife und wartete auf input(). GUIs
sind event-gesteuert, eine blockierende Schleife würde das Fenster einfrieren.
Lösung: quiz_engine.py als Zustandsmaschine neu geschrieben. Nach jeder Antwort
wird _zeige_frage() erneut aufgerufen.
Problem 4: Navigation zwischen Seiten
Der Zurück-Button führte fälschlicherweise zur Namenseingabe statt zum Hauptmenü.
Der Name wurde in Level-Demo erneut abgefragt.
Lösung: Name wird dauerhaft in self._name gespeichert. Alle Zurück-Buttons rufen
_zeige_optionen() auf.
Problem 5: Design und Positionierung
Das ursprüngliche Design wurde als zu altmodisch empfunden. Radiobuttons erschienen an falschen Positionen, Buttons hatten unterschiedliche Größen.
Lösung: Vollständige Überarbeitung der Farbpalette zu Pink-Design. Konsistente
anchor/justify-Parameter. Schriftart auf Comic Sans MS geändert.
8. Fazit
Im Laufe des Projekts sind wir auf viele technische und organisatorische
Herausforderungen gestoßen, von der Git-Konfiguration über Layout-Probleme bis hin
zur Umstrukturierung der Programmlogik. Dennoch konnten wir am Ende eine vollständig funktionierende GUI entwickeln, die alle geforderten Funktionen abdeckt.
Die Trennung von Logik und Darstellung, die zentrale _build_screen()-Methode und der klassenbasierte Aufbau haben das Projekt wartbar und erweiterbar gemacht. Das überarbeitete Pink-Design gibt der Anwendung ein modernes, einladendes Erscheinungsbild.
Die Zusammenarbeit im Team und der konsequente Einsatz von GitHub haben trotz
anfänglicher Schwierigkeiten gut funktioniert. Dieses Projekt hat uns gezeigt, dass
GUI-Entwicklung deutlich mehr Planung erfordert als CLI-Entwicklung - und dass es sich lohnt, von Anfang an auf eine klare Trennung von Darstellung und Logik zu achten.
