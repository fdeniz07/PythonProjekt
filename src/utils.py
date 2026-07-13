from pathlib import Path

def load_text(filename: str) -> str:
    """
    Lädt den Text aus einer Datei im data-Ordner des Projekts und gibt ihn als String zurück.
    """
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()