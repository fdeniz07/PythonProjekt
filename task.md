# Projektarbeit – Python Text Summarizer

## Ausgangssituation

In einer Zeit, in der Informationen im Überfluss vorhanden sind, gewinnt die Fähigkeit, Texte effizient zusammenzufassen, immer mehr an Bedeutung.

Ziel dieses Projekts ist die Entwicklung eines Python-Programms, das mithilfe der **Natural Language Toolkit (NLTK)**-Bibliothek eine **extraktive Textzusammenfassung** erstellt.

Das Programm soll aus einem längeren Text die wichtigsten Informationen extrahieren und als kurze Zusammenfassung ausgeben.

Als Grundlage dient ein bereitgestellter Text zum Thema **Climate Science**.

---

# Arten der Textzusammenfassung

Grundsätzlich unterscheidet man zwei Arten der automatischen Textzusammenfassung.

## Extraktive Zusammenfassung

Bei der extraktiven Zusammenfassung werden vorhandene Sätze oder Textabschnitte aus dem Originaltext ausgewählt.

### Eigenschaften

- Verwendet ausschließlich vorhandene Sätze
- Keine Generierung neuer Inhalte
- Einfach zu implementieren
- Bewahrt Originalität und Kontext des Textes

### Vorteile

- Einfache Umsetzung
- Hohe Genauigkeit
- Originalformulierungen bleiben erhalten

---

## Abstraktive Zusammenfassung

Bei der abstraktiven Zusammenfassung wird der Inhalt neu formuliert.

### Eigenschaften

- Erzeugt neue Formulierungen
- Nutzt Methoden der Natural Language Generation (NLG)
- Höhere Flexibilität
- Kreativere Zusammenfassungen

### Nachteile

- Deutlich komplexere Implementierung
- Höheres Risiko grammatikalischer oder semantischer Fehler

---

## Vergleich

| Extraktiv | Abstraktiv |
|------------|------------|
| Verwendet Originaltext | Erzeugt neue Formulierungen |
| Einfach umzusetzen | Komplex umzusetzen |
| Originalkontext bleibt erhalten | Kreativere Ergebnisse |
| Weniger Rechenaufwand | Höherer Rechenaufwand |

---

# Ziel des Projekts

In diesem Projekt wird ausschließlich eine **extraktive Textzusammenfassung** erstellt.

Dafür wird ein Text über **Climate Science** analysiert.

---

# Vorgehensweise

Die Zusammenfassung wird in mehreren Schritten erzeugt.

1. Text tokenisieren
2. Satzzeichen und Stopwords entfernen
3. Worthäufigkeiten bestimmen
4. Wortfrequenzen normalisieren
5. Text in einzelne Sätze aufteilen
6. Sentence Score berechnen
7. Die besten 20 % der Sätze auswählen
8. Zusammenfassung erzeugen

---

# Aufgaben

## Aufgabe 1 – NLTK kennenlernen

- NLTK installieren
- `word_tokenize()` kennenlernen
- `sent_tokenize()` kennenlernen
- Stopwords verwenden

---

## Aufgabe 2 – Text tokenisieren

Eine Funktion erstellen, die

- den Text tokenisiert
- Satzzeichen entfernt
- Stopwords entfernt

Als Ergebnis soll eine bereinigte Tokenliste entstehen.

---

## Aufgabe 3 – Word Count berechnen

Für jedes Wort wird die Häufigkeit bestimmt.

Anschließend werden

- das häufigste Wort gesucht
- alle Worthäufigkeiten normalisiert

Hierfür soll ein **Dictionary** verwendet werden.

---

## Aufgabe 4 – Sentence Count berechnen

Für jeden Satz wird ein Score berechnet.

Der Sentence Count ergibt sich aus der Summe der normalisierten Wortfrequenzen aller Wörter im Satz.

### Beispiel

Dictionary

```python
{
    "Climate": 3,
    "Science": 1,
    "Weather": 5,
    "Cars": 2
}