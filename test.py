import pyautogui

# pyautogui.position() is fetching mouse position
# The Left Top of one screen is the original point
# The Negative value refer to the second screen
print(pyautogui.position())

# pyautogui.size() returns the resolution of screen
print(pyautogui.size())

# pyautogui.moveTo(x, y, duration) move the mouse to specified position in duration time (second)
# Notes:If the mouse is moved to one of the four corners of the screen, 
# PyAutoGUI raises a FailSafeException and stops execution.
# Add pyautogui.FAILSAFE = False before moveTo()
print(pyautogui.position())
pyautogui.FAILSAFE = False
pyautogui.moveTo(1920, 0, duration = 3)
print(pyautogui.position())

# pyautogui set the time spacing between commands (second)
pyautogui.PAUSE = 2.5

# pyautogui.moveRel(xOffset, yOffset, duration=seconds) moves mouse to relative position in specified time (duration)
pyautogui.moveRel(-100,100,duration=3)
pyautogui.PAUSE = 3
pyautogui.moveRel(-200,200,duration=3)

