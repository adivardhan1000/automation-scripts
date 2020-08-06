import pyautogui
import time
import pickle
from pynput import mouse
from pynput.keyboard import Key, Listener
print('Press Ctrl-C to quit.')
print('get ready. Going to desktop in 5 sec. AltTab -> esc -> ctrl+c -> click ')
time.sleep(5)
pyautogui.hotkey('winleft','d')

def on_press(key):
    print('{0} pressed'.format(
        key))
    if key == Key.enter:
        tasks_todo.append(['enter'])

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    tasks_todo.append((x,y))
    if not pressed:
        # Stop listener
        return False


tasks_todo = []

try:
    while True:
        with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            ) as listener:
            listener.join()
        tasks_todo.pop(-1)
        with Listener(
            on_press=on_press,
            on_release=on_release,
            ) as listener:
            listener.join()
        
        
        
except KeyboardInterrupt:
    tasks_todo.pop(-1)
    tasks_todo.pop(-1)
    with open("test.txt", "wb") as fp:
       pickle.dump(tasks_todo, fp)
    
    with open("test.txt", "rb") as fp:   # Unpickling
       tasks_todo = pickle.load(fp)
       print(tasks_todo)
    print('\nDone.')
