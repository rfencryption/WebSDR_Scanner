import pyautogui
import time
print("Starting WebSDR Scanner")
time.sleep(10)

pyautogui.moveTo(316,192)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1359,597)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1108, 215)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1365, 402)
pyautogui.click()
time.sleep(1)
for number in range(1000):
    pyautogui.hold('shift')
    pyautogui.press('right', presses=200)

print("DONE")