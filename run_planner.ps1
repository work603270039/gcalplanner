$ErrorActionPreference = "Stop"
$venvPy = Join-Path $PSScriptRoot "gcalplanner\Scripts\python.exe"
if (Test-Path $venvPy) {
    & $venvPy -m vendo_sync.cli.chat_cli run @args
} else {
    python -m vendo_sync.cli.chat_cli run @args
}
