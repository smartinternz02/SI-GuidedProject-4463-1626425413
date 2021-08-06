#Detect text and show in console
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


img = cv2.imread('text.jpg')
#width, height = 400,400
#ImgResize=cv2.resize(img,(width,height))
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))
##Detecting Characters
print(pytesseract.image_to_boxes(img))

cv2.imshow('Result',img)
cv2.waitKey(0)

