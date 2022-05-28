# Image Reader
Read texts from images

## Intro
This project is focused on reading the text from a image with pytesseract in live time within a specific area selected and it can output the text in many ways depending on what you want, as an example you can read a text and then do a http request.
The code has a preview of the area that is reading, so you can adjust the pytesseract config to the optimal settings. Just comment it out to stop previewing.

## Packages
pip packages requirement:
- mss==6.1.0
- numpy==1.22.3
- pytesseract==0.3.9
- pyautogui==0.9.53
- pynput==1.7.6
- datetime==4.3
