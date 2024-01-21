import pyautogui as pyg
import time as t

# Open Chrome and navigate to the URL
pyg.hotkey('win', 'r')
t.sleep(1)
pyg.typewrite("chrome")
t.sleep(1)
pyg.press('enter')
t.sleep(2)
pyg.leftClick(418, 497)
t.sleep(1)
pyg.leftClick(488, 63)
t.sleep(1)
pyg.typewrite("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
t.sleep(1)
pyg.press('enter')
t.sleep(5)
pyg.leftClick(610, 110)
t.sleep(2)
pyg.typewrite("Placement")
t.sleep(2)
pyg.press('enter')