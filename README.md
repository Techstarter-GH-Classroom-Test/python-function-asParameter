# Aufgaben-Template
Das Template besteht aus folgenden Dateien:
- einem Github-Workflow in `.github/workflows/python-pipeline.yml`
- einer Configuration für Github Classroom `.github/classroom/autograding-python.json`
- einer README mit [README-Template](#readme-template)
- einem Template für Aufgaben: `exercises.py` 
- einem Template für Tests: `test_exercises.py` 

# To-Dos
1. Befüllen des Template-Textes der README (siehe [unten](#readme-template))
2. Befüllen der Datei in welcher die TNs die Aufgaben erledigen können (siehe `exercises.py`).
3. Befüllen der Test-Datei (siehe `test_exercises.py`). Aussagekräftige Error-Messages nutzen!
4. Löschen nicht benötigter Dateien
5. Verschieben der Test-Dateien in das Repo `Techstarter-GH-Classroom-Test/classroom_unit_tests`, Bennenung der Dateien nach dem Muster:
    - für Python: `test_repo-name.py`
6. Anpassen der `autograding.json`:
    1. Anpassen der Testnamen `name`.  Aussagekräftige Namen nutzen!
    2. Anpassen des `run`-Kommandos 
        - für Python: `python -m unittests file.Class.function`
    3. Anpassen der `points` (Punkte in Github Classroom pro Aufgabe)

# Testing-Frameworks
- für Python wird `unittests`genutzt

## Python-Unittesting mit unittests
1. Importieren des `unittests`-Moduls (native, keine Installation nötig)
2. Subclassing der `unittests.TestCase`-Klasse (Am besten einfach `Test`nennen)
3. Schreiben der Tests als Functionen der `Test`-Klasse
4. Nutzereingaben können für das Testen "gemockt" (Mocking) werden.

# Notion-Links
https://www.notion.so/techstarter/Github-Classroom-3acc378d53bc4156aa464b8259854431

https://www.notion.so/techstarter/Hausaufgaben-Automatisierung-15867eaf97d680e7bb94d22adcb50bb0

# README Template 

# Programmieraufgabe: `read_json()`

## Aufgabenbeschreibung

Schreibe eine Funktion `read_json(filename)`, die:
- Die Datei `daten.json` einliest.
- Die Werte des Schlüssels `name` ausgibt, wenn die Datei ein JSON-Array von Objekten enthält.
- Alle potenziellen Fehlerfälle berücksichtigt und spezifische Fehlermeldungen ausgibt.

### Anforderungen an die Funktion:
1. **Fehlerfall 1:** Wenn die Datei nicht existiert, soll folgender Fehler ausgegeben werden:
   ```
   Die Datei daten.json wurde nicht gefunden.
   ```
2. **Fehlerfall 2:** Wenn die Datei kein korrektes JSON enthält, soll folgender Fehler ausgegeben werden:
   ```
   Die Datei daten.json enthält kein gültiges JSON.
   ```
3. **Fehlerfall 3:** Wenn ein Objekt keinen Schlüssel `name` enthält, soll folgender Fehler ausgegeben werden:
   ```
   Kein 'name'-Schlüssel im Objekt: {objekt}
   ```
   Dabei bezeichnet `{objekt}` das aktuell überprüfte Objekt.
4. **Fehlerfall 4:** Wenn die Datei kein JSON-Array enthält, soll folgender Fehler ausgegeben werden:
   ```
   Die Datei daten.json enthält kein JSON-Array.
   ```

### Beispiel
Datei `daten.json`:
```json
[
    {"name": "Alice", "age": 25},
    {"age": 30},
    "Invalid Entry"
]
```

**Konsolenausgabe:**
```
Werte des Schlüssels 'name':
Alice
Kein 'name'-Schlüssel im Objekt: {'age': 30}
Kein 'name'-Schlüssel im Objekt: Invalid Entry
```

---

## Vorkenntnisse
Für die Bearbeitung dieser Aufgabe solltest du mit den folgenden Konzepten vertraut sein:
1. **Dateioperationen** in Python: Lesen von Dateien mit `open()`.
2. **JSON-Verarbeitung**: Nutzung des `json`-Moduls zum Laden und Verarbeiten von JSON-Daten.
3. **Fehlerbehandlung**: Umgang mit Ausnahmen mittels `try-except`.
4. **Iterieren über Datenstrukturen**: Verarbeiten von Listen und Dictionaries.

---

## Neue Konzepte in dieser Aufgabe
1. **Prüfen von Datenstrukturen**:
   - Überprüfen, ob eine JSON-Datenstruktur ein Array ist (`isinstance(data, list)`).
   - Überprüfen, ob ein Objekt ein Dictionary ist (`isinstance(item, dict)`).
2. **Arbeiten mit JSON-Daten**:
   - Umgang mit potenziell fehlerhaften JSON-Daten.
   - Dynamisches Extrahieren von Werten basierend auf Schlüsseln.
3. **Ausgeben von spezifischen Fehlermeldungen**:
   - Klar formulierte und informative Fehlermeldungen für Benutzer.

---

## Beispiele für neue Konzepte

### Fehlerbehandlung mit `try-except`:
```python
try:
    with open("daten.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("Die Datei daten.json wurde nicht gefunden.")
except json.JSONDecodeError:
    print("Die Datei daten.json enthält kein gültiges JSON.")
```

### Überprüfen der JSON-Datenstruktur:
```python
if isinstance(data, list):
    for item in data:
        if isinstance(item, dict) and 'name' in item:
            print(item['name'])
        else:
            print("Kein 'name'-Schlüssel im Objekt:", item)
else:
    print("Die Datei daten.json enthält kein JSON-Array.")
```

---

## Weiterführende Links

1. [Python-Dokumentation: Dateioperationen](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
2. [Python-Dokumentation: `json`-Modul](https://docs.python.org/3/library/json.html)
3. [Python-Dokumentation: Fehler- und Ausnahmenbehandlung](https://docs.python.org/3/tutorial/errors.html)
4. [Tutorial: Arbeiten mit JSON in Python](https://realpython.com/python-json/)
