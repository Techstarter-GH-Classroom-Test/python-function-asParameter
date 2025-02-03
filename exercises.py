def anwenden(numbers, func):
    """
    Wendet die übergebene Funktion auf jedes Element der Liste an.

    :param numbers: Liste von Zahlen
    :param func: Funktion, die auf jedes Listenelement angewendet wird
    :return: Neue Liste mit den Ergebnissen
    """
    return [func(x) for x in numbers]
