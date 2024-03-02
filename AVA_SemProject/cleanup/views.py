from django.shortcuts import render
from django.http import HttpResponse
import pyautogui
import time
# Create your views here.

def cleanup_system(request):
    try:
        #prefetch
        pyautogui.hotkey('win', 'r')
        time.sleep(2)

        pyautogui.typewrite("prefetch")
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)

        pyautogui.hotkey('shift', 'delete')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.press('enter')

        #temp
        pyautogui.hotkey('win', 'r')
        time.sleep(2)

        pyautogui.typewrite("temp")
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)

        pyautogui.hotkey('shift', 'delete')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.press('enter')

        #%temp%
        pyautogui.hotkey('win', 'r')
        time.sleep(2)

        pyautogui.typewrite("%temp%")
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)

        pyautogui.hotkey('shift', 'delete')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.press('enter')

        time.sleep(2)
        pyautogui.leftClick(709,740)


        return HttpResponse("System cleanup completed successfully.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

