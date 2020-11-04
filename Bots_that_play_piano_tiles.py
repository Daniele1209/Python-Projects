import pyautogui
import time
import keyboard
import random
import win32api, win32con

#tile positions:
# - tile_1 X:1128 Y:875
# - tile_2 X:1224 Y:875
# - tile_3 X:1324 Y:875
# - tile_4 X:1420 Y:875

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(1128, 875)[0] == 0:
        click(1128, 875)
    if pyautogui.pixel(1224, 875)[0] == 0:
        click(1224, 875)
    if pyautogui.pixel(1324, 875)[0] == 0:
        click(1324, 875)
    if pyautogui.pixel(1420, 875)[0] == 0:
        click(1420, 875)