# 📝 Python Text Summarizer

An educational Python project that implements **Extractive Text Summarization** using the **Natural Language Toolkit (NLTK)**.

The application analyzes a text, calculates word frequencies, scores every sentence, and automatically generates a concise summary by selecting the most relevant sentences.

---

## 📚 Project Background

This project was developed as part of a Python course project.

The objective is to implement an **extractive text summarization algorithm** without using machine learning or AI models.

Instead, the algorithm relies on classical Natural Language Processing (NLP) techniques provided by the **NLTK** library.

---

## 🚀 Features

- Read text files
- Tokenize text
- Remove punctuation
- Remove English stopwords
- Calculate word frequencies
- Normalize word frequencies
- Split text into sentences
- Calculate sentence scores
- Select the top 20% highest-ranked sentences
- Generate an extractive text summary

---

## 🏗️ Project Structure

```text
PythonProjekt/
│
├── data/
│   └── ClimateScienceText.txt
│
├── src/
│   ├── utils.py
│   ├── tokenizer.py
│   ├── frequency.py
│   ├── summarizer.py
│   └── main.py
│
├── requirements.txt
├── SUMMARY.md
└── README.md
```

---

## ⚙️ Technologies

- Python 3
- NLTK
- Dictionaries
- Functions
- Modular Programming
- Natural Language Processing (NLP)

---

## 📋 Workflow

```text
Read Text
      │
      ▼
Tokenization
      │
      ▼
Remove Stopwords
      │
      ▼
Calculate Word Frequencies
      │
      ▼
Normalize Frequencies
      │
      ▼
Split into Sentences
      │
      ▼
Calculate Sentence Scores
      │
      ▼
Select Top 20%
      │
      ▼
Generate Summary
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/fdeniz07/PythonProjekt.git
```

Open the project

```bash
cd PythonProjekt
```

Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python src/main.py
```

---

## 📄 Example Output

```text
================================================================================
SUMMARY
================================================================================

Climate science is a vast and multifaceted discipline...

Understanding the drivers of climate change...

Renewable energy technologies...

Climate science informs urban planning...

Climate science is a vital and indispensable field...
```

---

## 🎯 Learning Objectives

This project demonstrates:

- Text preprocessing
- Tokenization
- Stopword removal
- Dictionary usage
- Frequency analysis
- Sentence scoring
- Extractive summarization
- Modular software design
- Clean code principles

---

## 📖 Documentation

Additional documentation is available in:

- `SUMMARY.md`

---

## 🔮 Possible Improvements

- Support for multiple languages
- PDF document summarization
- Graphical user interface (Tkinter or PySide)
- Adjustable summary percentage
- Command-line arguments
- Export summary to TXT or PDF
- Web API with FastAPI
- Web application with Flask

---

## 👨‍💻 Author

**Fatih Deniz**

Software Developer

GitHub: https://github.com/fdeniz07

---

## 📜 License

This project was created for educational purposes.
