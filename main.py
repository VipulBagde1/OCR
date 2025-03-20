import cv2
import easyocr
from matplotlib import pyplot as plt
import numpy as np

images ='images/word.jpg'

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(images)
#print(result[0][0][0])

top_left= tuple(result[0][0][0])
bottom_right= tuple(result[0][0][2])
text=result[0][1]
font= cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

img=cv2.imread(images)
img=cv2.rectangle(img, top_left,bottom_right,(0,255,0),5)
img=cv2.putText(img,text,top_left,font,.5,(255,255,255),2,cv2.LINE_AA)
plt.imshow(img)
plt.show()