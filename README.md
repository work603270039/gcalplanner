# Vendo Sync Planner 🗓️

CLI-narzędzie do automatycznego “wpychania” luźnych zadań z kalendarza **Backlog** do pierwszych wolnych okien w kalendarzu **Plan** (08:00–16:00, min gap = 15 min).

## Instalacja
```powershell
cd C:\Py\gcalplanner
python -m venv gcalplanner
.\gcalplanner\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Chat‑REPL
```powershell
copy .env.example .env   # uzupełnij OPENAI_API_KEY
python -m vendo_sync.cli.chat_cli chat
```


## 💡 Skróty uruchomieniowe

Po aktywacji venv możesz skorzystać z gotowych skryptów w katalogu głównym:

| Skrypt | Co robi |
|--------|---------|
| `run_chat.ps1`  | Otwiera PowerShell‑owy chat‑REPL (ChatGPT‑o3) |
| `run_planner.ps1` | Uruchamia komendę `:run` planera |
| `run_chat.bat`  | To samo dla `cmd.exe` |
| `run_planner.bat` | To samo dla `cmd.exe` |

Skrypty sprawdzają, czy istnieje lokalny venv `gcalplanner\Scripts\python.exe`.  
Jeśli tak – używają go; jeśli nie – wołają globalnego `python`.
