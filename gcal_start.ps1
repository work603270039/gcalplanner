Write-Host "✅ Uruchomiono skrypt PowerShell"
Set-Location -Path "C:\Py\gcalplanner"

if (Test-Path ".\.venv.gcal\Scripts\Activate.ps1") {
    Write-Host "✅ Środowisko znalezione, aktywuję..."
    .\.venv.gcal\Scripts\Activate.ps1
} else {
    Write-Host "❌ Nie znaleziono środowiska .venv.gcal\Scripts\Activate.ps1"
}

Write-Host "`n--- KONIEC ---"
pause
