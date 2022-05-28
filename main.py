import time
import cv2
import mss
import numpy
import pytesseract
import pyautogui, sys
import tkinter as tk
from pynput.mouse import Listener
from datetime import datetime

x_i = 0
y_i = 0
x_f = 0
y_f = 0
pressed = 0

def on_click(x, y, button, pressed):
    global pressed, x_i, x_f, y_i, y_f
    if pressed:
        if pressed == 0:
            x_i = x
            y_i = y
            pressed = 1
        else:
            x_f = x - x_i
            y_f = y - y_i
            listener.stop()
            window.destroy()

def image_processing(img):
    processing = cv2.cvtColor(img, cv2.IMREAD_COLOR)        
    processing = cv2.cvtColor(processing, cv2.COLOR_BGR2GRAY)
    scaled = cv2.resize(processing, (0,0), fx=10, fy=10, interpolation = cv2.INTER_CUBIC)
    filtered = cv2.bilateralFilter(scaled, 11, 17, 17)
    thresh = cv2.threshlast_text(filtered, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    kernel = numpy.ones((5,5),numpy.uint8)
    eroded = cv2.erode(thresh, kernel, iterations = 2)
    pre_processed = eroded
    img_text = pytesseract.image_to_string(img, config='--psm 6')
    img_text = img_text.strip()
    return img_text

with mss.mss() as sct:

    #Window Creation
    window = tk.Tk()
    window.attributes('-fullscreen', True)
    window.attributes('-alpha', 0.3)
    print("Select the Top Left Corner and Bottom Right Corner of the desired Window")
    #window.after(10000, destroy_Window)

    #Mouse Coordinates recording on click
    listener = Listener(on_click=on_click)
    listener.start()

    #Window Starting
    window.mainloop()
    
    area = {'top': y_i, 'left': x_i, 'width': x_f, 'height': y_f}
    
    last_text = pytesseract.image_to_string(numpy.asarray(sct.grab(area)), config='--psm 6')
    try:
        while True:
            last_text = last_text.strip()
            img = numpy.asarray(sct.grab(area))

            img_text = image_processing(img)

            #Remove the # if you want to print the text to check
            #print(img_text)
            #print("-----REFRESH-----")

            #add conditions here
            
            last_text = img_text

            #Image GUI - Just comment if you don't want to preview
            cv2.imshow('Image', img)

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            
    except KeyboardInterrupt:
        print('\n')
