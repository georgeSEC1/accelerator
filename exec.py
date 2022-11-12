from PIL import Image
import numpy as np
import cv2
import os
import pyautogui
import pytesseract
import random
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
cv2.imwrite("test.png", image)
data = pytesseract.image_to_string(Image.open('test.png')).split(" ")
var = random.randint(0, len(data)-2)
proc = []
proc.append(data[var])
proc.append(data[var])
procB = '+'.join(proc)
os.system("start http://www.google.com/search?q=" + procB)
 


