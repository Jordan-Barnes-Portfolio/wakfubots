import pyscreeze as pg
import pyautogui
import time
timeout = time.time() + 60*480
while True:
    if time.time() > timeout:
        break
    try:
        pg.locateOnScreen('popup.png', confidence=0.5)
        pyautogui.moveTo(pg.locateCenterOnScreen('no.png', confidence=0.7))
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(pg.locateCenterOnScreen('play.png', confidence=0.7))
        pyautogui.click()
        print("found")
        pass
    except Exception:
        pass
    time.sleep(20)

