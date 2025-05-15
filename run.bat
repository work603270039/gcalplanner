@echo off
:: Uruchom PowerShell jako administrator i wykonaj skrypt PS1
powershell -Command "Start-Process powershell -Verb RunAs -ArgumentList '-NoExit','-ExecutionPolicy','Bypass','-File','C:\\Py\\gcalplanner\\gcal_start.ps1'"
