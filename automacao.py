import pyautogui
import time

pyautogui.alert('O codigo vai começar, não use nada do seu computador equanto o codigo carrega.')
pyautogui.PAUSE = 1

pyautogui.press('winleft')
pyautogui.write('\\\snp305-003')
pyautogui.press('enter')
pyautogui.PAUSE = 1
pyautogui.write('login')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('enter')

pyautogui.write('soft')
pyautogui.press('enter')
pyautogui.write('programas padrão')
pyautogui.press('enter')
pyautogui.PAUSE = 1
pyautogui.write('Oc')
pyautogui.press('enter')

pyautogui.write('Ocs Inventory')
pyautogui.press('enter')
pyautogui.keyDown('left')
pyautogui.keyUp('left')
pyautogui.press('enter')

pyautogui.write('login')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('enter')

pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')

pyautogui.write('http://ocsnti/ocsinventory')
pyautogui.press('enter')
pyautogui.press('enter')

pyautogui.click(x=1228, y=630)

