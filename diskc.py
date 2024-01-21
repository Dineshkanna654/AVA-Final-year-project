import pyautogui as pg
import time as t

pg.hotkey('win')
t.sleep(1)
pg.typewrite('disk cleanup')
t.sleep(1)
pg.hotkey('enter')
t.sleep(1)
pg.leftClick(639,406)
t.sleep(3)
pg.hotkey('enter')
t.sleep(1)
pg.hotkey('enter')
t.sleep(20)

