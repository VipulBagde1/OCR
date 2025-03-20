import cv2
import easyocr
from matplotlib import pyplot as plt
import numpy as np

images ='images/word.jpg'

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(images)
print(result)