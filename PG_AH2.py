import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.05)
time.sleep(1)
pg.typewrite('https://youtu.be/2iKZ0OZtGsQ?t=50s\n',0.05)
time.sleep(7)
pg.click(807, 507)
time.sleep(0.5)
pg.hotkey('f')
