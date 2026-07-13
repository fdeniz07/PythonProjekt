"""
Funktion zur Bewertung von Sätzen basierend auf den Wortfrequenzen.
"""

from nltk.tokenize import sent_tokenize, word_tokenize
from heapq import nlargest

def score_sentences(text: str,
                    word_frequencies: dict) -> dict:
    """
    Bewertet jeden Satz basierend auf den Wortfrequenzen.

    Args:
        text:
            Originaltext.

        word_frequencies:
            Wörterbuch mit normalisierten Wortfrequenzen.

    Returns:
        Wörterbuch mit Satzbewertungen.
    """

    sentence_scores: dict[str, float] = {}

    sentences = sent_tokenize(text)

    for sentence in sentences:

        sentence_score = 0

        words = word_tokenize(sentence.lower())

        for word in words:

            if word in word_frequencies:
                sentence_score += word_frequencies[word]

        sentence_scores[sentence] = sentence_score

    return sentence_scores




def generate_summary(sentence_scores: dict,
                     text: str,
                     percentage: float = 0.2) -> str:
    """
    Erstellt eine extraktive Zusammenfassung.

    Args:
        sentence_scores:
            Wörterbuch mit Satzbewertungen.

        text:
            Originaltext.

        percentage:
            Prozentsatz der zu behaltenden Sätze.

    Returns:
        Zusammenfassung als String.
    """

    sentences = sent_tokenize(text)

    number_of_sentences = max(
        1,
        int(len(sentences) * percentage)
    )

    best_sentences = nlargest(
        number_of_sentences,
        sentence_scores.keys(),
        key=lambda sentence: sentence_scores[sentence]
    )

    # Erstelle die Zusammenfassung, indem die besten Sätze in der Reihenfolge ihres Auftretens im Originaltext zusammengefügt werden.
    summary = []

    for sentence in sentences:
        if sentence in best_sentences:
            summary.append(sentence)

    return "\n\n".join(summary)