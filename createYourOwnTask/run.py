import pyautogui
import time
import pickle
print('Going to desktop in 5 sec.')
time.sleep(5)
pyautogui.hotkey('winleft','d')
pyautogui.PAUSE = 4
with open("test.txt", "rb") as fp:   # Unpickling
    tasks_todo = pickle.load(fp)
    print(tasks_todo)
for i in tasks_todo:
    print(i)
    if i != ['enter']:
        pyautogui.click(i)
    else:
        pyautogui.typewrite(i)
    pyautogui.PAUSE = 2
