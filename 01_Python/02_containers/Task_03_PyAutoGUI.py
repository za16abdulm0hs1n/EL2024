# This code is made for MacOS.
# For other OSs, change the hotkeys according to OS

import pyautogui
import time

def open_vscode():
    try:
        pyautogui.hotkey('command', 'space')

         
    except Exception:
        print (f"Error Opening Visual Studio Code: {Exception}")
        raise


open_vscode()
