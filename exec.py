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
do = ""
while(True):
    var = random.randint(0, len(data)-3)
    proc = []
    proc.append(data[var])
    proc.append(data[var+1])
    proc.append(data[var+2])
    procB = '+'.join(proc)
    procX = ' '.join(proc)
    testimonial = TextBlob(procX)
    if prev < testimonial.sentiment.subjectivity:
        do = procB
        prev = testimonial.sentiment.subjectivity
        i=0
    if i >= 9000:
        os.system("start http://www.google.com/search?q=" + do)
        break
    i+=1
        


