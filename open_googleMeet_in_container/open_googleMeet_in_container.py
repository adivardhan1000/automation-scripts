import pyautogui, time

pyautogui.typewrite(['winleft'])
pyautogui.PAUSE = 1
pyautogui.typewrite('mozilla firefox',0.15)
pyautogui.typewrite(['enter'])
pyautogui.PAUSE = 5
temp = pyautogui.locateOnScreen('container.png')
container = pyautogui.center(temp)
pyautogui.click(container)
temp = pyautogui.locateOnScreen('open_new_tab.png')
new_tab_at = pyautogui.center(temp)
pyautogui.click(new_tab_at)
temp = pyautogui.locateOnScreen('open_work_tab.png')
open_work_tab = pyautogui.center(temp)
pyautogui.click(open_work_tab)
pyautogui.typewrite('meet.google.com')
pyautogui.typewrite(['enter'])