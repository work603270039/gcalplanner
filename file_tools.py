"""
Minimalny zestaw narzędzi do przeglądania plików z poziomu agenta O3.
Zawiera:
  * ls  – listuje zawartość katalogu
  * cat – zwraca zawartość pliku tekstowego
  * run – uruchamia dowolne polecenie powłoki (ostrożnie!)
"""
from pathlib import Path
import subprocess
from typing import List

def ls(path: str = ".") -> List[str]:
    """Zwraca listę plików / katalogów w *path*."""
    return [p.name for p in Path(path).iterdir()]

def cat(path: str) -> str:
    """Zwraca zawartość pliku tekstowego UTF‑8."""
    return Path(path).read_text(encoding="utf-8")

def run(cmd: str) -> str:
    """Uruchamia polecenie powłoki i zwraca stdout (tekst)."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout
