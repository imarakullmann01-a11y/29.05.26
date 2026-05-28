## Rolle: Testverantwortlicher

Meine Aufgabe als Testverantwortlicher war es, sicherzustellen, dass die bestehende Programmlogik trotz der neuen tkinter-GUI weiterhin korrekt funktioniert. Außerdem wurden Tests für neue oder veränderte Logik ergänzt.

## Getestete Bereiche

Getestet wurden:

- Start einer Quiz-Session
- Speicherung des Spielernamens
- Startlevel des Quiz
- richtige Antworten
- falsche Antworten
- Punktevergabe
- Levelabschluss bei bestandenem Level
- Levelwiederholung bei nicht bestandenem Level
- Neustart des Quiz
- Speichern und Laden von Punkteständen
- Verhalten bei fehlender `scores.json`
- Verhalten bei beschädigter `scores.json`

## Vorgehensweise

Für die Tests wurden künstliche Testfragen verwendet. Dadurch sind die Tests unabhängig von der zufälligen Reihenfolge der echten Quizfragen. Die Klasse `FakeFrage` simuliert eine normale Quizfrage mit einer richtigen Antwort, Punkten und Feedback.

Mit `monkeypatch` wird die Funktion `create_fragen()` im Test ersetzt. Dadurch verwendet `QuizSession` während des Tests kontrollierte Testdaten.

## Ergebnis

Die Tests prüfen, ob die zentrale Quiz-Logik unabhängig von der GUI funktioniert. Besonders wichtig war, dass die GUI die Logik nur aufruft, aber nicht direkt verändert. Dadurch bleibt die Trennung zwischen Logik und Darstellung erhalten.

## Fazit

Die Programmlogik bleibt trotz GUI-Erweiterung testbar und stabil. Die Tests decken zentrale Funktionen wie Antwortprüfung, Punktevergabe, Levelsystem, Neustart und Score-Speicherung ab.
