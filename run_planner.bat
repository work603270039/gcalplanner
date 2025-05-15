@echo off
setlocal
set VENV_PY=%~dp0gcalplanner\Scripts\python.exe
if exist "%VENV_PY%" (
  "%VENV_PY%" -m vendo_sync.cli.chat_cli run %*
) else (
  python -m vendo_sync.cli.chat_cli run %*
)
