# This code is designed for macOS; please change the hotkeys for other operating systems.

import pyautogui
import time
import os
def wait_seconds(seconds = 1):
    time.sleep(seconds)

#--------------------------------
def clean_search_bar():
    try:
        wait_seconds(1)
        
        pyautogui.hotkey('command', 'a', interval=0.1)
        wait_seconds(1)

        pyautogui.press('backspace', interval=0.1)
        wait_seconds(1)
    except Exception as e:
        print(f"Error Cleaning Search Bar: {e}")

#-------------------------------
def open_vscode():
    try:

        wait_seconds(1)

        pyautogui.hotkey('command', 'space', interval=0.1)
        wait_seconds(1)

        clean_search_bar()
        pyautogui.write(' Visual Studio Code', interval=0.1)
        wait_seconds(1)

        pyautogui.press('enter', interval=0.1)
        wait_seconds(5)

    except Exception as e:
        print(f"Error Opening VSCode: {e}")

#--------------------------------
def open_extensions_sildbar():
    try:
        wait_seconds(1)

        pyautogui.hotkey('command', 'shift', 'x', interval=0.1)
        wait_seconds(1)

        clean_search_bar()
        wait_seconds(1)
    except Exception as e:
        print(f"Error Opening Extensions Sildbars : {e}")

#-------------------------------
def search_extension(extension_name=''):
    try:
        wait_seconds(1)

        pyautogui.write(extension_name, interval=0.1)
        wait_seconds(2)

        pyautogui.press('enter', interval=0.1)
        wait_seconds(1)

        pyautogui.hotkey('command', 'down')
        wait_seconds(1)

        pyautogui.press('enter')
        wait_seconds(1)

        pyautogui.hotkey('command', 'b')
        wait_seconds(1)
    except Exception as e:
        print(f"Error Searching Extension {extension_name}: {e}")

#-------------------------------------------------------
def is_it_instelled(extension_name=''):
        try:
            wait_seconds(1)
            uninstall_coord = pyautogui.locateCenterOnScreen(image='/Users/zaidabdulmohsin/Desktop/EL2024/01_Python/02_containers/Task_03_PyAutoGUI/uninstall.png', grayscale=False, confidence=0.9 )
            wait_seconds(2)
            if uninstall_coord is not pyautogui.ImageNotFoundException:
                print(f'The Extenesion {extension_name} is installed!')
                pyautogui.hotkey('command', 'w', interval=0.1)
                return False
        except pyautogui.ImageNotFoundException:
            return True
#-------------------------------------------------------
def install_extension(extension_name=''):
    try:
        wait_seconds(1)
        install_coord = pyautogui.locateCenterOnScreen(image='/Users/zaidabdulmohsin/Desktop/EL2024/01_Python/02_containers/Task_03_PyAutoGUI/install.png', grayscale=False, confidence=0.9 )
        wait_seconds(2)
        
        if install_coord is not pyautogui.ImageNotFoundException:
            wait_seconds(1)
            pyautogui.click(install_coord, button='left', duration=1)
            print(True)
            wait_seconds(1)
            pyautogui.hotkey('command', 'w', interval=0.1)

    except pyautogui.ImageNotFoundException as e:
        print(f'Image not found for extension {extension_name}: {e}')
        pyautogui.hotkey('command', 'w', interval=0.1)
    
    except Exception as e:
        print(f'Error Installing extenesion {extension_name}: {e}')
        pyautogui.hotkey('command', 'w', interval=0.1)

#-------------------------------------------------------
def entering_extension_names():
    extensions_names = []
    print("Welcome to the VSCode Extensions Installer. Type 'Exit' to leave or 'End' to finish entering extension names and start the installation.")
    wait_seconds(1)
    while True:
        extensions_name = str(input('Please Enter extension name: '))
        if extensions_name.lower() != 'end' and extensions_name.lower() != 'exit':
            extensions_names.append(extensions_name)
        elif extensions_name.lower() == 'end' or extensions_name.lower() == 'exit':
            break
    return extensions_names, extensions_name

#--------------------------------------------
def close_vscode():
    try:
        wait_seconds(1)
        print("Thank you for your patience. Good Bye!")
        wait_seconds(1)
        pyautogui.hotkey('command', 'q', interval=0.1)
        wait_seconds(1)
    except Exception as e:
        print(f'Error Closing VSCode: {e}')
            
extensions_names, extensions_name = entering_extension_names()

if extensions_name.lower() != 'exit':
    open_vscode()
    if len(extensions_names) != 0:
        for extension in extensions_names:
            open_extensions_sildbar()
            search_extension(extension)
            if is_it_instelled():
                install_extension(extension)
    print("All Extensions have been installed.")
close_vscode()
    

