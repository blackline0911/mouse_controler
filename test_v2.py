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

import psutil
import time

def wait_for_process(process_name, timeout=30):
    """等待應用程式啟動，最多等待 timeout 秒"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        for process in psutil.process_iter(attrs=['name']):
            if process.info['name'].lower() == process_name.lower():
                print(f"{process_name} 已啟動")
                return True
        time.sleep(1)  # 每秒檢查一次
    print(f"超時！未偵測到 {process_name} 啟動")
    return False

# 測試啟動應用程式
import subprocess




if __name__ == '__main__':
    S=size()
    max_x = S[0]
    max_y = S[1]
    win32api.ShellExecute(0, "open", r'D:\Program Files\Nox\bin\Nox.exe', '','',1 )
    # 等待應用程式啟動
    if wait_for_process("Nox.exe"):
        print("開始執行後續動作")
    else:
        print("應用程式未啟動，請檢查")
    # time.sleep(60*1)
    # set_window_to_top("夜神模擬器")
    

    # import matplotlib.pyplot as plt
    # I = screenshot()
    # plt.figure()
    # plt.imshow(I)
    # plt.show()

    # os.system("taskkill /F /IM Nox.exe")
    # subprocess.run(["taskkill", "/F", "/IM", "Nox.exe"], shell=True)


