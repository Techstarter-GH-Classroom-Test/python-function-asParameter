# Programmieraufgabe: `anwenden()`

## Aufgabenbeschreibung

Erstellen Sie eine Funktion `anwenden()`, die eine Liste von Zahlen und eine Funktion als Eingabeparameter nimmt. Die Funktion soll die übergebene Funktion auf jedes Element der Liste anwenden.

### Anforderungen an die Funktion:

1. Die Funktion `anwenden()` muss:
   - Eine Liste von Zahlen und eine Funktion als Parameter akzeptieren.
   - Die Funktion auf jedes Element der Liste anwenden und eine neue Liste zurückgeben.

### Beispiel

Eingaben und erwartete Rückgaben:

```python
anwenden([1, 2, 3], lambda x: x * 2)  # Erwartete Rückgabe: [2, 4, 6]
anwenden([5, 10], lambda x: x + 3)   # Erwartete Rückgabe: [8, 13]
```

## Vorkenntnisse

Für die Bearbeitung dieser Aufgabe solltest du mit den folgenden Konzepten vertraut sein:

Funktionen als Objekte: Funktionen können als Argumente an andere Funktionen übergeben werden.
Listen-Verarbeitung: Iteration über Listen und Anwendung von Operationen auf ihre Elemente.

## Weiterführende Links

[Python-Dokumentation: Funktionen als Objekte](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
[Python-Dokumentation: Listen-Verarbeitung](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

---

## exercises

```python
def anwenden(numbers, func):
    """
    Wendet die übergebene Funktion auf jedes Element der Liste an.

    :param numbers: Liste von Zahlen
    :param func: Funktion, die auf jedes Listenelement angewendet wird
    :return: Neue Liste mit den Ergebnissen
    """
    return [func(x) for x in numbers]
```
