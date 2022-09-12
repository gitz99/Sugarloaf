###pyautogui

## Reference URL
# https://pypi.org/project/PyAutoGUI/
# https://pyautogui.readthedocs.io/en/latest/keyboard.html - Keyboard_Keys

##Import
import pyautogui

# Basics
screenWidth, screenHeight = pyautogui.size() # Width&Height of primary monitor
currentMouseX, currentMouseY = pyautogui.position() #Current Mouse cursor position

pyautogui.moveTo(100,150) #Move the mouse to (100,150) coordinates
pyautogui.moveTo(100,150, duration=2) #Move the mouse to (100,150) coordinates with 2second duration
pyautogui.click() #Click
pyautogui.click(100,150) #Click at (100,150) coordinates
pyautogui.doubleClick() #Double click

pyautogui.write('Hello world!', interval=0.25) #Type with quarter-second pause in between each key
pyautogui.press('esc') #Press esc key

pyautogui.keyDown('shift')
pyautogui.press('left')
pyautogui.press('left')
pyautogui.press('left')
pyautogui.keyUp('shift')
#with pyautogui.hold('shift'):
    #pyautogui.press(['left','left','left'])
pyautogui.hotkey('ctrl','c')

# Displaying Message Boxes
pyautogui.alert('This is an alert box.')
pyautogui.confirm('Shall I proceed?')
pyautogui.prompt('What is your name?')
pyautogui.password('Enter password (text will be hidden)')

# Screen shot Functions
im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')
im2 = pyautogui.screenshot('my_screenshot2.png')

# Locating where an image is on the screenshot
button7location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
buttonx, buttony = pyautogui.center(button7location)
# buttonx, buttony = pyautogui.locateCenterOnScreen('button.png')
pyautogui.click(buttonx, buttony) # click the center of where the button was found
