# Vendo Sync Planner 🗓️

CLI-narzędzie do automatycznego “wpychania” luźnych zadań z kalendarza **Backlog** do pierwszych wolnych okien w kalendarzu **Plan** (08:00-16:00, min gap = 15 min) w horyzoncie 30 dni.

## Instalacja
```bash
python -m venv .venv && source .venv/Scripts/activate  # Windows PowerShell
pip install -r requirements.txt
```

## Szybki start
```bash
cp .env.example .env               # uzupełnij wartości
python -m vendo_sync.cli.chat_cli  # uruchom tryb interaktywny
```

## Struktura katalogów
```
vendo_sync/
├─ planner/           # logika pobierania, planowania, zapisu
├─ cli/               # interaktywny REPL :run / :auto / …
├─ tests/             # pytest
└─ ...
```

Szczegóły wymagań i roadmapa → patrz `docs/BRIEF.md` (prompt użytkownika).
