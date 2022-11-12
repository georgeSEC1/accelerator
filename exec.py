from PIL import Image
import numpy as np
import cv2
import os
import pyautogui
import pytesseract
import random
from textblob import TextBlob
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
cv2.imwrite("test.png", image)
data = pytesseract.image_to_string(Image.open('test.png')).split(" ")
prev = 0
i = 0
while(True):
    var = random.randint(0, len(data)-2)
    proc = []
    proc.append(data[var])
    proc.append(data[var+1])
    procB = '+'.join(proc)
    procX = ' '.join(proc)
    testimonial = TextBlob(procX)
    if prev < testimonial.sentiment.polarity:
        prev = testimonial.sentiment.polarity
        i=0
    if i >= 1280:
        os.system("start http://www.google.com/search?q=" + procB)
        break
    i+=1
        


