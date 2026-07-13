"""
 Funktion zur Berechnung der Wortfrequenzen in einem gegebenen Text.
"""


def calculate_word_frequencies(tokens: list) -> dict:
    """
    Berechnet normalisierte Wortfrequenzen.

    Args:
        tokens (list):
            Bereinigte Liste von Wörtern.

    Returns:
        dict:
            Wörterbuch mit normalisierten Wortfrequenzen.
    """

    word_frequencies = {}

    # Zähle jedes Wort
    for word in tokens:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

    # Finde die höchste Frequenz
    max_frequency = max(word_frequencies.values())

    # Normalisiere die Frequenzen
    for word in word_frequencies:
        word_frequencies[word] = (
            word_frequencies[word] / max_frequency
        )

    return word_frequencies