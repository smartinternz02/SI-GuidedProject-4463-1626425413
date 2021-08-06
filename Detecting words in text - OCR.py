
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


img = cv2.imread('text.jpg')
width, height = 640,400
ImgResize=cv2.resize(img,(width,height))

img = cv2.cvtColor(ImgResize,cv2.COLOR_BGR2RGB)
    
##Detecting words
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        #b = b.split(' ') #if we gave space values will print in tab space you can remove it
        b = b.split()
        print(b)
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9]) #rectangle box coordinates
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
            #cv2.rectangle(img,(x,hImg-y),(x+w,hImg-h),(0,0,255),1)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)    

cv2.imshow('Result',img)
cv2.waitKey(0)

