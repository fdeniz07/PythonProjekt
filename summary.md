# Projektarbeit – Zusammenfassung der Arbeitsschritte

## Aufgabe 1 – NLTK-Bibliothek kennenlernen

### Ergebnis

- Die NLTK-Bibliothek wurde erfolgreich in einer virtuellen Python-Umgebung installiert.
- Die wichtigsten Funktionen der Bibliothek wurden untersucht und getestet.
- Die Funktionen `word_tokenize()` und `sent_tokenize()` wurden für die Tokenisierung von Wörtern und Sätzen kennengelernt.
- Die integrierten englischen Stopwords wurden mithilfe von `stopwords.words("english")` eingebunden.
- Die Entwicklungsumgebung wurde für die weitere Projektarbeit vorbereitet.

---

## Aufgabe 2 – Text tokenisieren

### Ergebnis

- Der bereitgestellte Climate-Science-Text wurde erfolgreich eingelesen.
- Der Text wurde mit `word_tokenize()` in einzelne Wörter zerlegt.
- Alle Wörter wurden in Kleinbuchstaben umgewandelt.
- Satzzeichen wurden entfernt.
- Englische Stopwords wurden aus der Tokenliste entfernt.
- Es wurde eine bereinigte Tokenliste erstellt, die als Grundlage für die weitere Analyse dient.

---

## Aufgabe 3 – Word Count berechnen

### Ergebnis

- Die bereinigte Tokenliste wurde verwendet, um die Häufigkeit jedes Wortes zu bestimmen.
- Für die Speicherung der Worthäufigkeiten wurde ein Dictionary verwendet.
- Das Wort mit der höchsten Häufigkeit wurde ermittelt.
- Alle Word Counts wurden anhand des höchsten Wertes normalisiert.
- Die normalisierten Wortfrequenzen bilden die Grundlage für die Bewertung der einzelnen Sätze.

---

## Aufgabe 4 – Sentence Count berechnen

### Ergebnis

- Der Originaltext wurde mit `sent_tokenize()` in einzelne Sätze aufgeteilt.
- Jeder Satz wurde analysiert und in einzelne Wörter zerlegt.
- Für jedes im Dictionary enthaltene Wort wurde die normalisierte Wortfrequenz addiert.
- Dadurch wurde für jeden Satz ein individueller Sentence Score berechnet.
- Die Satzbewertungen wurden in einem Dictionary gespeichert und dienen als Grundlage für die Auswahl der wichtigsten Sätze.

---

## Aufgabe 5 – Extraktive Textzusammenfassung

### Ergebnis

- Alle Sätze wurden anhand ihres Sentence Scores bewertet.
- Die 20 % der Sätze mit den höchsten Bewertungen wurden ausgewählt.
- Die ausgewählten Sätze wurden in ihrer ursprünglichen Reihenfolge beibehalten.
- Aus diesen Sätzen wurde automatisch eine extraktive Textzusammenfassung erstellt.
- Die fertige Zusammenfassung wird als String in der Konsole ausgegeben.

---

# Fazit

Im Rahmen dieser Projektarbeit wurde erfolgreich ein Python-Programm zur **extraktiven Textzusammenfassung** entwickelt.

Das Programm verarbeitet einen Text in mehreren Schritten:

1. Tokenisierung des Textes
2. Entfernen von Satzzeichen und Stopwords
3. Berechnung und Normalisierung der Wortfrequenzen
4. Bewertung aller Sätze anhand ihrer Wortfrequenzen
5. Auswahl der wichtigsten 20 % der Sätze
6. Ausgabe einer automatisch erzeugten Zusammenfassung

Durch den modularen Aufbau mit mehreren Python-Modulen (`utils.py`, `tokenizer.py`, `frequency.py`, `summarizer.py` und `main.py`) ist der Quellcode übersichtlich, wartbar und leicht erweiterbar. Außerdem wurden Docstrings und aussagekräftige Variablennamen verwendet, um eine gute Lesbarkeit und Verständlichkeit sicherzustellen.