@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"
set "startupFolder=%AppData%\Microsoft\Windows\Start Menu\Programs\Startup"
for %%F in (*.*) do (
    if /i not "%%~xF"==".bat" (
        copy /y "%%F" "%startupFolder%"
    )
)
set "regKey=HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
for %%F in (*.*) do (
    if /i not "%%~xF"==".bat" (
        reg add "%regKey%" /v "%%~nF" /t REG_SZ /d "%cd%\%%F" /f
    )
)
