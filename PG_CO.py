import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n', 0.25)
pg.hotkey('winleft','up')
pg.typewrite('donovan mitchel stats\n', 0.25)

time.sleep(4)

pg.hotkey('space')

time.sleep(1)

pg.click(272, 210)

time.sleep(20)

pg.click(1122, 574, 2)

time.sleep(56.5)

pg.click(1122, 574, 2)

