from pyautogui import *
import os
import time
import subprocess
import win32api
import win32con
import win32gui

# Showing all working window name
# windows = getAllWindows()
# for window in windows:
#     print(window.title)

def set_window_to_top(win_name):
    hwnd = win32gui.FindWindow(None, win_name)
    
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)
        win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, max_x, max_y,  win32con.SWP_SHOWWINDOW)
    else:
        print("Window with name", win_name, " not found")


if __name__ == '__main__':
    S=size()
    max_x = S[0]
    max_y = S[1]
    # win32api.ShellExecute(0, "open", r'D:\Program Files\Nox\bin\Nox.exe', '','',1 )
    set_window_to_top("夜神模擬器")
    # time.sleep(60*1)

    # import matplotlib.pyplot as plt
    # I = screenshot()
    # plt.figure()
    # plt.imshow(I)
    # plt.show()

    # os.system("taskkill /F /IM Nox.exe")
    # subprocess.run(["taskkill", "/F", "/IM", "Nox.exe"], shell=True)


