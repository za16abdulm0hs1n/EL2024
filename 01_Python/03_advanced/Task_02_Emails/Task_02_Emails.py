# This code is designed for Ubuntu; please change the hotkeys for other operating systems.

import pyautogui
import time

def wait_seconds(seconds = 1):
    time.sleep(seconds)

#--------------------------------
def clean_search_bar():
    try:
        wait_seconds(1)
        
        pyautogui.hotkey('ctrl', 'a', interval=0.1)
        wait_seconds(1)

        pyautogui.press('backspace', interval=0.1)
        wait_seconds(1)
    except Exception as e:
        print(f"Error Cleaning Search Bar: {e}")

#-------------------------------
def open_thunderbird():
    try:

        wait_seconds(1)

        pyautogui.hotkey('win', interval=0.1)
        wait_seconds(1)

        clean_search_bar()
        pyautogui.write('Thunderbird', interval=0.1)
        wait_seconds(1)

        pyautogui.press('enter', interval=0.1)
        wait_seconds(5)

    except Exception as e:
        print(f"Error Opening Thunderbird: {e}")

#--------------------------------
def open_inbox():
    try:
        
        wait_seconds(1)
        inbox_coord = pyautogui.locateCenterOnScreen(image='/home/zaidabdulmohsin/Desktop/EL2024/01_Python/03_advanced/Task_02_Emails/inbox.png', grayscale=False, confidence=0.9 )
        wait_seconds(1)
    
    except pyautogui.ImageNotFoundException :
        inbox_coord = pyautogui.locateCenterOnScreen(image='/home/zaidabdulmohsin/Desktop/EL2024/01_Python/03_advanced/Task_02_Emails/inbox2.png', grayscale=False, confidence=0.9 )
        wait_seconds(1)

    finally:
        pyautogui.click(inbox_coord, button='left', duration=1)
        wait_seconds(1)
#-------------------------------
def mark_all_emais_unread():
    try:
        wait_seconds(1)

        pyautogui.hotkey('ctrl', 'a')
        wait_seconds(1)

        pyautogui.moveTo

        pyautogui.press('m')
        wait_seconds(1)


    except Exception as e:
        print(f"Error Marking All Emails Unread: {e}")

#-------------------------------------------------

def close_thunderbird():
    try:
        wait_seconds(1)
        print("Thank you for your patience. Good Bye!")
        wait_seconds(1)
        pyautogui.hotkey('ctrl', 'q', interval=0.1)
        wait_seconds(1)
    except Exception as e:
        print(f'Error Closing Thunderbird: {e}')
            

open_thunderbird()
open_inbox()
mark_all_emais_unread()
close_thunderbird()


