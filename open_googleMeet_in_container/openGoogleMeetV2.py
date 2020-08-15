import webbrowser as wb
import pyautogui as pag
import time

wb.open('https://meet.google.com')

time.sleep(10)

pag.typewrite(['enter'])

time.sleep(5)
pag.hotkey('ctrl','d')
time.sleep(1)
pag.hotkey('ctrl','e')
time.sleep(1)
pag.moveTo(x=1343,y=585,duration=1) #join_now
pag.click()
print('done')

