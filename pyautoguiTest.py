import pyautogui as pgui
import time 

# print(pgui.position())
 
# print(pgui.size())
# pgui.click() 


# pgui.hotkey('command', 'space')
 
time.sleep(2)

# Cmd + SpaceをシミュレートしてSpotlightを開く
# a = pgui.hotkey('command', 'space') 
# print(a)

# Cmdキーを押してからSpaceキーを押す
pgui.keyDown('command')
pgui.press('space')
pgui.keyUp('command')
