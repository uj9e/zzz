@echo off
set "image_url=https://cdn.discordapp.com/attachments/1102891940674015263/1349125705170030662/thumb.jpeg?ex=67d1f6b9&is=67d0a539&hm=5ab11d1ea46ed09d2e07bb0abea2c91835635b817d46c5b585eb0dcb232168a1&"
set "image_path=%temp%\wallpaper.jpg"

powershell -Command "Invoke-WebRequest -Uri '%image_url%' -OutFile '%image_path%'"

reg add "HKCU\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "%image_path%" /f
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters

pause
