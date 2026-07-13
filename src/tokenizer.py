import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Lade die benötigten NLTK-Ressourcen herunter, falls sie nicht vorhanden sind
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")
    
try:
    nltk.data.find("tokenizers/punkt_tab/english")
except LookupError:
    nltk.download("punkt_tab")
    

# Definiere die Menge der englischen Stoppwörter
stop_words = set(stopwords.words("english"))


def tokenize_text(text: str) -> list:
    """
    Tokenisiert den Text, entfernt Satzzeichen und Stoppwörter.
    
    Args:
        text: Der zu tokenisierende Text als String.

    Returns:
        Eine Liste von Token (Wörtern) ohne Satzzeichen und Stoppwörter.
    """

    tokens = word_tokenize(text)

    tokens = [word.lower() for word in tokens]

    tokens = [
        word for word in tokens
        if word not in string.punctuation 
    ]

    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return tokens