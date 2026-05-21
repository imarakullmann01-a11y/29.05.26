# Enthält alle Fragen für die drei Levels:
# leicht  (max 5 Punkte pro Frage)
# mittel  (max 10 Punkte pro Frage)
# schwer  (max 15 Punkte pro Frage)


from question import Question


def create_fragen():
    #  LEICHT 
    fragen_leicht = [
        Question(
            text="Ist Python eine Programmiersprache?",
            qtype="yn",
            punkte=5,
            richtig_text="ja"
        ),
        Question(
            text="Wie heißt der Datentyp für ganze Zahlen in Python?",
            qtype="text",
            punkte=5,
            richtig_text="int"
        ),
        Question(
            text="Schreibe eine Python-Zeile, die x den Wert 5 zuweist.",
            qtype="code",
            punkte=5,
            richtig_text="x = 5"
        ),
        Question(
            text="Wie wird Python typisiert?",
            qtype="mc",
            punkte=5,
            auswahl=[
                "statisch typisiert",
                "dynamisch typisiert",
                "gar nicht typisiert",
                "nur zur Compile-Zeit typisiert"
            ],
            richtig_index=1
        ),
        Question(
            text="Was ist eine IDE?",
            qtype="mc",
            punkte=5,
            auswahl=[
                "Eine Hardware-Komponente",
                "Eine integrierte Entwicklungsumgebung zum Programmieren",
                "Ein Datentyp",
                "Ein Betriebssystem"
            ],
            richtig_index=1
        ),
        Question(
            text="Ist Jupyter Notebook ein Werkzeug, mit dem man interaktiv Python-Code ausführen kann?",
            qtype="yn",
            punkte=5,
            richtig_text="ja"
        ),
        Question(
            text="Welcher Datentyp steht in Python für Zeichenketten?",
            qtype="mc",
            punkte=5,
            auswahl=["int", "float", "str", "bool"],
            richtig_index=2
        ),
        Question(
            text="Wie heißt der boolesche Literalwert für wahr in Python?",
            qtype="text",
            punkte=5,
            richtig_text="True"
        ),
        Question(
            text="Schreibe eine Python-Zeile, die eine leere Liste erzeugt und in der Variablen data speichert.",
            qtype="code",
            punkte=5,
            richtig_text="data = []"
        ),
        Question(
            text="Unterstützt Python objektorientierte Programmierung?",
            qtype="yn",
            punkte=5,
            richtig_text="ja"
        ),
    ]

    # MITTEL 
    fragen_medium = [
        Question(
            text="Welchen Datentyp hat der Ausdruck 42.0 in Python?",
            qtype="mc",
            punkte=10,
            auswahl=["int", "float", "str", "bool"],
            richtig_index=1
        ),
        Question(
            text="Welcher Operator führt eine Ganzzahldivision durch?",
            qtype="text",
            punkte=10,
            richtig_text="//"
        ),
        Question(
            text="Ist True in Python ein boolescher Wert?",
            qtype="yn",
            punkte=10,
            richtig_text="ja"
        ),
        Question(
            text="Wie lautet der Datentyp von True in Python?",
            qtype="mc",
            punkte=10,
            auswahl=["int", "bool", "str", "float"],
            richtig_index=1
        ),
        Question(
            text="Welcher Dateimodus öffnet eine Datei nur zum Lesen?",
            qtype="text",
            punkte=10,
            richtig_text="r"
        ),
        Question(
            text="Ist 'with open(\"datei.txt\", \"r\") as f:' eine sinnvolle Art, eine Datei zu öffnen?",
            qtype="yn",
            punkte=10,
            richtig_text="ja"
        ),
        Question(
            text="Schreibe eine Python-Zeile, die die Liste numbers mit den Werten 1, 2 und 3 erstellt.",
            qtype="code",
            punkte=10,
            richtig_text="numbers = [1, 2, 3]"
        ),
        Question(
            text="Welcher Operator steht für Potenzierung (z.B. 2 hoch 3)?",
            qtype="mc",
            punkte=10,
            auswahl=["^", "%", "**", "//"],
            richtig_index=2
        ),
        Question(
            text="Wie lautet der Rückgabewert des Ausdrucks 5 == 5 in Python?",
            qtype="text",
            punkte=10,
            richtig_text="True"
        ),
        Question(
            text="Kann man mit Python Textdateien schreiben?",
            qtype="yn",
            punkte=10,
            richtig_text="ja"
        ),
    ]

    # SCHWER
    fragen_schwer = [
        Question(
            text="Wie heißt das offizielle Style-Guide-Dokument für Python?",
            qtype="text",
            punkte=15,
            richtig_text="PEP 8"
        ),
        Question(
            text="Schreibe eine Funktionsdefinition foo(x), die x + 1 zurückgibt (in einer Zeile).",
            qtype="code",
            punkte=15,
            richtig_text="def foo(x): return x+1"
        ),
        Question(
            text="Ist Assembler eine Sprache mit niedrigem Abstraktionsgrad?",
            qtype="yn",
            punkte=15,
            richtig_text="ja"
        ),
        Question(
            text="Welche Aussage zu Python ist korrekt?",
            qtype="mc",
            punkte=15,
            auswahl=[
                "Python ist nur funktional.",
                "Python unterstützt mehrere Programmierparadigmen.",
                "Python ist nur deklarativ.",
                "Python kann nur Logikprogrammierung."
            ],
            richtig_index=1
        ),
        Question(
            text="Ist '2variable' ein gültiger Variablenname in Python?",
            qtype="yn",
            punkte=15,
            richtig_text="nein"
        ),
        Question(
            text="Welcher Dateimodus überschreibt eine bestehende Datei beim Öffnen?",
            qtype="text",
            punkte=15,
            richtig_text="w"
        ),
        Question(
            text="Welche logische Aussage entspricht NOT (x OR y)?",
            qtype="mc",
            punkte=15,
            auswahl=[
                "NOT x AND NOT y",
                "x AND y",
                "NOT x OR NOT y",
                "x OR y"
            ],
            richtig_index=0
        ),
        Question(
            text="Schreibe eine for-Schleife, die die Zahlen 0 bis 4 ausgibt (in einer Zeile).",
            qtype="code",
            punkte=15,
            richtig_text="for i in range(5): print(i)"
        ),
        Question(
            text="Ist Python dynamisch typisiert?",
            qtype="yn",
            punkte=15,
            richtig_text="ja"
        ),
        Question(
            text="Ist 'while' in Python eine Schleifen-Kontrollstruktur?",
            qtype="yn",
            punkte=15,
            richtig_text="ja"
        ),
    ]

    # Dictionary mit allen Levels zurückgeben
    return {
        "leicht": fragen_leicht,
        "mittel": fragen_medium,
        "schwer": fragen_schwer,
    }